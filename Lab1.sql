
-- Ex.1
SELECT first_name, email FROM customers;

-- Ex.2 
SELECT * FROM products WHERE category = 'Shoes';

-- Ex.3.
SELECT * FROM customers WHERE city = 'Uppsala';

-- Ex.4
SELECT * FROM products WHERE price = 199;

-- Ex.5
SELECT * FROM products ORDER BY name ASC;

-- Ex.6
SELECT * FROM customers ORDER BY joined_date ASC;

-- Ex.7
SELECT * FROM products WHERE stock = 0;

-- Ex.8
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;

-- Ex.9
SELECT * FROM customers
WHERE city IN ('Stockholm', 'Göteborg');

-- Ex.10
SELECT name AS product, price AS price_sek FROM products;



--Bonus questions:

-- Ex.11
SELECT * FROM products
WHERE category IN ('Clothing', 'Shoes') AND price > 1000;

-- Ex.12
SELECT name, price, stock, price * stock AS stock_value FROM products
WHERE stock > 0 ORDER BY stock_value DESC;

-- Ex.13
SELECT * FROM customers
WHERE first_name LIKE '____';

-- Ex.14
SELECT * FROM products
ORDER BY price ASC
LIMIT 5 OFFSET 5;

-- Ex.15
SELECT * FROM customers
WHERE joined_date < '2025-01-01' AND city <> 'Uppsala'
ORDER BY city, last_name;