import sqlite3
from functions import current_date
from main import Stats


def create_stats_table(database_name, table_name, h1, h2, h3, h4):
	conn = sqlite3.connect(f'{database_name}.db')
	c = conn.cursor()

	try:
		c.execute('''CREATE TABLE {}
				({}, {}, {}, {})'''.format(table_name, h1, h2, h3, h4))
	except:
		print("This table already exists")


def create_entry(database_name, table_name, stat, h1, h2, h3, h4, col, id_date):
	conn = sqlite3.connect(f'{database_name}.db')
	c = conn.cursor()
	c.execute("SELECT EXISTS(SELECT 1 FROM {} WHERE {}='{}')".format(table_name, col, id_date))

	if not c.fetchone()[0]:
		c.execute("INSERT INTO {} ({}, {}, {}, {}) values (?, ?, ?, ?)".format(table_name, h1, h2, h3, h4), 
															(stat.date, stat.weight, stat.steps, stat.kcals))
	else:
		print("This entry already exists, just update it")


	conn.commit()


#the part below is based on
#https://www.sqlitetutorial.net/sqlite-python/update/

def create_connection(db_file):

	conn = None
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)

	return conn

def update_entry(database_name, table_name, column_name, task):
	conn = create_connection(f'{database_name}.db')

	with conn:
		sql = ''' UPDATE {}
			  SET {} = ?
			  WHERE id = ?
		'''.format(table_name, column_name)
		c = conn.cursor()
		c.execute(sql, task)
		conn.commit()



