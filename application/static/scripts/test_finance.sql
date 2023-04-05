-- run these 1 at a time not as a whole, you may not need to run all of them

create database test_finance;

drop database test_finance;

use test_finance;

create table test1
(test_id int not null auto_increment primary key,
test_data varchar (25));

insert into test1(test_data) values ('some data');
insert into test1(test_data) values ('some more data');

select * from test1;

select test_data from test1 where test_id=1;
select test_data from test1;

drop procedure data_out;

DELIMITER //
create procedure data_out()
begin
select test_data from test1 where test_id=1;
end //

DELIMITER //
create procedure data_out_list()
begin
select test_data from test1;
end //

DELIMITER //
CREATE PROCEDURE add_data(in td varchar(25))
begin
insert into test_data
values(td);
end //
