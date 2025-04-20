-- Insert sample menu items
INSERT INTO menu_items (name, type, price, description) VALUES
('Margherita Pizza', 'pizza', 12.99, 'Classic tomato sauce, mozzarella, and basil'),
('Pepperoni Pizza', 'pizza', 14.99, 'Tomato sauce, mozzarella, and pepperoni'),
('Veggie Pizza', 'pizza', 13.99, 'Tomato sauce, mozzarella, mushrooms, bell peppers, and onions'),
('Cheeseburger', 'kitchen', 9.99, 'Beef patty with cheese, lettuce, and tomato'),
('Chicken Wings', 'kitchen', 10.99, 'Crispy chicken wings with your choice of sauce'),
('Caesar Salad', 'kitchen', 8.99, 'Romaine lettuce, croutons, parmesan, and Caesar dressing'),
('Craft Beer', 'bar', 6.99, 'Local craft beer on tap'),
('House Wine', 'bar', 7.99, 'Glass of house red or white wine'),
('Cocktail', 'bar', 9.99, 'Signature house cocktail');

-- Insert sample toppings
INSERT INTO toppings (name, price) VALUES
('Extra Cheese', 1.50),
('Pepperoni', 1.50),
('Mushrooms', 1.00),
('Bell Peppers', 1.00),
('Onions', 1.00),
('Olives', 1.00),
('Bacon', 2.00),
('Sausage', 2.00);

-- Insert sample tables
INSERT INTO tables (qr_code_token, table_number) VALUES
('table1', '1'),
('table2', '2'),
('table3', '3'),
('table4', '4'),
('table5', '5');

-- Insert sample admin user (password: admin123)
INSERT INTO admins (username, password_hash) VALUES
('admin', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW'); 