create database Datascience;
drop table books,members,borrowed_books;
 
create table Books ( Book_id int Primary Key,title varchar(50) not null,author varchar(50),published_year int);
create table Members (member_id int Primary Key,name varchar(50) not null,join_date date);
create table borrowed_books (
borrow_id INT,book_id INT,member_id INT,borrow_date DATE,
PRIMARY KEY (borrow_id),
FOREIGN KEY (book_id) REFERENCES books(book_id),
FOREIGN KEY (member_id) REFERENCES members(member_id));

insert into books (Book_id, title, author, published_year)
values ( 1,'The Alchemist', 'Paulo Coelho', 1993);
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

update books set published_year = 1970 where Book_id = 3;
alter table books MODIFY published_year YEAR;

alter table books ADD CONSTRAINT published_year CHECK(published_year >= 1970);
insert into books (Book_id, title, author, published_year)
values (4, 'Advanced Python', 'John Doe', 1972);


