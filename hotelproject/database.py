import mysql.connector


mydb = mysql.connector.connect(host='localhost', user='hotel', password='hotel', database='hotelms')

class Manager:
	def __init__(self):
		print('manager is in use')

	def is_valid(self):
		pass

	@staticmethod
	def add_to_db(self, cursor , value):
		cursor.execute('INSERT INTO hotel VALUES(%s, %s, %s, %s, %s, %s)', value)

	def delete_value(self, id):
		cursor.execute('DELETE FROM hotel WHERE id = %s', id)

