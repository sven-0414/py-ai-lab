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

-- Extra challenges Exercise 4
-- Extra challenges Exercise 5
-- Extra challenges Exercise 6
-- Extra challenges Exercise 7
-- Extra challenges Exercise 8
-- Extra challenges Exercise 9
