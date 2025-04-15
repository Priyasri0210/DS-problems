
select c.customer_id,
concat(c.first_name,' ' , c.last_name) as Full_name,
count(r.rental_id) as rental_count,
 rank() over (order by count(r.rental_id) desc) as ranking
 from customer c
 inner join rental r on c.customer_id = r.customer_id
 group by c.customer_id,c.first_name,c.last_name 
 order by ranking LIMIT 10;
 
 select c.customer_id,c.first_name,c.last_name,count(r.rental_id) as rental_count,
 dense_rank() over (order by count(r.rental_id) desc) as ranking
 from customer c
 inner join rental r on c.customer_id = r.customer_id
 group by c.customer_id,c.first_name,c.last_name 
 order by ranking LIMIT 10;
 
 select r.rental_id,c.first_name,c.last_name,f.title as film_title,r.rental_date
 from rental r
 inner join customer c on r.customer_id = c.customer_id
 inner join inventory i on r.inventory_id = i.inventory_id
 inner join film f on i.film_id = f.film_id;
 
 select c.customer_id,c.first_name,c.last_name,count(r.rental_id) as total_rentals
 from customer c
 left join rental r on r.customer_id = c.customer_id
 group by c.customer_id,c.first_name,c.last_name;

select *from payment;
select s.staff_id,s.first_name,s.last_name,sum(p.amount) as Total_payment 
from payment p
right join staff s on p.staff_id = s.staff_id
group by s.staff_id,s.first_name,s.last_name;

select avg(amount),min(amount),max(amount) from payment;

select monthname(payment_date) as month,sum(amount) as total_revenue 
from payment
group by month(payment_date),monthname(payment_date) order by month(payment_date);

select payment_id, amount , round(amount) as round_amount
from payment;

select amount,sqrt(amount) as sqrt_amount from payment;

select amount,mod(amount,5) as modulo_amount from payment;