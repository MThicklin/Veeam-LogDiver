import os

currentDir = os.getcwd()
cleanList = ["Warn Log Output - ", "No Good - "]
nukeList = [".txt", ".log"] 

def cleaner(nukeCheck):
    filesCleaned = 0
    if nukeCheck == 0:
        for file in os.listdir(currentDir):
            for startsWith in cleanList:
                if file.startswith(startsWith):
                    os.remove(file)
                    filesCleaned += 1
        print("All Clean! Files cleaned: ", filesCleaned)

    if nukeCheck == 1:
        nukeCheck = input("Please type YES to finish...")
        if nukeCheck == "YES":
            for file in os.listdir(currentDir):
                for endsWith in nukeList:
                    if file.endswith(endsWith):
                        os.remove(file)
                        filesCleaned += 1
            print("Nuclear Option Executed! Files cleaned: ", filesCleaned)
        else:
            print("YES in all caps not entered...")
            print("Nuclear Option Deactivated...")
            print("{} Files deleted, Exiting...".format(filesCleaned))
