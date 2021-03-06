-- Allows tables to be created in any order without dependencies being enforced
CREATE DATABASE IF NOT EXISTS sth_fruity;
use sth_fruity;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS persona;

-- Create tables
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR (20) UNIQUE NOT NULL,
    hash VARCHAR(500) NOT NULL,
    f_name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    last_login DATETIME,
    language VARCHAR(3)
);


CREATE TABLE player(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    name VARCHAR(30) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);


CREATE TABLE game(
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
  image VARCHAR(30) NOT NULL,
  created_by INTEGER NOT NULL,
  FOREIGN KEY (created_by) REFERENCES player(id)
);


-- Insert sample data
INSERT INTO `user` VALUES (1,'WhiteFamily','pbkdf2:sha256:260000$jVVzEctPpRhOWilC$c6bfc6097150f09f34f51d64cad272c812fb828b50fea38f0a00dca656fb384b','Walter','White','heisenberg@hotmail.com', '2021-09-09', 'en'),
                             (2,'SimpsonFamily','pbkdf2:sha256:260000$M3WYwna0COf6CWoK$6194a11836ac29c5b745bbe035fcc06eec13259c50fc3189769f60465e2aa80e','Homer','Simpson','homer@donuts.com', '2021-12-12', 'fr');

INSERT INTO `player` VALUES (1, 1,'Skylar'), (2, 1,'Pinkman'), (3, 2, 'Bart'), (4, 2, 'Lisa');

INSERT INTO `game` VALUES (1, 1, 1, 15005, 7, '2021-01-01'), (2, 1, 2, 11105, 5, '2021-05-01'), (3, 2, 1, 15805, 7, '2021-01-21'), (4, 2, 2, 19905, 9, '2021-03-01');

INSERT INTO `persona` VALUES (1, 'Simba', 'lion', 1), (2, 'Dumbo', 'elephant', 2), (3, 'Tom', 'cat', 3);
