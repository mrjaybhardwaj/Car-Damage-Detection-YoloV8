create database car_project2;

use car_project2;
show tables;
create table user_reg(
user_id int primary key auto_increment,
name varchar(20),
gender varchar(10),
address varchar(50),
contact_number varchar(20),
car_compeny varchar(20),
car_model varchar(20),
manufacturing_year int,
email_address varchar(20),
password varchar(30)
);

select * from user_reg;