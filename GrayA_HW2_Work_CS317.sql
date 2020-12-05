SELECT receipts.customer_id, first_name, last_name, SUM(receipts.amount) totalSpent
FROM customers
INNER JOIN receipts ON customers.customer_id = receipts.customer_id 
GROUP BY customer_id 
ORDER BY SUM(amount) DESC
LIMIT 4;

SELECT receipts.customer_id, first_name, last_name, AVG(receipts.amount) avgSpent
FROM customers
INNER JOIN receipts on customers.customer_id = receipts.customer_id
GROUP BY customer_id
ORDER BY AVG(amount) DESC
LIMIT 5;

SELECT receipts.customer_id, customers.first_name, customers.last_name, COUNT(*) purchases
FROM receipts
INNER JOIN customers ON receipts.customer_id = customers.customer_id
GROUP BY customer_id
ORDER BY COUNT(*) DESC
LIMIT 3;

SELECT purchase_date, COUNT(*)
FROM receipts
GROUP BY purchase_date
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT purchase_date, SUM(amount) profit
FROM receipts
GROUP BY purchase_date
ORDER BY SUM(amount) DESC
LIMIT 1;

SELECT receipts.customer_id, first_name, last_name
FROM customers
INNER JOIN receipts ON customers.customer_id = receipts.customer_id
WHERE purchase_date = '2018-05-27';

SELECT street_address
FROM students
GROUP BY street_address
HAVING COUNT(*) = 2;

SELECT first_name, last_name
FROM students 
INNER JOIN (SELECT street_address
FROM students
GROUP BY street_address
HAVING COUNT(*) = 2) AS siblings
ON students.street_address = siblings.street_address;

SELECT last_name, street_address, birthday
FROM students
GROUP BY birthday, street_address
HAVING COUNT(*) = 2;

SELECT first_name, last_name
FROM students
INNER JOIN (SELECT birthday, street_address
FROM students
GROUP BY birthday, street_address
HAVING COUNT(*) = 2) AS twins
ON students.birthday = twins.birthday
AND students.street_address = twins.street_address;