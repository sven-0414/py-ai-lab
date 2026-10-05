-- Lab 1 Databases
-- Sven Eriksson
--1
SELECT first_name, email FROM customers;
--2
SELECT * FROM products WHERE category = 'Shoes';
--3
SELECT * FROM customers WHERE city =  "Uppsala";
--4
SELECT * FROM products WHERE price = 199;
--5
SELECT * FROM products ORDER BY name;
--6
SELECT * FROM customers ORDER BY joined_date;
--7
SELECT * FROM products WHERE stock is 0;
--8
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;
--9
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');
--10
SELECT name AS product , price AS price_sek  FROM products;
-- Bonus 1
SELECT * FROM  products WHERE (category = 'Clothing' OR category = 'Shoes') AND price > 1000;
-- Bonus 2
SELECT name, price, stock, price * stock AS stock_value FROM products ORDER BY stock_value DESC;
-- Bonus 3
SELECT * FROM customers WHERE first_name LIKE '____';
-- Bonus 4
SELECT * FROM products ORDER BY price  LIMIT 5 OFFSET 5;
-- Bonus 5
SELECT * FROM customers WHERE joined_date < '2025-01-01' AND city != 'Uppsala' ORDER BY city, last_name
