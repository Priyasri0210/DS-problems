create database expense_tracker
use expense_tracker

create table categories(
 Id Int auto_increment Primary key,
 name Varchar(50) unique
 )

create table expenses (
  Id Int auto_increment Primary key,
  amount Decimal(10,2),
  description Text, 
  date Date,
  category_id Int,
  Foreign key (category_id) references categories(Id)
  on delete cascade
  on update cascade
  )

  INSERT INTO categories (name) VALUES
('Food'),
('Transport'),
('Rent'),
('Utilities'),
('Entertainment'),
('Healthcare'),
('Shopping'),
('Education'),
('Travel'),
('Miscellaneous');


INSERT INTO expenses (amount, description, date, category_id) VALUES
(80.00, 'Bus pass for April', '2025-04-02', 2)

INSERT INTO expenses (amount, description, date, category_id) VALUES
(80.00, 'Bus pass for April', '2025-04-02', (
select Id from categories where name = 'Transport'))