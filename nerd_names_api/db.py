import os
from flask import g
import pyodbc

# Get environ vars for DB connection
DRIVER   = '{ODBC Driver 13 for SQL Server}'
SERVER   = os.environ['DB_HOST']
DATABASE = os.environ['DB_NAME']
USERNAME = os.environ['DB_USERNAME']
PASSWORD = os.environ['DB_PASSWORD']


def query_mysql(query):
	"""Run query on connection stored in g."""
	cnx = get_db()
	cursor = cnx.cursor()
	cursor.execute(query)
	results = cursor.fetchall()
	# Cast to list rather than custom pyodbc 'Row' data structure
	results = [list(row) for row in results]
	# Add column labels
	columns = [column[0] for column in cursor.description]
	results_processed = [{col: val for col, val in zip(columns, row)} for row in results]
	cursor.close()
	return results_processed


def get_db():
	"""Connect to DB and store connection in g for life of request."""
	if 'db' not in g:
		g.db = pyodbc.connect('DRIVER=' + DRIVER +
							  ';SERVER=' + SERVER +
							  ';PORT=1433;' +
							  'DATABASE=' + DATABASE +
							  ';UID=' + USERNAME +
							  ';PWD=' + PASSWORD)
	return g.db


def close_db(e=None):
	"""Remove connection to db from g and close."""
	db = g.pop('db', None)
	if db is not None:
		db.close()


def init_app(app):
	"""In factory function, register the close_db function so
	that connections closed at end of request.
	"""
	app.teardown_appcontext(close_db)
