#!/usr/bin/python
#Filename: backup_ver1.py

import os
import time

#1.The files and directories to be backed up are specified in a list
source = ['"/Users/Linda8_Yang/Desktop/file"', '"/Users/Linda8_Yang/GitHub/Python"']
#Notice we had to use double quotes inside the string for names with spaces in it.

#2.The backup must be stored in a main backup directory
target_dir = '/Volumes/Other/GitHub'
#Remember to change this to what you will be

#3.The files are backed up into a zip file.
#4.The name of the zip archive is the current date and time.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5.We use the zip command to put the files in a zip archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

#Run the backup
print(zip_command)
if os.system(zip_command) == 0:
    print("Successfully to backup file!")
else:
    print("Backup file failed")


 


