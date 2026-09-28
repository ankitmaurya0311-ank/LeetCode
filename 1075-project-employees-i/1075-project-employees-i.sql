# Write your MySQL query statement below
select Project.project_id , round(avg(Employee.experience_years),2) as average_years 
from project 
join Employee on Employee.employee_id = Project.employee_id 
group by Project_id 
