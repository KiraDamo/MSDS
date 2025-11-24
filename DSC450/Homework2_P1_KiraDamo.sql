CREATE TABLE Writes(
    Author INT,
    Book INT,
    AuthorRank INT,
    
    CONSTRAINT Writes_FK
        FOREIGN KEY(Author)
        REFERENCES Authors(AuthorID),
        FOREIGN KEY(Book)
        REFERENCES Books(ISBN)
);

CREATE TABLE Books(
    ISBN INT,
    Title VARCHAR(225),
    Publisher VARCHAR(25),
    
    CONSTRAINT Books_PK
        PRIMARY KEY(ISBN),
    
    CONSTRAINT Books_FK
        FOREIGN KEY(Publisher)
        REFERENCES Publishers(PublisherName)
);

CREATE TABLE Publishers(
    PublisherName VARCHAR(25),
    PubNumber NUMBER(*, 0),
    Address VARCHAR(225),
    
    CONSTRAINT Publishers_PK
        PRIMARY KEY(PubNumber),
    
    CONSTRAINT Publishers_FK
        FOREIGN KEY(PubNumber)
        REFERENCES Books(ISBN)
);

CREATE TABLE Authors(
    LastName VARCHAR(25),
    FirstName VARCHAR(25),
    AuthorID Number(*, 0) PRIMARY KEY,
    Birthdate DATE
);


INSERT INTO Authors VALUES('CORMEN', 'THOMAS H', 15, '15-OCT-1956');
INSERT INTO Authors VALUES('Leiserson', 'CHARLES E', 14,'14-JUL-1957');
INSERT INTO Authors VALUES('Rivest', 'Ronald L', 28, '28-MAR-1958');
INSERT INTO Authors VALUES('Stein', 'Clifford', 97, '08-JUL-1959');
INSERT INTO Authors VALUES('Sakurai', 'JJ', 46, '01-JAN-1933');
INSERT INTO Authors VALUES('Napolitano', 'JIM', 23,  '02-FEB-1935');

INSERT INTO Publishers VALUES('The MIT Press', '9780262033848', '255 Main Street,
NE18. Floor 9. Cambridge, MA 02142');
INSERT INTO Publishers VALUES('CambridgeUniversity Press', '9781108473224', 'University Printing House,
Shaftesbury Road,Cambridge, United Kingdom');

INSERT INTO Books VALUES(9780262033848,'Introduction to Algorithms Third Edition
', 'The MIT Press');
INSERT INTO Books VALUES(9781108473224, 'Modern Quantum Mechanics Third Edition',
'CambridgeUniversity Press');

INSERT INTO Writes VALUES('15', 9780262033848, 1);
INSERT INTO Writes VALUES('14', 9780262033848, 2);
INSERT INTO Writes VALUES('28', 9780262033848, 3);
INSERT INTO Writes VALUES('97', 9780262033848, 4);
INSERT INTO Writes VALUES('46', 9781108473224, 1);
INSERT INTO Writes VALUES('23', 9781108473224, 2);


INSERT INTO Authors VALUES('King', 'Stephen', 2, '09-SEP-1947');
INSERT INTO Authors VALUES('Asimov', 'Isaac', 4, '02-JAN-1921');
INSERT INTO Authors VALUES('Verne', 'Jules', 7, '08-FEB-1828');
INSERT INTO Authors VALUES('Shelley', 'Mary', 37, '08-AUG-1797');

INSERT INTO Publishers VALUES('Bloomsbury Publishing', 17, 'London Borough of Camden');
INSERT INTO Publishers VALUES('Arthur A Levine Books', 18, 'New York City');

INSERT INTO Books VALUES(1111111, 'Databases from Outer Space', 17);
INSERT INTO Books VALUES(2223233, 'Revenge of the SQL', 17);
INSERT INTO Books VALUES(3333323, 'The Night of the Living Databases', 18);

INSERT INTO Writes VALUES(2, 1111111, 1);
INSERT INTO Writes VALUES(4, 1111111, 2);
INSERT INTO Writes VALUES(4, 2223233, 1);
INSERT INTO Writes VALUES(7, 2223233, 2);
INSERT INTO Writes VALUES(37, 3333323, 1);
INSERT INTO Writes VALUES(2, 3333323, 2);

CREATE TABLE Department(
    DeptName VARCHAR(25) PRIMARY KEY,
    Chair VARCHAR(25),
    College VARCHAR(25)
);

CREATE TABLE Advisors(
    AdvisorsID INT PRIMARY KEY,
    AdvisorName VARCHAR(50),
    Address VARCHAR(225),
    ResearchArea VARCHAR(25),
    Department VARCHAR(25),
    
    CONSTRAINT Advisors_FK
        FOREIGN KEY(Department)
        REFERENCES Department(DeptName)
);


CREATE TABLE Students(
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(25),
    LastName VARCHAR(25),
    AdvisorRef INT,
    
    CONSTRAINT Students_FK
        FOREIGN KEY(AdvisorRef)
        REFERENCES Advisors(AdvisorsID)
);

SELECT * FROM Department;
SELECT * FROM Students;
SELECT * FROM Advisors;

SELECT * FROM Books;
SELECT * FROM Authors;
SELECT * FROM Publishers;
SELECT * FROM Writes;

