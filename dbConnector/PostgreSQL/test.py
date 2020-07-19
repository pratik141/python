#!/usr/bin/python

import psycopg2
from config import configLoader as config

def pingtest():
	""" write to the PostgreSQL database server """
	try:
		# read connection parameters
		params = config(section="postgresqlReader")

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)

		# create a cursor
		cur = conn.cursor()

		# get a DB version
		cur.execute('SELECT version()')
		db_version = cur.fetchone()
		print('PostgreSQL database version: {}'.format(db_version))

	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)

	finally:
	    conn.close()
	    print('Database connection closed.')

databaseReader()
