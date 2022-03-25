import os, sys
from warning import warning

logName = ""
logFile = []

def cleaner():
    filesCleaned = 0
    print("Cleaning all logdiver files...")
    for file in os.listdir(os.getcwd()):
        if file.startswith("Warn Log Output - ") or file.startswith(
                "Info Log Output - ") or file.startswith("Top Section for ") or file.startswith("test") or file.startswith("No Good - "):
            os.remove(file)
            filesCleaned += 1
    return print("All Clean! Files cleaned: ", filesCleaned)

def vmcCrawl():
    try:
        with open(os.path.join(os.getcwd(), "VMC.log")) as vmcLog:
            vmcCrawl(vmcLog)
        vmcLog.close()
    except FileNotFoundError:
        print("VMC.log Not found.  This function needs the VMC.log from the utils folder of the VB&R logs.")

def logCrawler():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".log") and file != "VMC.log":
            logFile.append(file)
    return logFile

def logWriter(logFile):
    for index, file in enumerate(logFile):
        with open(os.path.join(os.getcwd(), str(logFile[index])), "r") as log:
            logContent = log.readlines()
            warning(file, logContent)
        log.close()

if sys.argv[1] == "clean":
    cleaner()
    exit()
    
if sys.argv[1] == "vmc":
    vmcCrawl()
    exit()
    
if sys.argv[1] == "crawl":
    logCrawler()
    logWriter(logFile)
    exit()