# Write your MySQL query statement belosl\
select Visits.customer_id , count(*) as count_no_trans 
from Visits
left join Transactions on Transactions.visit_id = visits.visit_id
where Transactions.visit_id is null 
group by Visits.customer_id
