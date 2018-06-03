#import
import os
import datetime
from shutil import copy, rmtree

#make it look pretty, probably could have made this its own separate thing to make it look cleaner
print("\n\
	================================================\n\
	| DARK SOULS REMASTERED AUTO SAVE BACK/RESTORE |\n\
	================================================")

print("             Option                        Command\n\
	   Back up & start.............backup or nothing\n\
	   Restore.....................restore\n")

#get user input
op = input("What would you like to do? ")

#check if backing up or restoring saves
if(op == '' or op == 'backup'):
	print("Backing up saves and starting...\n")

	#check if backup folder exists in DSR save loaction
	if not os.path.exists('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups'):
		os.makedirs('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups')

	#cout up the number of saves currently, we only want to keep the most recent 5
	folders = 0
	folderlist = []
	for _, dirs, _ in os.walk('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\'):
		for dirname in dirs:
			folders = folders + 1

	#check the number of folders, either make new fodler or delete one first
	if folders < 5:
		#get datetime and make folder with the name of the datetime
		folderName = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
		os.makedirs('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\' + folderName)
		#copy saves over to backup folder
		for _,_,files in os.walk('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\'):
			for filename in files:
				file_ = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\' + filename
				dest = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\' + folderName
				copy(file_,dest)
	#delete the oldest backup and make a new one
	else:
		location = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\'
		folderList = []
		#get all folder names and convert them to datetimes
		for _, dirs, _ in os.walk('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\'):
			for dirname in dirs:
				folderList.append(datetime.datetime.strptime(dirname,"%Y-%m-%d %H-%M-%S"))
		rmFolder = datetime.datetime.strftime(min(folderList) ,'%Y-%m-%d %H-%M-%S')
		#remove oldest backup
		rmtree(location + rmFolder)
		#make a new backup just like above
		folderName = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
		os.makedirs('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\' + folderName)
		for _,_,files in os.walk('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\'):
			for filename in files:
				file_ = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\' + filename
				dest = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\' + folderName
				copy(file_,dest)


	os.system('C:\\Users\\Kyle\\Documents\\NBGI\\"DARK SOULS REMASTERED"\\"DARK SOULS REMASTERED.url"')

elif(op == 'restore'):
	#quick check for no backups
	folders = 0
	folderlist = []
	for _, dirs, _ in os.walk('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\'):
		for dirname in dirs:
			folders = folders + 1

	if folders == 0:
		print('No backups, cannot restore...')
		exit(1)

	location = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\'
	folderList = []
	#get all folder names and convert them to datetimes
	for _, dirs, _ in os.walk('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\'):
		for dirname in dirs:				
			folderList.append(datetime.datetime.strptime(dirname,"%Y-%m-%d %H-%M-%S"))
	resFolder = datetime.datetime.strftime(max(folderList) ,'%Y-%m-%d %H-%M-%S')
	#copy & overwrite save files from backup to DSR saves folder
	for _,_,files in os.walk('C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\'):
			for filename in files:
				file_ = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\Backups\\' + resFolder + '\\' + filename
				dest = 'C:\\Users\\Kyle\\Documents\\NBGI\\DARK SOULS REMASTERED\\48549215\\'
				copy(file_,dest)

	op = input("Would you like to run the game now? ")
	if op == 'y' or op == 'Y':
		os.system('C:\\Users\\Kyle\\Documents\\NBGI\\"DARK SOULS REMASTERED"\\"DARK SOULS REMASTERED.url"')
	exit(0)