
-- Ex. 1
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title	TEXT NOT NULL,
	author	TEXT,
	year	INTEGER
);


-- Ex. 2
DROP TABLE books;

CREATE TABLE books(
	book_id	INTEGER PRIMARY KEY,
	title	TEXT NOT NULL,
	author	TEXT,
	year	INTEGER CHECK (year > 1400)
);


-- Ex. 3
ALTER TABLE books ADD COLUMN isbn TEXT;


-- Ex. 4
DROP TABLE books;


-- Ex. 5
CREATE TABLE reviews(
	review_id	INTEGER PRIMARY KEY,
	product_id	INTEGER NOT NULL,
	rating		INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
	comment		TEXT,
	FOREIGN KEY(product_id) REFERENCES products(product_id)
);


-- Ex. 6
INSERT INTO reviews (review_id, product_id, rating, comment)
VALUES(1, 10, 6, 'Great');

-- Error occurs: CHECK constraint failed: rating BETWEEN 1 AND 5


-- Ex. 7
INSERT INTO reviews (review_id, product_id, rating, comment)
VALUES(1, 50, 5, 'Great');

-- Error occurs: Result: FOREIGN KEY constraint failed, product_id = 50 does not exsits
