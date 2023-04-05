CREATE DATABASE budget_management;

-- drop database budget_management;

USE budget_management;

CREATE TABLE budget_user
(user_id int not null auto_increment primary key,
username varchar(50),
user_password varchar(50),
title varchar(10),
first_name varchar(50),
last_name varchar(50)
);

CREATE TABLE budget_account
(account_id int not null auto_increment primary key,
account_name varchar(50),
account_type varchar(50),
income_total decimal
);
-- Adding foreign key to 'budget_account' table 
ALTER TABLE budget_account
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

CREATE TABLE income
(income_id int not null auto_increment primary key,
income_source varchar(50),
income_date varchar(50),
income_total decimal
);

CREATE TABLE expense
(expense_id int not null auto_increment primary key,
expense_source varchar(50),
expense_date varchar(50),
expense_total decimal
);


CREATE TABLE category
-- To look at types of incoming and outgoing money e.g. food, holidays, bills etc 
(category_id int not null auto_increment primary key,
category_name varchar(50)
);
-- Adding foreign keys to 'category' table 
ALTER TABLE category
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE category
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE category
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);

CREATE TABLE weekly_budget
(weekly_budget_id int not null auto_increment primary key,
weekly_balance decimal
);

-- Adding foreign keys to 'weekly_budget' table 
ALTER TABLE weekly_budget
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE weekly_budget
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE weekly_budget
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);

ALTER TABLE weekly_budget
ADD COLUMN category_id int,
ADD foreign key(category_id) references category(category_id);




CREATE TABLE monthly_budget
(monthly_budget_id int not null auto_increment primary key,
monthly_balance decimal
);

-- Adding foreign keys to 'monthly_budget' table 
ALTER TABLE monthly_budget
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE monthly_budget
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE monthly_budget
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);

ALTER TABLE monthly_budget
ADD COLUMN category_id int,
ADD foreign key(category_id) references category(category_id);


CREATE TABLE annual_budget
(annual_budget_id int not null auto_increment primary key,
annual_balance decimal
);

-- Adding foreign keys to 'weekly_budget' table 
ALTER TABLE annual_budget
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE annual_budget
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE annual_budget
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);

ALTER TABLE annual_budget
ADD COLUMN category_id int,
ADD foreign key(category_id) references category(category_id);


CREATE TABLE custom_budget
(custom_budget_id int not null auto_increment primary key,
custom_balance decimal
);

-- Adding foreign keys to 'custom_budget' table 
ALTER TABLE custom_budget
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE custom_budget
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE custom_budget
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);

ALTER TABLE custom_budget
ADD COLUMN category_id int,
ADD foreign key(category_id) references category(category_id);

-- insert data into budget_user table
INSERT INTO budget_user (username, user_password, title, first_name, last_name)
VALUES
('BillGates', 'microsoft365', 'Mr', 'Bill', 'Gates');

-- insert data into budget_account table
INSERT INTO budget_account (account_name, account_type)
VALUES
('Bill Gates Savings Account', 'Savings Account');

-- insert data into income table
INSERT INTO income (income_source, income_date, income_total)
VALUES
('Microsoft Revenue', 2022-31-12, 1000000.00);

-- insert data into expense table
INSERT INTO expense (expense_source, expense_date, expense_total)
VALUES
('Mortgage', '2023-01-01', 50000.00);

-- insert data into category table
INSERT INTO category (category_name)
VALUES
('Housing Bills');

select *
from income;

select * 
from budget_user;

select *
from category;

-- inner join to compare income and expenses 
select
username, income_total, expense_total
from budget_user
inner join expense
on budget_user.user_id = expense.expense_id
inner join income
on budget_user.user_id = income.income_id;





