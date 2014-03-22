CREATE DATABASE newworldhoge DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
grant all on newworldhoge.* to username@localhost identified by 'password';
use newworldhoge
create table words(
  wordname varchar(255),
  part varchar(10)
) default charset=utf8;
