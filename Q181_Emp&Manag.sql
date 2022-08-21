-- Question: Table Employee has id as primary key and following columns: name, salary, managerId.
-- Table includes manager's info as well.
-- Write a query to find employees who earn more than their managers.

SELECT
    E.name AS Employee
FROM Employee E, Employee M
WHERE E.managerId = M.id AND E.salary > M.salary
