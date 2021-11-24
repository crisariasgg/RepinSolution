# Local imports
import datetime


# Third party 
import pandas as pd
import pymysql
from sqlalchemy import create_engine



class PartsPalImport():

	def __init__(self,name,user,host,port,password):
	
		self.user = user
		self.password = password
		self.host = host
		self.port = port 
		self.name = name
		self.connection_results = self.connection_to_db(self.name,self.user,self.host,self.port,self.password)
		
		
	def connection_to_db(self,name,user,host,port,password):
		connection_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(user, password, host, port, name)
		try:
			print('establishing connection...')
			connection = create_engine(connection_string)
			connection.connect()
		except Exception:
			raise("Error, can't establishing connection...")
		else:
			print ('No exception occurred')
		return connection
		

	def read_input_file(self,filename):
		data=pd.read_csv(filename)
		return data


	def insert_date_to_column(self,data,day):
		data['date'] = datetime.date.today()+datetime.timedelta(days=day)
		return data


	def import_to_sql(self,data,connection):
		data.to_sql(name='import_excel_partsauthority', con=connection, if_exists = 'append', index=False)

		



   







# def main():

# 	# Database credentials
# 	NAME='excel_comparison'
# 	USER = 'root'
# 	PASSWORD = 'Minimalista1'
# 	HOST = 'localhost'
# 	PORT = 3306

	# IMPORTING CSV FILE
	# data = read_input_file('prueba.csv')
	# add_future_date(data,1)

	# # IMPORTING DATA TO SQL
	# connection=connection_to_db(USER,PASSWORD,HOST,PORT,NAME)
	# import_to_sql(data,connection)
	

# if __name__ == "__main__":
# 	main()