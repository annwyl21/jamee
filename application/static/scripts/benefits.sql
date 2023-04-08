-- Using a database as a content management system
-- url endpoints are in the name field and attach to this base url https://www.gov.uk/

-- CREATE DATABASE budget_management;
use budget_management;
-- drop database budget_management;

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

