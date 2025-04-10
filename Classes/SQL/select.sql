-- used to switch the database
use sakila
select * from film

-- Distinct
select distinct rating from film

--where clause
select title,rating from film where rating = 'PG'
select * from actor

--Aliases
select first_name as Fname, last_name as Lname from actor

--AND OR NOT
select title,rating,length from film 
where (rating = 'PG' or rating = 'G') or length > 120

--IN
select title,rating from film 
where rating in ('PG','R')

-- Between
select title,release_year from film
where release_year between 2005 and 2006

-- Order by
-- use desc for descending, ascending is default
select * from country
select * from country order by country desc

-- Groupby
-- Having by(having should definitely have groupby)
select rating,length, count(*) as count from film
group by rating,length
having count > 200

--CASE
select title, length,
	case 
		when length > 120 Then 'Long'
        when length between 90 and 120 then 'medium'
        else 'short'
	end as length_category
from film

--Top
select * from film limit 5

--Nested query
select title,rating from film
where rating = (select rating from film where title = 'ALADDIN CALENDAR')

-- order of execution of query

-- select rating, count(*) as total
-- from film
-- where length > 60
-- groupby rating
-- having total > 100
-- order by total desc
-- limit 5; 


-- 1. from film
-- 2. where length > 60
-- 3. groupby rating
-- 4. having total > 100
-- 5. select rating, count(*) as total
-- 6. order by total desc
-- 7. limit 5; 

-- nested query
-- select * from film where rating = (select rating from film where id = 1)
-- BODMAS
-- bracket of division multiply addition substraction