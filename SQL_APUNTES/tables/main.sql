 --1 create

create table persons(
		id int,
        name varchar(100),
        edad int,
        email varchar(50),
        created date
)

create table persons2(
		id int not null ,
        name varchar(100) not null,
        edad int,
        email varchar(50),
        created date

)

create table persons4(
		id int not null ,
        name varchar(100) not null,
        edad int,
        email varchar(50),
        created datetime,
        unique(id),
        primary key(id)
)

create table persons5(
		id int not null ,
        name varchar(100) not null,
        edad int,
        email varchar(50),
        created datetime,
        unique(id),
        primary key(id),
        check(edad>=18)
)

create table persons6(
		id int not null ,
        name varchar(100) not null,
        edad int,
        email varchar(50),
        created datetime default current_timestamp(),
        unique(id),
        primary key(id),
        check(edad>=18)
)

-- 02 drop table
drop table persons8

-- 03 alter

alter table persons8
add surname varchar(150);


