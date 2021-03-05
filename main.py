""" IMPORTANT """
"""
MAKE SURE TO OPEN THE FOLDER IN TERMINAL OTHERWISE THE DEFAULT LOCATION OF TERMINAL IS HOME WHERE FILES WILL BE PLACED
"""
import os
import shutil

workingdirectory = os.getcwd()
name = input("Enter the name of folder (create if not exist): ")
name.replace(" ", "_")
fileType = input("Enter the file extension (without '.') : ")
fileType = "." + fileType
fullpath = os.path.join(workingdirectory, name)
print(fullpath)
try:
    os.mkdir(fullpath)
except:
    print("A folder named ", name, "already exists")
count = 0
errors = 0
for foldername, subfoldersList, filesList in os.walk(".\\"):
    for fileName in filesList:
        if fileName.endswith(fileType):
            try:
                shutil.copy(os.path.join(foldername, fileName), fullpath)
                print(fileName)
                count += 1
            except:
                errors += 1
print(count, " ", errors)
