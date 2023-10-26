SELECT Department.name as "Department", Employee.name as "Employee", Employee.salary as "Salary"
FROM Employee
LEFT JOIN Department 
On Employee.departmentID = Department.id
WHERE (departmentID, salary) IN
    (
    SELECT departmentID, Max(salary)
    FROM Employee
    Group By departmentID
    )