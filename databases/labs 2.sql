
--  Excersise 1
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER
);

-- Excersise 2
DROP TABLE books;

CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER CHECK (year > 1400)
);
 
 -- Excersise 3
 ALTER TABLE books ADD COLUMN isbn TEXT;
 
 -- Excersise 4
 DROP TABLE books;

  -- Excersise 5
 CREATE TABLE reviews (
	review_id  INTEGER PRIMARY KEY,
	product_id INTEGER,
	comment TEXT,
	rating INTEGER CHECK (rating > 0 AND rating <= 5),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
 );

 -- Excersise 6  
INSERT INTO reviews (review_id, product_id, comment, rating)
	VALUES (1, 1, 'Megakass skräp', 6);
	
-- Result: CHECK constraint failed: rating > 0 AND rating <= 5

 -- Excersise 7  
INSERT INTO reviews (review_id, product_id, comment, rating)
	VALUES (2, 50, 'Kanonbäst!', 5);
-- Result: FOREIGN KEY constraint failed

-- Extra challenges Exercise 1
CREATE TABLE suppliers (
	supplier_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	country TEXT DEFAULT 'Sweden',
	email TEXT
);

-- Extra challenges Exercise 2
INSERT INTO suppliers (name, email)
	VALUES ('Kalle', 'kalle@mail.se')

-- Extra challenges Exercise 3
INSERT INTO suppliers (name, email)
	VALUES ('Nordic Textiles', 'kalle@mail.se')

	--Result: UNIQUE constraint failed: suppliers.name

-- Extra challenges Exercise 4
CREATE TABLE coupons (
	code TEXT PRIMARY KEY,
	discount_percent INTEGER CHECK (discount_percent BETWEEN 1 AND 90),
	valid_until TEXT NOT NULL
);

-- Extra challenges Exercise 5
INSERT INTO suppliers (name, email)
	VALUES ('Kalle', 'kalle@mail.se');
-- Result: CHECK constraint failed: discount_percent BETWEEN 1 AND 90

-- Extra challenges Exercise 6
ALTER TABLE suppliers RENAME COLUMN email TO contact_email;

-- Extra challenges Exercise 7
PRAGMA table_info(products);

-- 0	product_id	INTEGER	0		1
-- 1	name	TEXT	1		0
-- 2	category	TEXT	0		0
-- 3	price	REAL	0		0
-- 4	stock	INTEGER	0		0


-- Extra challenges Exercise 8
-- Extra challenges Exercise 9
