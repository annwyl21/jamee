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

CREATE TABLE income
(income_id int not null auto_increment primary key,
income_source varchar(50),
income_total decimal
);

CREATE TABLE expense
(expense_id int not null auto_increment primary key,
expense_source varchar(50),
expense_total decimal
);

CREATE TABLE category
-- To look at types of incoming and outgoing money e.g. food, holidays, bills etc 
(category_id int not null auto_increment primary key,
category_name varchar(50)
);

CREATE TABLE debt
(debt_total_id int not null auto_increment primary key,
debt_total_figure decimal,
debt_source varchar(50))
;

CREATE TABLE savings
(savings_total_id int not null auto_increment primary key,
savings_total_figure decimal,
savings_source varchar(50))
;


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


-- Adding foreign keys to the 'debt' table 
ALTER TABLE debt
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE debt
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE debt
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);


-- Adding foreign keys to the 'savings' table 
ALTER TABLE savings
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE savings
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE savings
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);




-- insert test data into budget_user table
-- INSERT INTO budget_user (username, user_password, title, first_name, last_name)
-- VALUES
('BillGates', 'microsoft365', 'Mr', 'Bill', 'Gates');

-- insert data into income table
-- INSERT INTO income (income_source, income_date, income_total)
-- VALUES
-- ('Microsoft Revenue', 2022-31-12, 1000000.00);

-- insert data into expense table
-- INSERT INTO expense (expense_source, expense_date, expense_total)
-- VALUES
-- ('Mortgage', '2023-01-01', 50000.00);

-- insert data into category table
-- INSERT INTO category (category_name)
-- VALUES
-- ('Housing Bills');


-- Inserting annual expenses for renters 
INSERT INTO expense (expense_source, expense_total)
VALUES
('Annual average food and drink (renters)', 4415.00),
('Annual average energy bills (renters)', 1345.00),
('Annual average rent (renters)', 9247.00),
('Annual average housing costs (homeowners)', 12650.00),
('Annual average petrol/diesel (renters)', 1172.00),
('Annual average train fares (renters)', 216.00),
('Annual average bus fares (renters)', 318.00),
('Annual average eating/drinking out (renters)', 3415.00),
('Annual average holidays (renters)', 1541.00),
('Annual average clothes (renters)', 2178.00);



-- Inserting monthly expenses for renters
INSERT INTO expense (expense_source, expense_total)
VALUES
('Monthly average food/drink (renters and homeowers)',368.00), 
('Monthly average energy bills (renters and homeowers)', 112.00),
('Monthly average rent (renters)', 771.00),
('Monthly average housing costs (homeowners)', 1054.00),
('Monthly average petrol/diesel (renters and homeowers)', 98.00),
('Monthly average train fares (renters and homeowers)', 18.00),
('Monthly average bus fares (renters and homeowers), 26.00'),
('Monthly average eating/drinking out (renters and homeowers)', 285.00),
('Monthly average holidays (renters and homeowers)',128.00);


-- Inserting weekly expenses for renters
INSERT INTO expense (expense_source, expense_total)
 VALUES
 ('Weekly average food/drink (renters and homeowers)', 85.00),
 ('Weekly average energy bills (renters and homeowers)', 26.00),
 ('Weekly average rent (renters)', 178.00),
 ('Weekly average housing costs (homeowners)', 243.00),
 ('Weekly average petrol/diesel (renters and homeowers)', 23.00),
 ('Weekly average train fares (renters and homeowers)', 4.00),
 ('Weekly average bus fares (renters and homeowers)', 6.00),
 ('Weekly eating/drinking out (renters and homeowers)', 66.00),
 ('Weekly average holidays (renters and homeowers)', 30.00),
 ('Weekly average clothes/footwear (renters and homeowers)', 42.00);



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





