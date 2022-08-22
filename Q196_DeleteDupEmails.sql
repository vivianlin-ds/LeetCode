-- Question: Table Person has id as primary key and contains emails in lowercase.
-- Write a query to delete all duplicate emails, keeping only on unique email with smallest id.

DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id
