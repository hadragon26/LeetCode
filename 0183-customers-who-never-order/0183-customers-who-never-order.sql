# Write your MySQL query statement below


select c.name Customers
from customers c
where c.id not in (select o.customerId from orders o )