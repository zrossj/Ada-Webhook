-- this script is optional as its already setup for be executed within the python API for postgres.

drop table customer_mail;
create table customer_mail  (	
	name varchar(64), 
	mail_address varchar(64)
);

drop table fx_price_collected;
create table fx_price_collected (
	coin char(6),	
	date timestamp,
	code char(3),
	codein char(3),
	name varchar(64),
	high decimal,	
	low decimal,
	"varBid" decimal,
	"pctChange" decimal,
	bid decimal, 
	ask decimal
);
