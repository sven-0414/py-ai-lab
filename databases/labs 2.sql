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
 -- Excersise 4
 -- Excersise 5
 -- Excersise 6
 -- Excersise 7
 -- Excersise 8
