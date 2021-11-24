"""This module download a zip file from a FTP server and unzip it"""



import ftplib
import zipfile


class FTPConnection():
	
	def __init__(self,FTP_HOST,FTP_USER,FTP_PASS):

		self.ftp_host = FTP_HOST
		self.ftp_user = FTP_USER
		self.ftp_pass = FTP_PASS

		self.connection_results = self.connection_to_ftp(self.ftp_host,self.ftp_user,self.ftp_pass)


	def connection_to_ftp(self,host,user,password):
		try:
			print("establishing server's connection...")
			connection = ftplib.FTP(host, user, password)
			connection.encoding = "utf-8"
		except Exception:
			raise("Error, can't establishing connection...")
		else:
			print ('No exception occurred')
		return connection


class DownloadFromFTP():
	
	def __init__(self,filename,ftp_connection):
	
		self.filename = filename
		self.ftp_connection = ftp_connection
		self.get_file_from_server(self.filename,self.ftp_connection)
		self.unzip_file(self.filename)
	
    
	def get_file_from_server(self,filename,ftp):
		with open(filename, "wb") as file:  
			ftp.retrbinary(f"RETR {filename}", file.write)


	def unzip_file(self,file):
		with zipfile.ZipFile(file, 'r') as zip_ref:
			zip_ref.extractall()


	