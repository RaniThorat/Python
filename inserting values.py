# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:23:14 2023

@author: Admin
"""

import psycopg2 as pg2

#create a coonection with postgreSQL
conn=pg2.connect(database='testme',user='postgres',password='root')

#Establish connection and start with cursor
cur=conn.cursor()


cur.execute("insert into cur1(course_name,course_instructor,topic)values('Introduction to Sql','Ram','Julia')");


cur.execute("insert into cur1(course_name,course_instructor,topic)values('Analyzing the survey data python','Sham','Python')");


cur.execute("insert into cur1(course_name,course_instructor,topic)values('Introduction to CHTGPT','Ganesh','Theory')");


cur.execute("insert into cur1(course_name,course_instructor,topic)values('Testing in python','Jayesh','Python')");

conn.commit()

cur.close();
conn.close();