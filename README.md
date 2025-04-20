# 1861 Public House Ordering System

A modern, efficient ordering system for 1861 Public House that allows customers to place orders directly from their tables and provides staff with a comprehensive admin panel for order management.

## System Overview

The system consists of two main components:
1. Customer-facing ordering interface
2. Staff/admin management panel

## Customer Ordering System

### Accessing the Menu
- Customers scan the QR code at their table
- They are automatically directed to the menu page for that specific table
- No login or registration required

### Features
- Browse available menu items
- View item descriptions and prices
- Add items to order
- Customize orders with available toppings
- Submit orders directly to kitchen/bar
- View order status in real-time

## Admin Panel

### Access
- URL: `/admin`
- Default credentials:
  - Username: `admin`
  - Password: `admin123`

### Features

#### Menu Management
- Add, edit, and delete menu items
- Set item prices
- Add descriptions
- Toggle item availability
- Manage item-topping relationships

#### Table Management
- Add, edit, and delete tables
- Set table capacity
- Update table status (available, occupied, reserved)
- Generate and print QR codes for tables

#### Topping Management
- Add, edit, and delete toppings
- Set topping prices
- Assign toppings to menu items

#### Order Management
- View all active orders
- Filter orders by type (kitchen/bar)
- Update order status (new, preparing, ready, delivered)
- View order history
- Access order statistics

#### Statistics
- View total orders
- Track revenue
- Calculate average order value
- Monitor busiest hours
- Identify popular menu items

## Technical Details

### Backend
- Built with FastAPI
- PostgreSQL database
- JWT authentication
- RESTful API endpoints

### Frontend
- Modern, responsive design
- Tailwind CSS for styling
- Vanilla JavaScript for interactivity
- Real-time updates

## Setup Instructions

### Prerequisites
- Python 3.9+
- PostgreSQL
- Node.js (for frontend development)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ordersystem.git
cd ordersystem
```

2. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure the database:
- Create a PostgreSQL database
- Update the DATABASE_URL in `.env` file

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the backend server:
```bash
uvicorn main:app --reload
```

6. Access the application:
- Customer interface: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin`

## Security Notes

- Change default admin credentials immediately after first login
- Use environment variables for sensitive information
- Implement proper CORS policies in production
- Use HTTPS in production environment

## Support

For technical support or questions, please contact:
- Email: support@1861publichouse.com
- Phone: (555) 123-4567

## License

This project is licensed under the MIT License - see the LICENSE file for details.