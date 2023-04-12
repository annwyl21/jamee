CREATE DATABASE budget_management;

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
income_source varchar(200),
income_total decimal
);

CREATE TABLE expense
(expense_id int not null auto_increment primary key,
expense_source varchar(200),
expense_total decimal
);

CREATE TABLE category
-- To look at types of incoming and outgoing money e.g. food, holidays, bills etc 
(category_id int not null auto_increment primary key,
category_name varchar(100)
);

CREATE TABLE debt
(debt_total_id int not null auto_increment primary key,
debt_total_figure decimal,
debt_source varchar(100),
debt_interest int(5),
debt_term int(5),
debt_monthsyears varchar(10)
);

CREATE TABLE savings
(savings_total_id int not null auto_increment primary key,
savings_total_figure decimal,
savings_source varchar(100))
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
-- ('BillGates', 'microsoft365', 'Mr', 'Bill', 'Gates');

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


-- Inserting annual expenses for renters and homeowners
-- INSERT INTO expense (expense_source, expense_total)
-- VALUES
-- ('Annual average weekly food and drink (renters and homeowers)', 4415.00),
-- ('Annual average weekly energy bills (renters and homeowers)', 1345.00),
-- ('Annual average weekly rent (renters)', 9247.00),
-- ('Annual average weekly housing costs (homeowners)', 12650.00),
-- ('Annual average weekly petrol/diesel (renters and homeowers)', 1172.00),
-- ('Annual average weekly train fares (renters and homeowers)', 216.00),
-- ('Annual average weekly bus fares (renters and homeowers)', 318.00),
-- ('Annual average weekly eating/drinking out (renters and homeowers)', 3415.00),
-- ('Annual average weekly holidays (renters and homeowers)', 1541.00),
-- ('Annual average weekly clothes (renters and homeowers)', 2178.00);



-- Inserting monthly expenses for renters and homeowners
INSERT INTO expense (expense_source, expense_total)
VALUES
('Monthly average food/drink (renters and homeowers)',368.00), 
('Monthly average energy bills (renters and homeowers)', 112.00),
('Monthly average rent (renters)', 771.00),
('Monthly average housing costs (homeowners)', 1054.00),
('Monthly average petrol/diesel (renters and homeowers)', 98.00),
('Monthly average train fares (renters and homeowers)', 18.00),
('Monthly average bus fares (renters and homeowers)', 26.00),
('Monthly average eating/drinking out (renters and homeowers)', 285.00),
('Monthly average holidays (renters and homeowers)',128.00);


-- Inserting weekly expenses for renters and homeowners
-- INSERT INTO expense (expense_source, expense_total)
--  VALUES
--  ('Weekly average food/drink (renters and homeowers)', 85.00),
--  ('Weekly average energy bills (renters and homeowers)', 26.00),
--  ('Weekly average rent (renters)', 178.00),
--  ('Weekly average housing costs (homeowners)', 243.00),
--  ('Weekly average petrol/diesel (renters and homeowers)', 23.00),
--  ('Weekly average train fares (renters and homeowers)', 4.00),
--  ('Weekly average bus fares (renters and homeowers)', 6.00),
--  ('Weekly eating/drinking out (renters and homeowers)', 66.00),
--  ('Weekly average holidays (renters and homeowers)', 30.00),
--  ('Weekly average clothes/footwear (renters and homeowers)', 42.00);



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


select *
from expense;

-- stored procedure to grab a list of monthly expense data from the database
DELIMITER //
create procedure average_monthly_data()
begin
select expense_total from expense;
end //
DELIMITER ;

-- drop procedure average_monthly_data;

call average_monthly_data();

-- Using a database as a content management system
-- url endpoints are in the name field and attach to this base url https://www.gov.uk/

create table benefits
	(benefit_id int not null auto_increment primary key,
    benefit_name varchar (50),
    how varchar (500),
    what varchar (500));
    
-- Child Benefit data
insert into benefits(benefit_name, how, what) 
values 
    ('child-benefit', 
    'You get Child Benefit if you are responsible for bringing up a child who is; under 16 or under 20 if they stay in approved education or training. Only one person can get Child Benefit for a child. There is no limit to how many children you can claim for.', 
    'There are 2 child benefit rates. £24. per week for the eldest child or an only child, and £15.90 for each additional child, paid every 4-weeks.');

-- Housing Benefit data
insert into benefits(benefit_name, how, what) 
values 
    ('housing-benefit', 
    'Housing Benefit can help you pay your rent if you are unemployed, on a low income or claiming benefits. It is being replaced by Universal Credit. You can only make a new claim for Housing Benefit if either of the following apply; you have reached State Pension age or you are in supported, sheltered or temporary housing.', 
    'You may get help with all or part of your rent. There is no set amount of Housing Benefit and what you get will depend on whether you rent privately or from a council.');

-- ESA Benefit data
insert into benefits(benefit_name, how, what) 
values 
    ('employment-support-allowance', 
    'You can apply for Employment and Support Allowance (ESA) if you have a disability or health condition that affects how much you can work. ESA gives you; money to help with living costs if you are unable to work or support to get back into work if you are able to. You can apply if you are employed, self-employed or unemployed.', 
    'How much you get will depend on what stage your application is at, as well as things like your age and whether you are able to get back into work. If you get new style ESA you will earn Class 1 National Insurance credits, which can help towards your State Pension and some benefits in the future.');

-- JSA Benefit data
insert into benefits(benefit_name, how, what) 
values 
    ('jobseekers-allowance', 
    'You can apply for New Style Jobseekers Allowance (JSA) to help you when you are looking for work. You cannot apply for income-based JSA any more. If you are currently getting income-based JSA, you will keep getting payments while you are eligible until your claim ends.', 
    'When you apply to claim JSA, your work coach will make an agreement with you to look for work. This agreement is called a Claimant Commitment. Your Claimant Commitment could include; what you need to do to look for work. You can search and apply for work using the Find a job service.');

-- Universal Credit
insert into benefits(benefit_name, how, what) 
values 
    ('universal-credit', 
    'Universal Credit is a payment to help with your living costs. It is paid monthly - or twice a month for some people in Scotland. You may be able to get it if you are on a low income, out of work or you cannot work.', 
    'How much Universal Credit you get depends on; your standard allowance any extra amounts that apply to you and any money taken off your payment. Universal Credit is paid monthly and is based on your circumstances each month. This is called your assessment period and it starts the day you make your claim.');

create table form
(id int not null auto_increment primary key,
salary varchar(200),
other varchar(200),
food_drink varchar(200),
housing varchar(200),
energy varchar(200),
petrol varchar(200),
train varchar(200),
bus varchar(200),
eating varchar(200),
holidays varchar(200),
clothes varchar(200));

insert into debt(debt_total_figure, debt_source)
values
	(10000, 'Personal Loan', 5, 5, 'years'),
    (5000, 'Personal Loan', 5, 5, 'years'),
    (3000, 'Personal Loan', 5, 5, 'years'),
    (50000, 'Mortgage', 2, 25, 'years'),
    (100000, 'Mortgage', 12, 50, 'years'),
    (75000, 'Mortgage', 6, 10, 'years'),
    (10000, 'Car Loan', 14, 5, 'months'),
    (25000, 'Car Loan', 6, 2, 'years'),
    (75000, 'Car Loan', 4, 5, 'years'),
    (400, 'Credit Card', 14, 2, 'months'),
    (750, 'Credit Card', 15, 10, 'months'); 
     