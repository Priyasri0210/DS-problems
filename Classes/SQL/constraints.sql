-- NOT NULL - It ensures the column cannot be Null
create table Employees(
 Id INT,
 Name VARCHAR(100),
 Department VARCHAR(60),
 Salary Decimal(10,2) NOT NULL
 )

 -- Unique - ensures all the values in a column are different
 create table Employees_3 (
 Id INT UNIQUE,
 Name VARCHAR(100),
 Department VARCHAR(60),
 Salary Decimal(10,2) NOT NULL
 )

 -- Primary key - combination of unique key and not null(uniquely
 -- identifying the each records in table)
create table College (
 RollNo INT PRIMARY KEY,
 Name VARCHAR(100),
 Department VARCHAR(60)
 )

 -- Foreign key - 
 -- if you are creating a foreign key in a table, it should be primary key
 -- in other table
 create table Student (
 RollNo INT PRIMARY KEY,
 Name VARCHAR(100),
 Department_id INT,
 Foreign key (Department_id) references Department(DeptId)
 )

 -- check - check the condition to add into the table
   create table Age (
 Name varchar(50),
 Age Int check (Age > 0)
 )

-- Default - Sets default value to the column if not given
 create table bank_status(
 UserId Int,
 status varchar(20) default 'active'
 )

 -- auto_increment
create table Student_table (
 RollNo INT auto_increment,
 Name VARCHAR(100),
 Department_id INT,
 Primary Key(RollNo)
 )