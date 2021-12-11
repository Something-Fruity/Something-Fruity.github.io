-- Allows tables to be created in any order withough dependencies being enforced
SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS persona;

-- Create tables
CREATE TABLE account (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR (20) UNIQUE NOT NULL,
    hash VARCHAR(100) NOT NULL,
    f_name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL
);


CREATE TABLE player(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    account_id INTEGER NOT NULL,
    name VARCHAR(30) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(id)
);


CREATE TABLE history(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,  
    player_id INTEGER NOT NULL,
    persona_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    level INTEGER NOT NULL, 
    datetime DATE NOT NULL,
    FOREIGN KEY (player_id) REFERENCES player(id),
    FOREIGN KEY (persona_id) REFERENCES persona(id)
);


CREATE TABLE persona (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR (20) UNIQUE NOT NULL,
  image VARCHAR(30) NOT NULL
);


-- Insert sample data
INSERT INTO `account` VALUES (1,'WhiteFamily','123456','Walter','White','heisenberg@hotmail.com');

INSERT INTO `player` VALUES (1, 1,'Skylar'), (2, 1,'Pinkman');

INSERT INTO `history` VALUES (1, 1, 1, 15005, 7, '2021-01-01'), (2, 1, 2, 11105, 5, '2021-05-01'), (3, 2, 1, 15805, 7, '2021-25-01'), (4, 2, 2, 19905, 9, '2021-03-01');

INSERT INTO `persona` VALUES (1, 'Simba', 'lion'), (2, 'Dumbo', 'elephant'), (3, 'Tom', 'cat'');