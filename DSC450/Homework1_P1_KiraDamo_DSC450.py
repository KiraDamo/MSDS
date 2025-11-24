#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 11:37:49 2025

@author: kiradamo
"""

#Part 1A
    
def file_average(fname):
    '''The function accepts a file name and reads the lines.
    The numbers in the list are then added together and divided by the
    length of the list. Function then returns average.'''
    file = open(fname, 'r')
    num_list = file.readlines()
    
    total = 0
    for number in num_list:
        total = total + float(number) #converts string to float
    file.close()
    
    avg = total / len(num_list)
    
    return avg


#Part 1B

def num_per_line(fname):
    '''This function accepts a file name, reads and splits the lines
    and intiates writing to a new file. The values are split by commas
    and written with a new line at the end. Output file is then closed.'''
    file = open(fname, 'r')
    num_lines = file.read().splitlines() #removes extra line between rows
    file.close()
    outfile = open('hw1_p1_b_output.txt', 'w')
    
    for line in num_lines:
        numbers = line.split(",") #splits by commas
        for value in numbers:
            outfile.write(value+'\n') #begins new line afer each value.
    file.close()
   
#Part 1C

def generateInsert(table, list_values):
    '''The function accepts tables and a list. The string is formatted to
    take the name of the table and the combined list as a string and output
    a SQL query.'''
    list_values = ",".join(list_values) #combines list into one string with commas
    query = f"INSERT INTO {table} VALUES ({list_values});" #list enclosed in parentheses
    return query