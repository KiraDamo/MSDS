#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Homework 9
Kira Damo
Due November 17th'''

import sqlite3
import json
import urllib.request
import time
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

twitter_data_url = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
webFD = urllib.request.urlopen(twitter_data_url)
tweets = webFD.readlines()

outfile = open('tweet_errors.txt', 'w', encoding='utf-8')

#inserting Geo table into schema

cursor.execute('DROP TABLE IF EXISTS Geo')
geo_tbl = '''CREATE TABLE Geo(
    geo_id TEXT PRIMARY KEY,
    type TEXT,
    longitude TEXT,
    latitude TEXT
);'''

cursor.execute('DROP TABLE IF EXISTS User')
user_tbl = '''CREATE TABLE User(
    id INT PRIMARY KEY,
    name TEXT,
    screen_name TEXT,
    description TEXT,
    friends_count INT
 );'''

cursor.execute('DROP TABLE IF EXISTS Tweet')
tweet_tbl = '''CREATE TABLE Tweet(
    id INT PRIMARY KEY,
    created_at TEXT,
    id_str TEXT,
    text TEXT,
    source TEXT,
    in_reply_to_user_id INT,
    in_reply_to_screen_name TEXT,
    in_reply_to_status_id INT,
    retweet_count INT,
    contributors TEXT,
    geo_id TEXT,
    
    FOREIGN KEY (id_str) REFERENCES User(id)
    FOREIGN KEY (geo_id) REFERENCES Geo(geo_id)
    );'''

cursor.execute(geo_tbl)
cursor.execute(tweet_tbl)
cursor.execute(user_tbl)

tweet_insert = '''INSERT INTO Tweet (created_at, id_str, text, source,
                  in_reply_to_user_id, in_reply_to_screen_name,
                  in_reply_to_status_id, retweet_count, contributors, geo_id)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
user_insert = '''INSERT OR IGNORE INTO User (id, name, screen_name, description,
                friends_count)VALUES (?, ?, ?, ?, ?)'''
geo_insert = geo_insert = '''INSERT INTO Geo (geo_id, type,
                            longitude, latitude) VALUES (?, ?, ?, ?)'''

for tweet in tweets:
    try:
        tdict = json.loads(tweet.decode('utf-8'))
        
        tweet_data = [
            tdict.get('created_at'),
            tdict.get('id_str'),
            tdict.get('text'),
            tdict.get('source'),
            tdict.get('in_reply_to_user_id'),
            tdict.get('in_reply_to_screen_name'),
            tdict.get('in_reply_to_status_id'),
            tdict.get('retweet_count'),
            tdict.get('contributors'),
            tdict.get('geo_id')
            ]
        cursor.execute(tweet_insert, tweet_data)
        
        #if geo data exists, then the following dictionary will be retrieved
        #retrieved geo data will be instered into geo table
        
        if tdict['geo'] != None:
            geo_data = [
                tdict['id'],
                tdict['geo']['type'],
                tdict['geo']['coordinates'][0],
                tdict['geo']['coordinates'][1]]
            cursor.execute(geo_insert, geo_data)
    
        user_data = [
            tdict['user']['id'],
            tdict['user']['name'],
            tdict['user']['screen_name'],
            tdict['user']['description'],
            tdict['user']['friends_count']
            ]
        cursor.execute(user_insert, user_data)

    except ValueError:
        outfile.write(str(tweet))

outfile.close()  

print('Question 1 part A')

#finds id that contains 78, 81, or 87 using SQL query.
#uses time module to report runtime.

user_table_retrieval = cursor.execute('SELECT * FROM User LIMIT 10;').fetchall()
tweet_table_retrieval = cursor.execute('SELECT * FROM Tweet LIMIT 10;').fetchall()   
geo_table_retrieval = cursor.execute('SELECT * FROM Geo LIMIT 10;').fetchall()   

runtime_start_a = time.time()
p1a_results = cursor.execute('''SELECT * FROM Tweet
               WHERE id_str LIKE '%78%' OR '%81%' OR '%87%';''').fetchall()
runtime_end_a = time.time()

print('The runtime for this query was {} seconds'.format(runtime_end_a - runtime_start_a))

cursor.close()
conn.commit()
conn.close() 

print('Question 1 part B')

#uses python to read file and find id that contains 78, 81, or 87.
#uses time module to report runtime.

runtime_start_b = time.time()
twitter_data_url = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
webFD = urllib.request.urlopen(twitter_data_url)
tweets = webFD.readlines()

outfile_2 = open('tweet_errors_b.txt', 'w', encoding='utf-8')

p1b = []
for tweet in tweets:
    try:
        tdict = json.loads(tweet.decode('utf-8'))
        id_str = tdict.get('id_str')
        
        conditions = ['78', '87', '81']
        
        if any(cond in id_str for cond in conditions):
            tweet_data_b = [
                tdict.get('created_at'),
                tdict.get('id_str'),
                tdict.get('text'),
                tdict.get('source'),
                tdict.get('in_reply_to_user_id'),
                tdict.get('in_reply_to_screen_name'),
                tdict.get('in_reply_to_status_id'),
                tdict.get('retweet_count'),
                tdict.get('contributors'),
                tdict.get('geo_id')
                ]
            p1b.append(tweet_data_b)
    except ValueError:
        outfile_2.write(str(tweet))
        
outfile_2.close()
runtime_end_b = time.time()
print('The runtime for this query was {} seconds'.format(runtime_end_b - runtime_start_b))


print('Question 1 part C')

#finds unique friends count using sql query
#uses time module to report runtime.

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

runtime_start_c = time.time()
p1c = cursor.execute('''SELECT COUNT(DISTINCT friends_count) FROM User''').fetchall()

cursor.close()
runtime_end_c = time.time()
print('The runtime for this query was {} seconds'.format(runtime_end_c - runtime_start_c))

print('Question 1 part D')

#finds unique friends count using python
#uses time module to report runtime.

runtime_start_d = time.time()

all_users = []
for tweet in tweets:
    try:
        tdict = json.loads(tweet.decode('utf-8'))
        user_data = [
            tdict['user']['id'],
            tdict['user']['name'],
            tdict['user']['screen_name'],
            tdict['user']['description'],
            tdict['user']['friends_count']
        ]
        all_users.append(user_data)
    except ValueError:
        pass

df_users = pd.DataFrame(all_users, columns = ['id', 'name', 'screen_name',
                                              'description', 'friends_count'])

unique_fc = df_users['friends_count'].unique()

runtime_end_d = time.time()

print('The runtime for this query was {} seconds'.format(runtime_end_d - runtime_start_d))

print('Question 1 part E contains a plot')

#uses python visualization to graph length of tweet vs length of username
#uses time module to report runtime.

twitter_data_url = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
webFD = urllib.request.urlopen(twitter_data_url)
tweets = webFD.readlines()

outfile_3 = open('tweet_errors_c.txt', 'w', encoding='utf-8')

lentweets = []
lenusername = []
for tweet in tweets[:92]:
    try:
        tdict = json.loads(tweet.decode('utf-8'))
        each_tweet = tdict['text']
        username = tdict['user']['name']
        if each_tweet != None and username != None:
            lentweets.append(len(each_tweet))
            lenusername.append(len(username))
    except ValueError:
        outfile_3.write(str(tweet))

plt.scatter(lenusername, lentweets)
plt.xlabel("Length of Username")
plt.ylabel("Length of Tweet")
plt.title("Username Length vs Tweet Length")
plt.show()
##NOTE only 90 tweets in total will be plotted because the first two tweets are invalid
outfile_3.close()   

