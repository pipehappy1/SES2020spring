

We use flask in this example, install flask

    conda install -y  flask
	

Use the following to run mysql server, with port exposed on localhost.

	docker run -p 3306:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=12345 -d mysql:latest

Use the following to connect to the server, even -P option is not used when creating the server. The network id and ip address is found by docker inspect my-mysql | grep NetworkID and docker inspect my-mysql | grep IPAddress

    docker run -it --network 705c5b79742039fadf4e2547b26128e01845949b207285edd0b2afe23a8d98cc --rm mysql mysql -h172.17.0.2 -uroot -p12345

use the following to set up power user

    CREATE USER 'yguan' IDENTIFIED BY '123456';
	GRANT ALL PRIVILEGES ON * . * TO 'yguan';
	FLUSH PRIVILEGES;
	
After this step, now the account yguan can be accessed anywhere by the following, note: username and password are both needed

    mysql -h 127.0.0.1  -uyguan -p123456

use the following to setup the database

    create database test;
	use test;
	
use the following to setup tables;

	create table location (
	   id INT NOT NULL AUTO_INCREMENT,
       name varchar(40) NOT NULL,
	   qrid varchar(40) NOT NULL,
       description varchar(200) NOT NULL,
       PRIMARY KEY ( id ),
	   INDEX (qrid, name)
    );

