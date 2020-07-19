#!/usr/bin/python

import psycopg2
from config import configLoader as config

def databasereader():
	""" write to the PostgreSQL database server """
	try:
		# read connection parameters
		params = config(section="postgresqlReader")

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)

		# create a cursor
		cur = conn.cursor()

		### sample 
		## Read data
		cur = conn.cursor()

		cur.execute("SELECT id, name, address, salary  from COMPANY")
		rows = cur.fetchall()
		for row in rows:
		   print ("ID      = ", row[0])
		   print ("NAME    = ", row[1])
		   print ("ADDRESS = ", row[2])
		   print ("SALARY  = ", row[3], "\n")

		print ("Operation done successfully")
		conn.close()

	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)

	finally:
	    conn.close()
	    print('Database connection closed.')

databasereader()
