#!/usr/bin/python

import psycopg2
from config import configLoader as config

def databasewriter():
	""" write to the PostgreSQL database server """
	try:
		# read connection parameters
		params = config(section="postgresqlWriter")

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)

		# create a cursor
		cur = conn.cursor()

		### sample 
		## create table

		cur = conn.cursor()
		cur.execute('''
			CREATE TABLE COMPANY(
		      ID INT PRIMARY KEY     NOT NULL,
		      NAME           TEXT    NOT NULL,
		      AGE            INT     NOT NULL,
		      ADDRESS        CHAR(50),
		      SALARY         REAL);''')
		print ("Table created successfully")
		conn.commit()

		## Insert
		cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (1, 'user1', 44, 'abc', 60158 )");

		cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (2, 'user2', 53, 'qwe', 83000 )");

		cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (3, 'user3', 38, 'asd', 44920 )");

		cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (4, 'user4', 25, 'xyz ', 35078 )");
		conn.commit()
		print ("Records created successfully")

		# closing connection
		conn.close()

	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)

	finally:
	    conn.close()
	    print('Database connection closed.')

databasewriter()
