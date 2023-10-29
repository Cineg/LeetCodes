SELECT name as Customers
FROM Customers
where Customers.id not in ( 
    SELECT customerId FROM Orders
);