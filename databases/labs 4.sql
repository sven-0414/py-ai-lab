SELECT orders.order_id, customers.first_name, customers.last_name, orders.status 
	FROM orders
	JOIN customers ON orders.customer_id = customers.customer_id;
	
SELECT orders.order_id, customers.first_name
	FROM orders
	JOIN customers ON customers.customer_id = orders.customer_id 
	WHERE customers.first_name = 'Erik';

SELECT orders.order_id, customers.first_name, customers.last_name, customers.city, orders.status
	FROM orders
	JOIN customers ON customers.customer_id = orders.customer_id 
	WHERE customers.city = "Göteborg";
	
SELECT *, products.name, products.category FROM order_items
	JOIN products ON products.product_id = order_items.product_id;

SELECT order_items.order_id , products.name
	FROM order_items
	JOIN products ON products.product_id = order_items.product_id
	WHERE products.category = 'Shoes';
	
SELECT products.name, order_items.quantity, order_items.unit_price, order_items.quantity * order_items.unit_price AS line_total
	FROM order_items
	JOIN products ON products.product_id = order_items.product_id
	WHERE order_items.order_id = 10;
	
