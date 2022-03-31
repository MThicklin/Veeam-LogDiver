import os, sys, shutil
from warning import warning
from vmc import vmcCrawl

logName = ""
logFile = []

def cleaner(nukeCheck):
    filesCleaned = 0
    if nukeCheck == 0:
        for file in os.listdir(os.getcwd()):
            if file.startswith("Warn Log Output - ") or file.startswith(
                "Info Log Output - ") or file.startswith("Top Section for ") or file.startswith("test") or file.startswith("No Good - "):
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

def stow(folderName):
    filesMoved = 0
    srcPath = os.getcwd()
    destPath = os.path.join(srcPath, folderName)
    os.mkdir(destPath)
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt") or file.endswith(".log"):
            shutil.move(srcPath+file, destPath+file)
            filesMoved += 1
    print("{} files stowed away in {}".format(filesMoved, folderName))

def vmcLogCrawl():
    try:
        with open(os.path.join(os.getcwd(), "VMC.log")) as vmcLog:
            vmcCrawl(vmcLog)
        vmcLog.close()
    except FileNotFoundError:
        print("VMC.log Not found.  This function needs the VMC.log from the utils folder of the VB&R logs.")

def logCrawler():
    for file in os.listdir(os.getcwd()):
        fileName = "Warn Log Output - " + str(file) + ".txt"
        if os.path.exists(fileName):
            print('{} already exists. Skipping...'.format(fileName))
            continue
        if file.endswith(".log") and file != "VMC.log":
            logFile.append(file)
    return logFile

def logWriter(logFile):
    for index, file in enumerate(logFile):
        with open(os.path.join(os.getcwd(), str(logFile[index])), "r") as log:
            logContent = log.readlines()
            fileName = "Warn Log Output - " + str(file) + ".txt"
            warning(fileName, logContent)
        log.close()

if sys.argv[1] == "clean":
    print("Cleaning all Log diver txt files.")
    cleaner(0)
    exit()
        
if sys.argv[1] == "nuke":
        print("Nuclear Option Activated...")
        print("ALL NON-LOGDIVER FILES WILL BE DELETED...")
        cleaner(1)

if sys.argv[1] == "stow":
        folderName = input("Name the folder to stow the files in: ")
        stow(folderName)
    
if sys.argv[1] == "vmc":
    vmcCrawl()
    exit()
    
if sys.argv[1] == "crawl":
    logCrawler()
    logWriter(logFile)
    exit()