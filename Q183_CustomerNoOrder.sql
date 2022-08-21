-- Question: Table Customers has id as primary key and contains name of the customer.
-- Table Orders has id as primary key and customerId as foreign key.
-- Write a query to report all customers who never order anything.

SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders)
