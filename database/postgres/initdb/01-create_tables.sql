CREATE TABLE artifacts(
  id int NOT NULL,
  name varchar(50),
  price int,
  PRIMARY KEY (id)
);

CREATE TABLE customers(
  id int NOT NULL PRIMARY KEY,
  name varchar(50),
  address varchar(255),
  phone varchar(20)
);
