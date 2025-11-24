#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 4

@author: kiradamo
"""

fd = open('/Users/kiradamo/Documents/DSC 450/animal.txt', 'r')
lines = fd.readlines()

print('Animals related to bear: ')
for line in lines:
    if line == '':
        break
    AID, ANAME, ACATEGORY, TIMETOFEED = line.split(',')
    if 'bear' in ANAME:
        print(ANAME, ACATEGORY, end='\n')
fd.seek(0)

print('Animals that are not related to tiger and are common: ')
for line in lines:
    if line == '':
        break
    AID, ANAME, ACATEGORY, TIMETOFEED = line.split(',')
    if 'tiger' not in ANAME and 'common' in ACATEGORY:
        print(ANAME, ACATEGORY, end='\n')
fd.seek(0)


#part 2
import sqlite3

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

cursor.execute('DROP TABLE Employee')

CT_EMPLOYEE = '''CREATE TABLE Employee (
First VARCHAR(25),
Last VARCHAR(25),
Address VARCHAR(100),
PRIMARY KEY (First, Last)
);''' 
    
cursor.execute(CT_EMPLOYEE)

cursor.execute('DROP TABLE JobInfo')   
CT_JOB = '''CREATE TABLE JobInfo (
Job VARCHAR(25),
Salary NUMBER(10),
ASSISTANT VARCHAR(25),
PRIMARY KEY (Job)
);'''

cursor.execute(CT_JOB)

    
with open('/Users/kiradamo/Documents/DSC 450/data_module4_part2.txt') as file:
    lines = [line.strip().split(', ') for line in file]
    for line in lines:
        (First, Last, Address, Job, Salary, Assistant) = line
        Salary = int(Salary) if Salary != 'NULL' else None
        cursor.execute('INSERT OR IGNORE INTO Employee VALUES (?, ?, ?);', (First, Last, Address))
        cursor.execute('INSERT OR IGNORE INTO JobInfo VALUES (?, ?, ?);', (Job, Salary, Assistant))

results_Employee = cursor.execute('SELECT * FROM Employee;')
results_Employee.fetchall()
results_JobInfo = cursor.execute('SELECT * FROM JobInfo;')
results_JobInfo.fetchall()



D_Query = '''SELECT * FROM JobInfo WHERE Salary is NULL'''
partD = cursor.execute(D_Query)
partD.fetchall()