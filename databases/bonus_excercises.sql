SELECT * FROM products
WHERE category IN ('Clothing', 'Accessories')
  AND price BETWEEN 150 AND 500
ORDER BY price DESC;

SELECT * FROM orders
WHERE order_date >= '2026-02-01' AND order_date < '2026-03-01'
  AND status != 'cancelled';
  
SELECT order_items.order_id, products.name, order_items.quantity, order_items.quantity * order_items.unit_price AS line_total
	FROM order_items
	JOIN products ON order_items.product_id = products.product_id
	WHERE order_items.quantity * order_items.unit_price > 500
	ORDER BY line_total DESC;
	
SELECT DISTINCT customers.first_name, customers.last_name, customers.city
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
WHERE customers.city IN ('Uppsala', 'Stockholm');

-- Excercise 5
INSERT INTO customers (customer_id, first_name, last_name, city)
	VALUES (11, 'Leo', 'Falk', 'Uppsala');

INSERT INTO orders (order_id, customer_id, order_date)
	VALUES (16, 11, DATE('now'));

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
	VALUES
		(16, 1, 1, 599),   
		(16, 9, 2, 129);   
	
-- Exercise 6
UPDATE orders SET status = 'cancelled' WHERE order_id = 12;
UPDATE products SET stock = stock + 1 WHERE name = 'Sneakers Classic';
UPDATE products SET stock = stock + 1 WHERE name = 'Socks 3-pack';

-- Excersice 7
DELETE FROM products WHERE product_id = 1;
-- Result: FOREIGN KEY constraint failed
-- Order_intems point to this product with FOREIGN KEY:s
-- The shop needs to inactivate the product without deleting it. For exampe set stock to 0 och change category to 'Inactive'

-- Excercise 8
ALTER TABLE products ADD COLUMN discount_percent INTEGER DEFAULT 0 CHECK (discount_percent BETWEEN 0 AND 90);

UPDATE products SET discount_percent = 20 WHERE category = 'Shoes';

SELECT name, price, price * (1 - discount_percent / 100.0) AS price_after_discount
FROM products;