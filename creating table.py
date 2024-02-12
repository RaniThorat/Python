# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:20:05 2023

@author: Admin
"""

#after installing with pip install psycopg2
import psycopg2 as pg2

#create connection with postgresql
conn=pg2.connect(database='testme',user='postgres',password='root')

#establish connection and start curosr to be ready to query
cur=conn.cursor()

#Execute a command :create courser table
cur.execute(""" create table cur1(
    course_id serial primary key,
    course_name varchar(50) unique not null,
    course_instructor varchar (100) not null,
    topic varchar(20) not null)""")

#make thechanges to the database persistance
conn.commit()

#close the connection
conn.close()
