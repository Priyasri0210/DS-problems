-- create a new database

-- create database <database_name>
create database datascience

-- Data Definition Language
-- Creating a table
-- create table <table_name> (Column_name Datatype)
create table Employees (
 Id INT,
 Name VARCHAR(100),
 Department VARCHAR(60)
 )
 
 
 -- Altering the table
 -- alter table table_name ADD column_name datatype
 alter table Employees ADD Salary Decimal(10,2)
 
 
 #Drop
 #drop table table_name - Deletes objects from database
 drop table Employees
 
 -- Truncate
 -- drop table table_name - removes all the rows, but it doesn't delete the schema
 truncate table Employees 
 
 