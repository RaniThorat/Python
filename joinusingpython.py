# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:18:38 2023

@author: Admin
"""

import psycopg2 as pg2

#create connection with postgresql
conn=pg2.connect(database='testme',user='postgres',password='root')

#establish connection and start curosr to be ready to query
cur=conn.cursor()

#Execute a command :create courser table
cur.execute(""" create table cur_add(
    course_id serial primary key,
    duration varchar(50) unique not null,
    fees integer )
    """)

#make thechanges to the database persistance
conn.commit()

#close the connection
conn.close()


####################################################################
import psycopg2 as pg2

#create a coonection with postgreSQL
conn=pg2.connect(database='testme',user='postgres',password='root')

#Establish connection and start with cursor
cur=conn.cursor()


cur.execute("insert into cur_add(duration,fees)values('14days',50000)");


cur.execute("insert into cur_add(duration,fees)values('50days',60000)");


cur.execute("insert into cur_add(duration,fees)values('40days',70000)");


cur.execute("insert into cur_add(duration,fees)values('30days',5000)");

conn.commit()

cur.execute("""select  course_name,course_instructor, topic, course_id
            from cur1
            inner join cur_add
            on cur1. course_id=cur_add. course_id
            """ )

cur.close();
conn.close();


#########################################################################

