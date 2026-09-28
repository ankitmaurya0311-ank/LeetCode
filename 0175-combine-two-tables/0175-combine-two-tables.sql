# Write your MySQL query statement below
select Person.firstNAme , Person.lastName ,Address.city , address.state from person
left join address on address.PersonID = person.personid

