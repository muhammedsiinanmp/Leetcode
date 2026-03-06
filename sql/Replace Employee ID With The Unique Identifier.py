"""
LeetCode 1378: Replace Employee ID With The Unique Identifier
Category: SQL
Difficulty: Easy

Problem
-------
Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

Table: EmployeeUNI
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| unique_id   | int     |
+-------------+---------+

Write a SQL query to show the unique ID of each employee.  
If an employee does not have a unique ID, return NULL instead.

Approach
--------
1. Use a LEFT JOIN between the Employees table and EmployeeUNI table.
2. Join them using the common column `id`.
3. LEFT JOIN ensures that all employees appear in the result even if
   they do not have a matching unique identifier.
4. Select `unique_id` from EmployeeUNI and `name` from Employees.

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(1)
"""

"""
SELECT 
    u.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI u
ON e.id = u.id;
"""