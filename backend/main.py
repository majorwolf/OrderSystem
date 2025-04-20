from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import menu, orders

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
app.include_router(menu.router)
app.include_router(orders.router)

@app.get("/")
async def root():
    return {"message": "Welcome to 1861 Public House Ordering System API"} 