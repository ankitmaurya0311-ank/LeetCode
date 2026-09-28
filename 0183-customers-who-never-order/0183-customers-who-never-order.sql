# Write your MySQL query statement below
select customers.name as Customers from customers 
left join Orders on orders.customerId = Customers.id
where orders.customerId is null 