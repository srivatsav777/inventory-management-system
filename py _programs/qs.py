from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LocalWebserverAuth() 

drive = GoogleDrive(gauth)

#file1 =drive.CreateFile()#{'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#file1.SetContentFile('process.bpmn') # Set content of the file from given string.
#file1.Upload()

#file2 =drive.CreateFile({'id': file1['id']})#{'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#file2.GetContentFile('2a.c')


file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
print (drive.GetAbout())
for file1 in file_list:
  #print('title: %s, id: %s' % (file1['title'], file1['id']))
  if(file1['title']=='2a.c'):
     file2=drive.CreateFile()
     file2.GetContentFile('file1')
