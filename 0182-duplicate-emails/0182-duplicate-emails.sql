# Write your MySQL query statement below





select p.email as Email
from person p 
group by Email
having count(Email)>1