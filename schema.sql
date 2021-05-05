DROP TABLE IF EXISTS people;

CREATE TABLE people (
  id INT NOT NULL PRIMARY KEY,
  name varchar(255) NOT NULL,
  teacher varchat(255) NOT NULL
);

INSERT INTO people (id, name, teacher) VALUES (1, "Beth", "True"), (2, "Aaron", "False"), (3, "Adil", "False"), (4, "Roselyn", "False")