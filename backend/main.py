from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import menu, orders, tables, toppings, admin, auth

app = FastAPI(title="1861 Public House Ordering System")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(menu.router, prefix="/admin/menu", tags=["menu"])
app.include_router(orders.router, prefix="/admin/orders", tags=["orders"])
app.include_router(tables.router, prefix="/admin/tables", tags=["tables"])
app.include_router(toppings.router, prefix="/admin/toppings", tags=["toppings"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(auth.router, prefix="/admin/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to 1861 Public House Ordering System API"} 