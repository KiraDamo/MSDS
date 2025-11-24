#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 5
Due October 15th

@author: kiradamo
"""
#Part 1
import sqlite3
import csv

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

#cursor.execute('DROP TABLE Chauffers')
#drop table in case already exists

crttbl = '''CREATE TABLE Chauffers (
License_Number NUMBER(6),
    Renewed DATE,
    Status VARCHAR(25),
    Status_Date DATE,
    Driver_Type VARCHAR(25),
    License_Type VARCHAR(25),
    Original_Issue_Date DATE,
    Name VARCHAR(50),
    Sex VARCHAR(5),
    Chauffeur_City VARCHAR(50),
    Chaffeur_State VARCHAR(50),
    Record_Number VARCHAR(20) NOT NULL UNIQUE,
    
    CONSTRAINT Record_PK
        Primary Key(Record_Number)    
);'''

cursor.execute(crttbl) #creates table

insert = 'INSERT OR IGNORE INTO Chauffers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'

fd = open('/Users/kiradamo/Documents/DSC 450/Public_Chauffeurs_Short_hw3.csv', 'r')
reader = csv.reader(fd)
next(reader)
for row in reader:
    cursor.execute(insert, row)

fd.close()

results = cursor.execute('SELECT * FROM Chauffers LIMIT 10;')
results.fetchall()

conn.commit()
conn.close()


#Part 3
import sqlite3
import json

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

fd_tweets = open('/Users/kiradamo/Documents/DSC 450/Module5.txt', 'r', encoding='utf8')
ln = fd_tweets.readline().split('EndOfTweet')

insert_tweets = '''INSERT OR IGNORE INTO Tweets VALUES (?,?,?,?,?,?,?,?,?)'''

tweet_tbl = '''CREATE TABLE Tweets (
    created_at DATE,
    id_str INT(50),
    text VARCHAR(280),
    source VARCHAR(100),
    in_reply_to_user_id VARCHAR(50),
    in_reply_to_screen_name VARCHAR(50),
    in_reply_to_status_id varchar(50),
    retweet_count INT(10),
    contributors VARCHAR(50),
    
    CONSTRAINT Tweet_PK
        Primary Key(id_str)
);'''
    
#cursor.execute('DROP TABLE Tweets')
#drop table if already exists
cursor.execute(tweet_tbl)

allData = []
#creates empty list and for each key/index in the tweet, the designated value
#will be added to the list
for tweet in ln:
    tw_load = json.loads(tweet)
    allData.append((tw_load['created_at'],
                 tw_load['id_str'], tw_load['text'],
                 tw_load['source'], tw_load['in_reply_to_user_id'],
                 tw_load['in_reply_to_screen_name'], tw_load['in_reply_to_status_id'],
                 tw_load['retweet_count'], tw_load['contributors']))
 
cursor.executemany(insert_tweets, allData)
#inserts all data compiled from list

results = cursor.execute('SELECT * FROM Tweets LIMIT 10;')
results.fetchall()
#shows sample of 10 values

conn.commit()
conn.close()