#Table creation that was provided.
createtbl = """
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),

  TimeToFeed NUMBER(4,2),

  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);
"""

inserts = ["INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);", "INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);", "INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);", "INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);", "INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);", "INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);", "INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);", "INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);", "INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.5);", "INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);", "INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);"]

import sqlite3

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

cursor.execute(createtbl)   # create the Animal table
for ins in inserts:         # insert the rows
    cursor.execute(ins)

conn.commit()   # finalize inserted data
conn.close()    # close the connection

#Part 2A
'''This part selects all the rows that were populated in the SQL database
and writes into a txt file the column names and then formats each column'''

allrows = conn.execute('SELECT * FROM Animal')
rows = allrows.fetchall()

with open('animal.txt', 'w') as file:
     file.write('AID, AName, ACategory, TimeToFeed\n')
     #for consistency, all variables are the same as db
     for row in rows:
         file.write('%d, %s, %s, %.2f\n' % tuple(row))
         #formats tuple and rounds to nearest hundreth decimal place
file.close()

conn = sqlite3.connect('dsc450.db')

conn.execute('DROP TABLE Animal')
conn.execute(createtbl)

#Part 2B
'''This part reads the txt file and saves all lines in the txt file as
a sublist. the executemany function then runs the insert queries for 
all rows in the txt file. Using the COUNT query in SQL, the number of rows
is calculated and returned in a print statement.'''
fd = open('animal.txt', 'r')
rows = fd.readlines()
#reads all lines in txt file
animal_data = [row.split(',') for row in rows][1:]
#splits rows by comma and neglects header.
#also creates each row into a list that is inside a big list
    
cursor = conn.cursor()
cursor.executemany('INSERT INTO Animal VALUES (?, ?, ?, ?);', animal_data)
#executes queries with each row of the list
result = conn.execute('SELECT COUNT(*) FROM Animal')
#sql query to count number of rows in Animal table
result.fetchall()
#prints final count of rows
cursor.close()
file.close()
#closes file and cursor





