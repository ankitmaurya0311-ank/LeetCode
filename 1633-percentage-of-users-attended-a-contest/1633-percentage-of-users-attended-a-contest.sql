# Write your MySQL query statement below
select contest_id , round(count(distinct user_id)*100.00/(select Count(*)from Users ),2) as percentage
from register 
group by Contest_id 
order by percentage desc, contest_id asc
