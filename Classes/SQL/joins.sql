-- Joins
-- combining tables together is called joins\
-- Inner joins
-- Left joins
-- Right join
-- full join

-- inner joins ---> returns only the matching rows from both table
-- left join(left outer join) ---> return matching row from both table along with all the rows in the left table
-- right join(right outer join) --> return matching row from both table along with all the rows in the right table
-- full join ---> combination of left and right join (union)

--inner join
select f.title , c.name
from film f
inner join film_category fc on f.film_id = fc.film_id
inner join category c on c.category_id = fc.category_id

-- left join
select c.first_name , c.last_name , r.rental_date
from customer c
left join rental_temp r on c.customer_id = r.customer_id


-- right join
select c.first_name , c.last_name , r.rental_date
from customer_temp c
right join rental_temp r on c.customer_id = r.customer_id


--full join(not supported in mysql, so use union)
select c.first_name , c.last_name , r.rental_date
from customer c
left join rental_temp r on c.customer_id = r.customer_id
union
select c.first_name , c.last_name , r.rental_date
from customer_temp c
right join rental_temp r on c.customer_id = r.customer_id