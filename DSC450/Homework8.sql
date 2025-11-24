DROP TABLE STUDENT CASCADE CONSTRAINTS;
CREATE TABLE STUDENT(
	ID		CHAR(3),
	Name		VARCHAR2(20),
	Midterm	NUMBER(3,0) 	CHECK (Midterm>=0 AND Midterm<=100),
	Final		NUMBER(3,0)	CHECK (Final>=0 AND Final<=100),
	Homework	NUMBER(3,0)	CHECK (Homework>=0 AND Homework<=100),
	PRIMARY KEY (ID)
);
INSERT INTO STUDENT VALUES ( '445', 'Seinfeld', 86, 90, 99 );
INSERT INTO STUDENT VALUES ( '909', 'Costanza', 74, 72, 86 );
INSERT INTO STUDENT VALUES ( '123', 'Benes', 93, 89, 91 );
INSERT INTO STUDENT VALUES ( '111', 'Kramer', 99, 91, 93 );
INSERT INTO STUDENT VALUES ( '667', 'Newman', 78, 82, 84 );
INSERT INTO STUDENT VALUES ( '889', 'Banya', 51, 66, 50 );
SELECT * FROM STUDENT;

DROP TABLE WEIGHTS CASCADE CONSTRAINTS;
CREATE TABLE WEIGHTS(
	MidPct	NUMBER(2,0) CHECK (MidPct>=0 AND MidPct<=100),
	FinPct	NUMBER(2,0) CHECK (FinPct>=0 AND FinPct<=100),
	HWPct	NUMBER(2,0) CHECK (HWPct>=0 AND HWPct<=100)
);
INSERT INTO WEIGHTS VALUES ( 30, 30, 40 );
SELECT * FROM WEIGHTS;
COMMIT;

DECLARE
    x FLOAT;
    y FLOAT;
    z FLOAT;
    sum_score NUMBER(5,1);
    grade CHAR(1);
BEGIN
    SELECT MidPct, FinPct, HwPct INTO x,y,z FROM WEIGHTS;
    DBMS_OUTPUT.PUT_LINE('Weights are ' || x || ', ' || y || ', ' || z);
    
    DBMS_OUTPUT.PUT_LINE('Student Records are: ');
    FOR student_record IN (SELECT ID, Name, Midterm, Final, Homework FROM STUDENT)
LOOP
    sum_score := (student_record.Midterm * x + student_record.Final * y +
    student_record.Homework * z) / 100;
    IF sum_score >= 90 THEN 
        grade := 'A';
    ELSIF sum_score >= 80 AND sum_score < 90 THEN
        grade := 'B';
    ELSIF sum_score >= 65 AND sum_score < 80 THEN
        grade := 'C';
    ELSE
        grade := 'F';
    END IF;
    DBMS_OUTPUT.PUT_LINE(student_record.ID || ', ' || student_record.Name || ', ' ||
    sum_score || ', ' || grade);
END LOOP;
END;
/

DROP TABLE ENROLLMENT CASCADE CONSTRAINTS;
DROP TABLE SECTION CASCADE CONSTRAINTS;

CREATE TABLE SECTION(
 SectionID 	CHAR(5),
 Course	VARCHAR2(8),
 Students	NUMBER DEFAULT 0,
 CONSTRAINT PK_SECTION 
		PRIMARY KEY (SectionID)
);

CREATE TABLE ENROLLMENT(
 SectionID	CHAR(5),
 StudentID	CHAR(7),
 CONSTRAINT PK_ENROLLMENT 
		PRIMARY KEY (SectionID, StudentID),
 CONSTRAINT FK_ENROLLMENT_SECTION 
		FOREIGN KEY (SectionID)
		REFERENCES SECTION (SectionID)
);
 
INSERT INTO SECTION (SectionID, Course) VALUES ( '12345', 'CSC 355' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '22109', 'CSC 309' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '99113', 'CSC 300' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '99114', 'CSC 300' );
COMMIT;
SELECT * FROM SECTION;

CREATE OR REPLACE TRIGGER section_capacity
BEFORE INSERT ON ENROLLMENT
FOR EACH ROW
    DECLARE
        num_students NUMBER;
    BEGIN
        SELECT STUDENTS INTO num_students FROM SECTION
        WHERE SectionID = :NEW.SectionID;

        IF num_students < 5 THEN
            UPDATE SECTION SET Students = Students + 1
            WHERE SectionID = :NEW.SectionID;
        ELSE
            raise_application_error(-20102, '[Unable to enroll. Class is at full capacity.]');
        END IF;
    END;
/

SELECT * FROM ENROLLMENT;

INSERT INTO ENROLLMENT VALUES ('12345','1234567');
INSERT INTO ENROLLMENT VALUES ('12345','7654321');
INSERT INTO ENROLLMENT VALUES ('12345','1357246');
INSERT INTO ENROLLMENT VALUES ('12345','3456789');
INSERT INTO ENROLLMENT VALUES ('12345','9876543');
INSERT INTO ENROLLMENT VALUES ('12345','3579468');

CREATE OR REPLACE TRIGGER student_removal
AFTER DELETE ON ENROLLMENT
FOR EACH ROW
BEGIN
    UPDATE SECTION SET Students = Students - 1
    WHERE SectionID = :old.SectionID;
END;
/

SELECT * FROM ENROLLMENT;
DELETE FROM ENROLLMENT WHERE StudentID = '3456789';
SELECT * FROM ENROLLMENT;
SELECT * FROM SECTION;