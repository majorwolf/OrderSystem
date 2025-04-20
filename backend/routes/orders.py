from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Order, OrderItem, Table
from ..schemas import Order as OrderSchema, OrderCreate, OrderItem as OrderItemSchema

router = APIRouter(prefix="/api/orders", tags=["orders"])

@router.post("/", response_model=OrderSchema)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """Create a new order"""
    # Verify table exists
    table = db.query(Table).filter(Table.id == order.table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")

    # Create order
    db_order = Order(
        table_id=order.table_id,
        last_name=order.last_name
    )
    db.add(db_order)
    db.flush()  # Get the order ID

    # Create order items
    for item in order.items:
        db_item = OrderItem(
            order_id=db_order.id,
            menu_item_id=item.menu_item_id,
            customizations=item.customizations,
            type=item.type,
            status="new"
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/type/{order_type}", response_model=List[OrderSchema])
async def get_orders_by_type(order_type: str, db: Session = Depends(get_db)):
    """Get orders by type (kitchen or bar)"""
    if order_type not in ["kitchen", "bar"]:
        raise HTTPException(status_code=400, detail="Invalid order type")

    orders = db.query(Order).join(OrderItem).filter(
        OrderItem.type == order_type,
        OrderItem.status != "delivered"
    ).distinct().all()
    return orders

@router.patch("/{order_id}/status", response_model=OrderItemSchema)
async def update_order_status(
    order_id: int,
    item_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    """Update the status of an order item"""
    if status not in ["new", "preparing", "ready", "delivered"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    order_item = db.query(OrderItem).filter(
        OrderItem.order_id == order_id,
        OrderItem.id == item_id
    ).first()

    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    order_item.status = status
    db.commit()
    db.refresh(order_item)
    return order_item 