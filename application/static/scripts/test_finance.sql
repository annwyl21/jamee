-- run these 1 at a time not as a whole, you may not need to run all of them

create database test_finance;

use test_finance;

create table test1
(test_id int not null auto_increment primary key,
test_data varchar (15));

insert into test1(test_data) values ('some data');

select * from test1;

select test_data from test1 where test_id=1;

drop procedure data_out;

DELIMITER //
create procedure data_out()
begin
select test_data from test1 where test_id=1;
end //
