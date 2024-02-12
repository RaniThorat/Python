# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:47:26 2023

@author: Admin
"""

import psycopg2 as pg2

conn=pg2.connect(database='testme',user='postgres',password='root')

cur=conn.cur1()
cur.execute("select * from cur1")
rows=cur.fetchall()
conn.commit()
cur.close()
conn.close()
for row in rows:
    print(row)



#########################################################################################
import psycopg2 as pg2

conn=pg2.connect(database='testme',user='postgres',password='root')

cur=conn.cursor()

cur.execute("""select course_instructor,count(*) 
            from cur1 group by course_instructor""")
            
conn.commit()
rows=cur.fetchall()
for rows in rows:
    print(rows)
cur.close()

conn.close()

##############################################################################
import psycopg2 as pg2
conn=pg2.connect(database='testme',user='postgres',password='root')

cur=conn.cursor()

cur.execute("select * from cur1 order by course_instructor")

conn.commit()

rows=cur.fetchall()

for rows in rows:
    print(rows)
    
cur.close()

conn.close()
