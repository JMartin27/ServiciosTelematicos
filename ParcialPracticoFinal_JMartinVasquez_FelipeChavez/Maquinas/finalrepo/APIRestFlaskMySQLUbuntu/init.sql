
CREATE DATABASE myflaskapp;
use myflaskapp;

CREATE TABLE books (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(255),
    description varchar(255),
    author varchar(255)
);


INSERT INTO books VALUES(null, "La hojarasca", "Interesante", "Gabo"),
    (null, "El principito", "Brillante", "Antoine de Saint");
