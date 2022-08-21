-- Question: Table Person has personId as primary key and contains info about ID of some persons and their names.
-- Table Address has addressId as primary key and contains info about city and state of one person.
-- Write a query to report first name, last name, city, and state of each person.

SELECT
    P.lastName, P.firstName,
    A.city, A.state
FROM Person P
-- Using LEFT JOIN to achieve NULL if person doesn't have corresponding Address entry.
LEFT JOIN Address A ON A.PersonId = P.PersonId
