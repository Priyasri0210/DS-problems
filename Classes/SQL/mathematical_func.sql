-- abs(absolute) ---> converts to positive number
-- 10 - 5 --> 5
-- 5 - 10 --> -5
-- abs(5-10) --> 5
select payment_id, amount , abs(amount-5) as absolute_amount
from payment

-- ceil
select payment_id, amount , ceil(amount) as ceil_amount
from payment

-- floor
select payment_id, amount , floor(amount) as floor_amount
from payment

-- round
select payment_id, amount , round(amount,1) as round_amount
from payment

-- mod
select * from rental
select rental_id,mod(rental_id,2) as is_odd
from rental

-- power()
select rental_id,power(rental_id,2) as powered_value
from rental

-- sqrt()
select rental_id, sqrt(rental_id) as sqrt_value
from rental