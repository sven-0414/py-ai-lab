-- Excersise 1
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

  -- Excersise 5
 CREATE TABLE reviews (
	review_id  INTEGER PRIMARY KEY,
	product_id INTEGER,
	comment TEXT,
	rating INTEGER CHECK (rating > 0 AND rating <= 5) 
FOREIGN KEY (product_id) REFERENCES products(product_id)
 )

 -- Excersise 6
 -- Excersise 7
 -- Excersise 8
