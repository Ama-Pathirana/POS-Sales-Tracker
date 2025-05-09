show databases;
DROP DATABASE IF EXISTS pos_sales_tracker;

CREATE DATABASE pos_sales_tracker;


-- Drop child tables first due to foreign key constraints
DROP TABLE IF EXISTS sale_items;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS stores;

DROP TABLE IF EXISTS sale_items, sales, products, stores;

CREATE TABLE stores (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR(100),
    location VARCHAR(255)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    stock_quantity INT,
    store_id INT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT,
    sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE sale_items (
    sale_item_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT,
    product_id INT,
    quantity INT,
    item_price DECIMAL(10,2),
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


INSERT INTO stores (store_name, location)
VALUES 
  ('Main Street Store', 'Downtown'),
  ('Uptown Branch', 'Uptown');
  
  
  INSERT INTO products (product_name, price, stock_quantity, store_id)
VALUES 
  ('Coffee', 5.00, 100, 1),
  ('Tea', 3.50, 150, 1),
  ('Sandwich', 7.25, 60, 1),
  ('Muffin', 2.75, 80, 2),
  ('Juice', 4.00, 120, 2);


INSERT INTO sales (store_id, sale_date, total_amount)
VALUES 
  (1, '2025-05-09 08:15:00', 13.50),
  (1, '2025-05-09 09:30:00', 10.00),
  (2, '2025-05-09 10:05:00', 8.75);


-- Sale 1: Coffee x2, Tea x1 (total = 5*2 + 3.5 = 13.5)
INSERT INTO sale_items (sale_id, product_id, quantity, item_price)
VALUES 
  (1, 1, 2, 5.00),
  (1, 2, 1, 3.50);

-- Sale 2: Sandwich x1, Tea x1 (total = 7.25 + 3.5 = 10.75, but assume discount/promo = 10.00)
INSERT INTO sale_items (sale_id, product_id, quantity, item_price)
VALUES 
  (2, 3, 1, 7.25),
  (2, 2, 1, 3.50);

-- Sale 3: Muffin x2 (total = 2 * 2.75 = 5.50) and Juice x1 (4.00)
INSERT INTO sale_items (sale_id, product_id, quantity, item_price)
VALUES 
  (3, 4, 2, 2.75),
  (3, 5, 1, 4.00);






