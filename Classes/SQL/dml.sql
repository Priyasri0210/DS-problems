 -- Data manipulation Language
 -- Insert - insert the values inside the table
 -- insert into table_name (columns) values (values)
 insert into Employees (Id,Name,Department,Salary) 
 values(1, 'Bharath Kumar','SE',50000.0)
 
 insert into Employees (Id,Name,Department,Salary) 
 values(2, 'Sam','SE',50000.0)
 
 -- select - to get the values from table
 -- select <* , column name> from table_name
 select * from Employees
 
 -- update - to update the values inside the table
 -- update table_name set column_name = new_value where condition
 update Employees set salary = 60000.0 WHERE Id = 1
 
 -- Delete 
 delete from Employees where id = 1



 --DDL
 --DML
 --DCL -- Database Admins (grant,revoke)
 --TCL



 1 - 10 ---> changed
 11 - 1000 ---> unchanged
