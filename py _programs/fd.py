from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LocalWebserverAuth() 

drive = GoogleDrive(gauth)
file2=drive.CreateFile()
file1 =drive.CreateFile({'id': file2['id']})#{'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.GetContentFile('2a.c') # Set content of the file from given string.
#file1.Upload()
