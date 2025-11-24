DROP TABLE Animal;
-- ACategory: Animal category 'common', 'rare', 'exotic'.  May be NULL
-- TimeToFeed: Time it takes to feed the animal (hours)
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(35) NOT NULL,
  ACategory VARCHAR2(19),
  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);
INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);
INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.75);
INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);
INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.5);
INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.75);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.75);

SELECT * FROM Animal WHERE TimeToFeed < 1.9;

SELECT * FROM Animal WHERE ACategory = 'rare' OR ACategory = 'exotic';

SELECT * FROM Animal WHERE ACategory is NULL;

SELECT * FROM Animal WHERE TimeToFeed > 1.6 AND TimeToFeed < 2.7;

SELECT MIN(TimeToFeed) as MinTimeToFeed, MAX(TimeToFeed) as MaxTimeToFeed
FROM Animal;

SELECT AVG(TimeToFeed) as avgTimeToFeed FROM Animal;

SELECT COUNT(*) as numNull FROM Animal WHERE ACategory is NULL;

SELECT * FROM Animal
WHERE AName = 'Alpaca' OR AName = 'Llama' OR ACategory != 'exotic';