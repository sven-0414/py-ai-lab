SELECT orders.order_id, customers.first_name, customers.last_name, orders.status 
	FROM orders
	JOIN customers ON orders.customer_id = customers.customer_id;