1. Connect to Database using admin
mysql -u root -p

2. Create new user
create user <username>@<localhost> IDENTIFIED BY <password>;

-- DCL --> Data Control Language
3. Grant permissions
grant all privileges on expense_tracker.* to 'bharath'@'localhost'
grant select,update,insert on sakila.* to 'bharath'@'localhost'

4. Remove permissions
revoke select,update,insert on sakila.* to 'bharath'@'localhost'