-- aggregate functions
-- count()
-- sum()
-- avg()
-- max()
-- min()

--count
select count(*) from film

select * from customer
select * from address
select * from city

select ct.city, count(c.customer_id) as count_of_members
from customer c
inner join address a on c.address_id = a.address_id
inner join city ct on ct.city_id = a.city_id
group by ct.city

-- sum()
select * from payment
select sum(amount) from payment

-- avg()
select avg(amount) from payment

-- max
select max(amount) from payment

-- min
select min(amount) from payment

-- sum(group by)
select customer_id, sum(amount)
from payment
group by customer_id