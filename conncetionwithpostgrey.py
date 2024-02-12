# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:36:35 2023

@author: Admin
"""

import psycopg2 as pg2

#create a connection with postgresql
#password is whatever you set
conn=pg2.connect(database='dvdrental',user='postgres',password='root')

#establish connection and start curosr to be ready to quoery
cur=conn.cursor()

#pass in a postgrey query as a string
cur.execute("select * from payment")

#return a tuple of the first row as a python
cur.fetchone()

#return a tuple of the many row as a python
cur.fetchmany(10)

# returning a tuple of the all row as a pytohn
cur.fetchall()

#To save and index results ,assign  it to a variable
data=cur.fetchmany(10)

#close the connection
conn.close()
