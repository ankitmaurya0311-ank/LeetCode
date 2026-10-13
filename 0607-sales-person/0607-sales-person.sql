select name from salesPerson 
where sales_id not in (select orders.sales_id from orders join company on company.com_id = orders.com_id where company.name = 'Red' )