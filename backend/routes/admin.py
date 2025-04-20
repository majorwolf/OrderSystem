from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
from ..database import get_db
from .. import models, schemas
from ..auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

# Menu Item Management
@router.get("/menu", response_model=List[schemas.MenuItem])
async def get_menu_items(
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    return db.query(models.MenuItem).all()

@router.post("/menu", response_model=schemas.MenuItem)
async def create_menu_item(
    menu_item: schemas.MenuItemCreate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    db_menu_item = models.MenuItem(**menu_item.dict())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

@router.put("/menu/{item_id}", response_model=schemas.MenuItem)
async def update_menu_item(
    item_id: int,
    menu_item: schemas.MenuItemCreate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    db_menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not db_menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    for key, value in menu_item.dict().items():
        setattr(db_menu_item, key, value)
    
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

@router.delete("/menu/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_menu_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    db.delete(menu_item)
    db.commit()
    return None

# Table Management
@router.get("/tables", response_model=List[schemas.Table])
async def get_tables(
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    return db.query(models.Table).all()

@router.post("/tables", response_model=schemas.Table)
async def create_table(
    table: schemas.TableCreate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    db_table = models.Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.put("/tables/{table_id}", response_model=schemas.Table)
async def update_table(
    table_id: int,
    table: schemas.TableCreate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    db_table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")
    
    for key, value in table.dict().items():
        setattr(db_table, key, value)
    
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete("/tables/{table_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_table(
    table_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    
    db.delete(table)
    db.commit()
    return None

# Topping Management
@router.get("/toppings", response_model=List[schemas.Topping])
async def get_toppings(
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    return db.query(models.Topping).all()

@router.post("/toppings", response_model=schemas.Topping)
async def create_topping(
    topping: schemas.ToppingCreate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    db_topping = models.Topping(**topping.dict())
    db.add(db_topping)
    db.commit()
    db.refresh(db_topping)
    return db_topping

@router.put("/toppings/{topping_id}", response_model=schemas.Topping)
async def update_topping(
    topping_id: int,
    topping: schemas.ToppingCreate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    db_topping = db.query(models.Topping).filter(models.Topping.id == topping_id).first()
    if not db_topping:
        raise HTTPException(status_code=404, detail="Topping not found")
    
    for key, value in topping.dict().items():
        setattr(db_topping, key, value)
    
    db.commit()
    db.refresh(db_topping)
    return db_topping

@router.delete("/toppings/{topping_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_topping(
    topping_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    topping = db.query(models.Topping).filter(models.Topping.id == topping_id).first()
    if not topping:
        raise HTTPException(status_code=404, detail="Topping not found")
    
    db.delete(topping)
    db.commit()
    return None

# Menu Item Availability
@router.patch("/menu/{item_id}/availability", response_model=schemas.MenuItem)
async def update_menu_item_availability(
    item_id: int,
    availability: schemas.MenuItemAvailability,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    menu_item.is_available = availability.is_available
    db.commit()
    db.refresh(menu_item)
    return menu_item

# Table Status Management
@router.patch("/tables/{table_id}/status", response_model=schemas.Table)
async def update_table_status(
    table_id: int,
    status_update: schemas.TableStatusUpdate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    
    table.status = status_update.status
    db.commit()
    db.refresh(table)
    return table

# Order Management
@router.get("/orders", response_model=List[schemas.Order])
async def get_orders(
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    return db.query(models.Order).all()

@router.get("/orders/{order_id}", response_model=schemas.Order)
async def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/orders/{order_id}/items/{item_id}", response_model=schemas.OrderItem)
async def update_order_item_status(
    order_id: int,
    item_id: int,
    status_update: schemas.OrderItemStatusUpdate,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    order_item = db.query(models.OrderItem).filter(
        models.OrderItem.order_id == order_id,
        models.OrderItem.id == item_id
    ).first()
    
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")
    
    order_item.status = status_update.status
    db.commit()
    db.refresh(order_item)
    return order_item

@router.get("/orders/table/{table_id}", response_model=List[schemas.Order])
async def get_orders_by_table(
    table_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    return db.query(models.Order).filter(models.Order.table_id == table_id).all()

@router.get("/orders/history", response_model=List[schemas.Order])
async def get_order_history(
    start_date: datetime = None,
    end_date: datetime = None,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    query = db.query(models.Order)
    
    if start_date:
        query = query.filter(models.Order.created_at >= start_date)
    if end_date:
        query = query.filter(models.Order.created_at <= end_date)
    
    return query.all()

@router.get("/orders/stats", response_model=schemas.OrderStats)
async def get_order_stats(
    start_date: datetime = None,
    end_date: datetime = None,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    query = db.query(models.Order)
    
    if start_date:
        query = query.filter(models.Order.created_at >= start_date)
    if end_date:
        query = query.filter(models.Order.created_at <= end_date)
    
    orders = query.all()
    
    total_orders = len(orders)
    total_revenue = sum(
        sum(item.price for item in order.items)
        for order in orders
    )
    
    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "average_order_value": total_revenue / total_orders if total_orders > 0 else 0
    }

# Menu Item Toppings Management
@router.get("/menu/{item_id}/toppings", response_model=schemas.MenuItemWithToppings)
async def get_menu_item_toppings(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_item

@router.post("/menu/{item_id}/toppings/{topping_id}", response_model=schemas.MenuItemTopping)
async def add_menu_item_topping(
    item_id: int,
    topping_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    topping = db.query(models.Topping).filter(models.Topping.id == topping_id).first()
    if not topping:
        raise HTTPException(status_code=404, detail="Topping not found")
    
    # Check if the topping is already associated with the menu item
    existing = db.query(models.MenuItemTopping).filter(
        models.MenuItemTopping.menu_item_id == item_id,
        models.MenuItemTopping.topping_id == topping_id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Topping already associated with menu item")
    
    menu_item_topping = models.MenuItemTopping(
        menu_item_id=item_id,
        topping_id=topping_id
    )
    db.add(menu_item_topping)
    db.commit()
    db.refresh(menu_item_topping)
    return menu_item_topping

@router.delete("/menu/{item_id}/toppings/{topping_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_menu_item_topping(
    item_id: int,
    topping_id: int,
    db: Session = Depends(get_db),
    current_user: models.Admin = Depends(get_current_user)
):
    menu_item_topping = db.query(models.MenuItemTopping).filter(
        models.MenuItemTopping.menu_item_id == item_id,
        models.MenuItemTopping.topping_id == topping_id
    ).first()
    
    if not menu_item_topping:
        raise HTTPException(status_code=404, detail="Menu item topping not found")
    
    db.delete(menu_item_topping)
    db.commit()
    return None 