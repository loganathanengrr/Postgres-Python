import os
import psycopg2

class DBConnect():
	"""
	static method returns the connection object
	"""
	@classmethod
	def connect(cls, hostname, database_name, username=None, password=None):
		connection = None
		try:
			connection = psycopg2.connect(
				dbname=database_name, user=username, password=password, host=hostname
				)
		except psycopg2.Error as error:
			print(error)

		return connection



if __name__ == '__main__':
	username = os.environ.get("DB_USERNAME")
	password = os.environ.get("DB_PASSWORD")
	hostname = "postgres-rds-python.cd5fqbgabgpv.ap-south-1.rds.amazonaws.com"
	database_name = 'Users'
	connection = DBConnect.connect(hostname, database_name, username, password)
	if connection:
		print("database connected")
		try:

			cursor = connection.cursor()
			# cursor.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")
			cursor.execute("INSERT INTO student (name) values(%s)", ("Vijay", ))
			connection.commit()
			cursor.execute("SELECT * FROM student")
			print(cursor.fetchall())
			cursor.close()
		except psycopg2.Error as error:
			print(error)

		connection.close()
