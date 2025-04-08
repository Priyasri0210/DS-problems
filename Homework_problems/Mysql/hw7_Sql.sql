create database Datascience;
create table Books ( Book_id int,title varchar(50),author varchar(50),published_year int);
create table Members (member_id int,name varchar(50),join_date date);
create table borrowed_books (borrow_id int,book_id int,member_id int,borrow_date date);

insert into books (Book_id, title, author, published_year)
values (1, 'The Alchemist', 'Paulo Coelho', 1993);
insert into books (Book_id, title, author, published_year)
values (2, 'Cybersecurity', 'Alice Brown', 1990);
insert into books (Book_id, title, author, published_year)
values (3, 'Python for Beginners', 'John Doe', 1890);

select * from books;

insert into members (member_id, name, join_date) values (101,'Andrew','2019-02-10');
insert into members (member_id, name, join_date) values (102,'John','2023-10-10');
select * from members;

insert into borrowed_books (borrow_id, book_id, member_id, borrow_date) values (1001,1,101,'2024-02-10');
insert into borrowed_books (borrow_id, book_id, member_id, borrow_date) values (1002,3,102,'2024-03-10');
select * from borrowed_books;

select title, author from books;
select * from members where join_date > '2023-01-01';

-- SET SQL_SAFE_UPDATES = 0;
update books set title = 'Advanced python' where Book_id = 103;
delete from books where Book_id = 102;
select * from books;

