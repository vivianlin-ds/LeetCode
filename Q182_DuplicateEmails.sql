-- Question: Table Person has id as the primary key and contains email (all lowercase)
-- Write a query to report all duplicate emails.

SELECT email AS Email
FROM Person
GROUP BY email HAVING COUNT(email) > 1
