use hotelms;

create table hotel(
hotel_id int not null auto_increment primary key,
user_name varchar(100) not null,
members varchar(100),
phone_number char(10) not null,
is_having_room char(5),
room_number char(2));
