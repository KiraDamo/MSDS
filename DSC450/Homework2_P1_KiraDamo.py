#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 2 Part 1 Question 4
@author: kiradamo
"""

def validateInsert(query):
    '''This function accepts a string and checks that the string starts with
    INSERT INTO and ends with a semi-colon. If condition is met, table and values
    are distinguished by indexing of the string and reprinted in confirmation statement.
    otherwise invalid statement is printed.'''
    if query.startswith("INSERT INTO ") and query.endswith(';'):
        #initial condition that MUST be met
        table = query[query.index('INTO ') + 5:query.index(' VALUES')]
        #^indexing of table name.
        #Detecting index instead of setting boundaries of indexes since table
        #name can vary in length
        values = query[query.index('('):query.index(')') + 1]
        #same structure for table name for finding values
        print(f"Inserting {values} into {table} table")
        #reprinting statement with according variables
    else:
        print('Invalid Statement')
        #error message if string requirements are not met
            