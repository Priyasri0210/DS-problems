-- Rank
-- dense_rank

-- rank() - it skips the next number if same rank applies more than 1 time
-- 1 - 100  - 1
-- 2 - 100  - 1
-- 3 - 99   - 3
-- 4 - 98   - 4
-- 5 - 95   - 5

-- dense_rank() 
-- 1 - 100  - 1
-- 2 - 100  - 1
-- 3 - 99   - 2
-- 4 - 98   - 3
-- 5 - 95   - 4

select title,length,
rank() over (order by length desc) as Ranking
from film

select title,length,
dense_rank() over (order by length desc) as Ranking
from film

--exists
select * from customer c
where exists (
select 1 from rental_temp r where r.customer_id = c.customer_id
)