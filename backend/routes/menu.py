from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import MenuItem
from ..schemas import MenuItem as MenuItemSchema

router = APIRouter(prefix="/api/menu", tags=["menu"])

@router.get("/", response_model=List[MenuItemSchema])
async def get_menu_items(db: Session = Depends(get_db)):
    """Get all available menu items"""
    items = db.query(MenuItem).filter(MenuItem.is_available == True).all()
    return items

@router.get("/{item_id}", response_model=MenuItemSchema)
async def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific menu item by ID"""
    item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item 