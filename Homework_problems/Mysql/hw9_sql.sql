use  sakila;
select distinct rating from film;

select title,length from film order by length desc limit 5;

select * from address
select * from country

select title as movie_title, rental_rate as rate from film;
select * from film;

update film set rental_rate = rental_rate + 0.5 where  rating='G';
select * from film where (rating = 'PG' AND rental_duration > 5) OR rating != 'R';

select title,length from film
where length between 90 and 120;

select first_name,last_name from actor order by last_name desc;

select rating , count(*) as film_count from film group by rating;

select rating , count(*) as film_count from film group by rating having count(*) > 200;

select title, length,
	case 
		when length < 60 Then 'short'
        when length between 60 and 120 then 'medium'
        else 'short'
	end as length_category
from film;

select first_name,last_name from customer where customer_id NOT IN ( select distinct customer_id from rental);

select *  from rental