2. write a function that will accept two strings and return Boolean if they are anagram
 str1 = rail safety
 str2= fairy tales


def check_ang(str1, str2):
    A = sorted([x.lower() for x in str1 if x != ' '])
    B = sorted([x.lower() for x in str2 if x != ' '])
    return A == B

with main as (
 
select dept_name,emp_id,salary from hawa_dept as a left join hawa_emp as b on a.dept_id = b.dept_id)


select distinct dept_name,count(emp_id) over (partition by dept_name order by (select null)) as emp_count,
isnull(max(salary) over (partition by dept_name order by (select null)),0) as max_dept_sal
from main

SQL problem -

 DECLARE @emp_id INT = 2;

WITH emp_hierarchy AS (
    -- Start with the given employee
    SELECT 
        id,
        name,
        managerid
    FROM jaban_emp
    WHERE id = @emp_id

    UNION ALL

    -- Recursively find each manager
    SELECT 
        e.id,
        e.name,
        e.managerid
    FROM jaban_emp e
    INNER JOIN emp_hierarchy eh
        ON e.id = eh.managerid
)
-- Select all names, from top manager to the employee
SELECT name
FROM emp_hierarchy
ORDER BY CASE WHEN managerid IS NULL THEN 0 ELSE 1 END, id;


