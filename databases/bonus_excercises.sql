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

INSERT INTO customers (customer_id, first_name, last_name, city)
	VALUES (11, 'Leo', 'Falk', 'Uppsala');

INSERT INTO orders (order_id, customer_id, order_date)
	VALUES (16, 11, DATE('now'));

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
	VALUES
		(16, 1, 1, 599),   -- 1 Hoodie Black
		(16, 9, 2, 129);   -- 2 Socks 3-pack