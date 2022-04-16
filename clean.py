import os

startsWithList = ["Warn Log Output - ", "No Good - "]

def cleaner(nukeCheck):
    filesCleaned = 0
    if nukeCheck == 0:
        for file in os.listdir(os.getcwd()):
            for startsWith in startsWithList:
                if file.startswith(startsWith):
                    os.remove(file)
                    filesCleaned += 1
        print("All Clean! Files cleaned: ", filesCleaned)

    if nukeCheck == 1:
        nukeCheck = input("Please type YES to finish...")
        if nukeCheck == "YES":
            for file in os.listdir(os.getcwd()):
                if file.endswith(".txt") or file.endswith(".log"):
                    os.remove(file)
                    filesCleaned += 1
            print("Nuclear Option Executed! Files cleaned: ", filesCleaned)
        else:
            print("YES in all caps not entered...")
            print("Nuclear Option Deactivated...")
            print("{} Files deleted, Exiting...".format(filesCleaned))
