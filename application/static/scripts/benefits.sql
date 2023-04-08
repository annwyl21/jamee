Create Database benefits;

Use benefits;

drop database benefits;

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
ALTER TABLE budget_account
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

Create table employment_support_allowance
(esa_id int not null auto_increment primary key,
firstname varchar(50),
lastname varchar(50),
age INT,
weekly_esa decimal ,
monthly_esa decimal,
annual_esa decimal)
;

Create table job_seeker_allowance
(jsa_id int not null auto_increment primary key,
firstname varchar(50),
lastname varchar(50),
age INT,
weekly_jsa decimal ,
monthly_jsa decimal,
annual_jsa decimal)
;

Create table child_tax_credit
(cta_id int not null auto_increment primary key,
firstname varchar(50),
lastname varchar(50),
age INT,
weekly_eta decimal ,
monthly_eta decimal,
annual_eta decimal)
;

Create table housing_benefit
(hb_id int not null auto_increment primary key,
firstname varchar(50),
lastname varchar(50),
age INT,
weekly_hb decimal ,
monthly_hb decimal,
annual_hb decimal)
;

CREATE TABLE budget_user
(user_id int not null auto_increment primary key,
username varchar(50),
user_password varchar(50),
title varchar(10),
first_name varchar(50),
last_name varchar(50)
);

ALTER TABLE employment_support_allowance
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE job_seeker_allowance
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE child_tax_credit
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);



CREATE TABLE income
(income_id int not null auto_increment primary key,
income_source varchar(50),
income_date varchar(50),
income_total decimal
);

ALTER TABLE employment_support_allowance
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE job_seeker_allowance
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE child_tax_credit
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);

ALTER TABLE housing_benefit
ADD COLUMN income_id int,
ADD foreign key(income_id) references income(income_id);




CREATE TABLE expense
(expense_id int not null auto_increment primary key,
expense_source varchar(50),
expense_date varchar(50),
expense_total decimal
);

ALTER TABLE employment_support_allowance
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);

ALTER TABLE job_seeker_allowance
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);

ALTER TABLE child_tax_credit
ADD COLUMN expense_id int,
ADD foreign key(expense_id) references expense(expense_id);




ALTER TABLE employment_support_allowance
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE job_seeker_allowance
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE child_tax_credit
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);

ALTER TABLE housing_benefit
ADD COLUMN user_id int,
ADD foreign key(user_id) references budget_user(user_id);


-- CREATE TABLE category
-- -- To look at types of incoming and outgoing money e.g. food, holidays, bills etc 
-- (category_id int not null auto_increment primary key,
-- category_name varchar(50)
-- );
-- Adding foreign keys to 'category' table 
-- ALTER TABLE category
-- ADD COLUMN user_id int,
-- ADD foreign key(user_id) references budget_user(user_id);

-- ALTER TABLE category
-- ADD COLUMN income_id int,
-- ADD foreign key(income_id) references income(income_id);

-- ALTER TABLE category
-- ADD COLUMN expense_id int,
-- ADD foreign key(expense_id) references expense(expense_id);

-- CREATE TABLE weekly_budget
-- (weekly_budget_id int not null auto_increment primary key,
-- weekly_balance decimal
-- );

-- Adding foreign keys to 'weekly_budget' table 
-- ALTER TABLE weekly_budget
-- ADD COLUMN user_id int,
-- ADD foreign key(user_id) references budget_user(user_id);

-- ALTER TABLE weekly_budget
-- ADD COLUMN income_id int,
-- ADD foreign key(income_id) references income(income_id);

-- ALTER TABLE weekly_budget
-- ADD COLUMN expense_id int,
-- ADD foreign key(expense_id) references expense(expense_id);

-- ALTER TABLE weekly_budget
-- ADD COLUMN category_id int,
-- ADD foreign key(category_id) references category(category_id);




-- CREATE TABLE monthly_budget
-- (monthly_budget_id int not null auto_increment primary key,
-- monthly_balance decimal
-- );

-- -- Adding foreign keys to 'monthly_budget' table 
-- ALTER TABLE monthly_budget
-- ADD COLUMN user_id int,
-- ADD foreign key(user_id) references budget_user(user_id);

-- ALTER TABLE monthly_budget
-- ADD COLUMN income_id int,
-- ADD foreign key(income_id) references income(income_id);

-- ALTER TABLE monthly_budget
-- ADD COLUMN expense_id int,
-- ADD foreign key(expense_id) references expense(expense_id);

-- ALTER TABLE monthly_budget
-- ADD COLUMN category_id int,
-- ADD foreign key(category_id) references category(category_id);


-- CREATE TABLE annual_budget
-- (annual_budget_id int not null auto_increment primary key,
-- annual_balance decimal
-- );

-- -- Adding foreign keys to 'weekly_budget' table 
-- ALTER TABLE annual_budget
-- ADD COLUMN user_id int,
-- ADD foreign key(user_id) references budget_user(user_id);

-- ALTER TABLE annual_budget
-- ADD COLUMN income_id int,
-- ADD foreign key(income_id) references income(income_id);

-- ALTER TABLE annual_budget
-- ADD COLUMN expense_id int,
-- ADD foreign key(expense_id) references expense(expense_id);

-- ALTER TABLE annual_budget
-- ADD COLUMN category_id int,
-- ADD foreign key(category_id) references category(category_id);


-- CREATE TABLE custom_budget
-- (custom_budget_id int not null auto_increment primary key,
-- custom_balance decimal
-- );

-- -- Adding foreign keys to 'custom_budget' table 
-- ALTER TABLE custom_budget
-- ADD COLUMN user_id int,
-- ADD foreign key(user_id) references budget_user(user_id);

-- ALTER TABLE custom_budget
-- ADD COLUMN income_id int,
-- ADD foreign key(income_id) references income(income_id);

-- ALTER TABLE custom_budget
-- ADD COLUMN expense_id int,
-- ADD foreign key(expense_id) references expense(expense_id);

-- ALTER TABLE custom_budget
-- ADD COLUMN category_id int,
-- ADD foreign key(category_id) references category(category_id);
