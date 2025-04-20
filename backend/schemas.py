from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class MenuItemBase(BaseModel):
    name: str
    type: str
    price: float
    description: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ToppingBase(BaseModel):
    name: str
    price: float

class ToppingCreate(ToppingBase):
    pass

class Topping(ToppingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TableBase(BaseModel):
    number: int
    capacity: int
    status: str = "available"

class TableCreate(TableBase):
    pass

class Table(TableBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    menu_item_id: int
    customizations: Optional[Dict[str, Any]] = None
    type: str

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    status: str

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    table_id: int
    last_name: str

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class Order(OrderBase):
    id: int
    created_at: datetime
    items: List[OrderItem]

    class Config:
        from_attributes = True

class AdminBase(BaseModel):
    username: str

class AdminCreate(AdminBase):
    password: str

class Admin(AdminBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class OrderItemStatusUpdate(BaseModel):
    status: str

    class Config:
        orm_mode = True

class MenuItemAvailability(BaseModel):
    is_available: bool

    class Config:
        orm_mode = True

class TableStatusUpdate(BaseModel):
    status: str

    class Config:
        orm_mode = True

class MenuItemToppingBase(BaseModel):
    menu_item_id: int
    topping_id: int

class MenuItemToppingCreate(MenuItemToppingBase):
    pass

class MenuItemTopping(MenuItemToppingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MenuItemWithToppings(MenuItem):
    toppings: List[Topping] = []

    class Config:
        orm_mode = True

class OrderItemCustomization(BaseModel):
    toppings: List[int] = []
    special_instructions: Optional[str] = None

    class Config:
        orm_mode = True

class OrderStats(BaseModel):
    total_orders: int
    total_revenue: float
    average_order_value: float

    class Config:
        orm_mode = True 