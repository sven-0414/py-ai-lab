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