DROP TABLE IF EXISTS people;

CREATE TABLE people (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name varchar(255) NOT NULL,
  teacher varchat(255) NOT NULL
);

INSERT INTO people (name, teacher) VALUES ("Beth", "True"), ("Aaron", "False"), ("Adil", "False"), ( "Roselyn", "False")