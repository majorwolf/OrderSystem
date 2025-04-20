
# 📄 1861 Public House Ordering System – Product Requirements Document (PRD)

## 1. Executive Summary

The **1861 Public House Ordering System** is a modular, containerized web application that enables restaurant patrons to order food and drinks via QR codes at their table. This system will digitize menu presentation and order intake, aiming to improve service speed, order accuracy, and operational coordination between staff roles (kitchen, bar, admin).

## 2. Objective

To build a simple, platform-agnostic, ordering platform with a static HTML/CSS/JS frontend and a PostgreSQL backend — all deployed within a Docker Compose stack. The application should be extremely lightweight and easy to understand and modify without needing any developer tools or package management.

## 3. Platform Requirements

- ✅ **Docker Compose Compatible**: Must be deployable as a multi-container stack (frontend, backend, database)
- ✅ **PostgreSQL**: Required as the primary relational database
- ✅ **Static Frontend**: Use HTML, Tailwind CSS, and vanilla JavaScript
- ✅ **Tailwind CSS Allowed**: Tailwind CDN may be included via `<script>` tag
- 🚫 **No Package Installation**: Do not use npm, yarn, or build tools
- 🚫 **No JavaScript Frameworks**: No React, Node.js, or TypeScript

## 4. Target Users

| Role | Description |
|------|-------------|
| Customer | Scans QR code, browses menu, places order |
| Kitchen Staff | Views and updates food orders |
| Bar Staff | Views and updates drink orders |
| Admin | Manages menu, orders, tables, QR codes |

## 5. System Architecture Overview

```yaml
# Docker Compose Stack (High-Level)

services:
  frontend: [Static HTML/CSS/JS served by Nginx]
  backend: [Lightweight backend API to serve data to/from PostgreSQL]
  database: [PostgreSQL]
```

## 6. Core Components

- **QR System**: Maps QR to table ID
- **Frontend (Static HTML/CSS/JS)**: Customer, Kitchen, Bar, Admin interfaces
- **Backend (Minimal REST API)**: Order processing, data persistence, and routing
- **Database (PostgreSQL)**: Stores menu items, orders, users, and table data
- **Admin Panel**: Accessible interface for managing the system

## 7. Functional Requirements

### 7.1 Customer Flow
- Scan table-specific QR → load menu
- Browse menu → customize items (especially pizzas)
- Add items to cart → submit order with last name
- Receive confirmation with simple visual cue

### 7.2 Staff Interfaces

| Interface | Features |
|----------|----------|
| **Kitchen** | View food orders, update status |
| **Bar** | View drink orders, update status |
| **Admin** | Login required. Manage menu, toppings, QR codes, tables |

### 7.3 Order Routing
- Orders automatically split: `kitchen`, `bar`, or `both`
- Items routed to respective dashboards
- Status flows: `new` → `preparing` → `ready` → `delivered`
- Order completed when all components are `delivered`

## 8. UI Requirements

### Shared UI Guidelines
- Use HTML for structure, Tailwind CSS (via CDN) for styling, and vanilla JavaScript for interactivity
- Avoid frontend build tools or preprocessors
- Fully responsive design using Tailwind utility classes

### Pages
- **Customer**: Menu, Cart, Pizza Customizer, Order Confirmation
- **Kitchen**: Order Queue, Status Update, Filtering
- **Bar**: Drink Orders, Status Update
- **Admin**: Login Page, Menu CRUD, Toppings, QR code tools, Settings

## 9. API Specification

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/menu` | Retrieve all menu items |
| GET    | `/api/menu/:id` | Retrieve a specific item |
| POST   | `/api/orders` | Submit a new order |
| GET    | `/api/orders/type/:type` | Get orders for kitchen or bar |
| PATCH  | `/api/orders/:id/status` | Update status |
| POST   | `/api/auth/login` | Authenticate admin user |
| GET    | `/api/auth/me` | Get logged-in admin info |

## 10. Database Design (PostgreSQL)

**Tables**:
- `menu_items` (id, name, type, price, description, is_available)
- `toppings` (id, name, price, is_available)
- `menu_item_toppings` (menu_item_id, topping_id)
- `tables` (id, qr_code_token, table_number)
- `orders` (id, table_id, last_name, created_at)
- `order_items` (id, order_id, menu_item_id, customizations, type, status)
- `admins` (id, username, password_hash, created_at)

> Order item `status` tracks individual fulfillment state (`new`, `preparing`, `ready`, `delivered`)

## 11. Technical Requirements

### 11.1 Performance
- <2s page loads on average mobile device
- 100+ concurrent users
- 50 orders/min sustained throughput

### 11.2 Security
- HTTPS via Nginx
- Admin login authentication using username + password
- Input validation client-side and server-side
- Simple authentication token/session-based access

### 11.3 Resilience & Monitoring
- 99.9% uptime
- PostgreSQL backup scripts
- Error logging written to local files or syslog

### 11.4 Simplicity
- No TypeScript or frontend build system
- No Node.js or external runtime required
- All assets directly usable in browser (HTML, CSS, JS)

## 12. Business Logic

- Custom pizzas can have toppings added/removed
- Topping price added per item
- Large pizza: +$2 surcharge
- Orders must include a last name
- Menu/toppings can be toggled without deletion

## 13. Deployment Plan

- **Nginx**: Serves static frontend (reverse proxy handled externally)
- **Lightweight Backend**: Provides JSON API for data transactions
- **PostgreSQL**: Volume-mapped for persistence
- **Docker Compose**: All services orchestrated together

## 14. Status

All features are in the planning phase. No components are currently implemented.

## 15. Roadmap

| Feature | Priority |
|--------|----------|
| Admin login system | 🔄 High |
| Customer order history | 🔄 High |
| Analytics dashboard | 🔄 Medium |
| Inventory management | 🔄 Low |
| Kitchen display integrations | 🔄 Low |

## 16. Maintenance

- Auto-backups for PostgreSQL
- Periodic updates to HTML/CSS/JS files as needed
- Monitor nginx access/error logs
- Feedback loop via admin dashboard
