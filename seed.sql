CREATE TABLE humans (
    human_id SERIAL PRIMARY KEY,
    fname VARCHAR(25) NOT NULL,
    lname VARCHAR(25) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE animals (
    animal_id SERIAL PRIMARY KEY,
    human_id INTEGER REFERENCES humans(human_id) NOT NULL,
    name VARCHAR(50) NOT NULL,
    animal_species VARCHAR(25) NOT NULL,
    birth_year INTEGER
);

INSERT INTO humans (fname, lname, email)
VALUES ('Marne', 'Jobes', 'mjobes0@gmail.com'),
('Margarette', 'Liset', 'mliset1@devmountain.com'),
('Errick', 'de Broke', 'edebroke2@gmail.com'),
('Kippy', 'Goodall', 'kgoodall3@dev.com'),
('Frank', 'Paris', 'fparis4@gmail.com');

INSERT INTO animals (human_id, name, animal_species, birth_year)
VALUES (1,	'Fluffy', 'cat', 2010),
(2,	'Squiggles', 'snake', 2016),
(3,	'Fido', 'dog', 2015),
(2,	'Birdy', 'bird', 2017),
(5,	'Buster', 'dog', 2011),
(5,	'Bugs', 'rabbit', 2016),
(5,	'Twinkie', 'dog', 2014),
(4,	'Fluffster', 'dog', 2013),
(1,	'Twinkles', 'cat', 2014);

INSERT INTO animals (human_id, name, animal_species)
VALUES (4,	'Bubbles', 'fish'),
(2,	'Mr. Hops', 'rabbit'),
(1,	'Cuddles', 'cat');