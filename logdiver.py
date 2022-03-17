import os, sys
from warning import warning
#from topsection import topSection
from vmc import vmcCrawl

searchType = ""
ProcessJobs = ""
crawl = ""
logName = ""
logFile = []
logFileAskedskip = False

try:
    if sys.argv[2] == "warn" or "info":
        searchType = sys.argv[2]
    else:
        searchTypeAsked = input("Please specify info or warn entries: ")
        searchType = searchTypeAsked
except IndexError:
    searchType = ""
    pass

def sysCrawl():
    try:
        with open(os.path.join(os.getcwd(), "VMC.log")) as vmcLog:
            vmcCrawl(vmcLog)
        vmcLog.close()
    except FileNotFoundError:
        print("VMC.log Not found.  This function needs the VMC.log from the utils folder of the VB&R logs.")

def cleaner():
    filesCleaned = 0
    print("Cleaning all logdiver files...")
    for file in os.listdir(os.getcwd()):
        if file.startswith("Warn Log Output - ") or file.startswith(
                "Info Log Output - ") or file.startswith("Top Section for ") or file.startswith("test"):
            os.remove(file)
            filesCleaned += 1
    return print("All Clean! Files cleaned: ", filesCleaned)


def crawler():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".log") and file != "VMC.log":
            logFile.append(file)
    return logFile


if sys.argv[1] == "clean":
    cleaner()
    exit()
    
if sys.argv[1] == "vmc":
    sysCrawl()
    exit()

elif sys.argv[1] == "crawl":
    searchType = sys.argv[2]
    crawler()
else:
    logFileInput = sys.argv[1]
    logFile.clear()
    logFile.append(logFileInput)
    logFileAskedskip = False


def writer(logFile, searchType):
    for index, file in enumerate(logFile):
        with open(os.path.join(os.getcwd(), str(logFile[index])), "r") as log:
            logContent = log.readlines()
            warning(file, logContent, searchType)
        log.close()


#def section(logFile):
#    for index, file in enumerate(logFile):
#        with open(os.path.join(os.getcwd(), str(logFile[index])),
#                  "r") as topSec:
#            topSection(file, topSec)
#        topSec.close()


#section(logFile)
writer(logFile, searchType)
