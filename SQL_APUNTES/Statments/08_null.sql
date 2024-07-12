SELECT  * FROM  users where age is null  

SELECT  * FROM  users where email is not null  and age=13

SELECT name,surname,  ifnull(age,0) as age from users

