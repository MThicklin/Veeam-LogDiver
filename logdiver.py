import os, sys
from warning import warning
#2

searchType = ""
ProcessJobs = ""
crawl = ""
logFile = []
logFileAskedskip = False

for option in sys.argv:
    if option == "crawl":
        logFileAskedskip = True
        for file in os.listdir(os.getcwd()):
            if file.endswith(".log"):
                print(os.path.join(os.getcwd(), file))
                filePath = os.path.join(os.getcwd(), file)
                logFile.append(filePath)
    else:
        try:
            logFileInput = sys.argv[1]
            logFile.clear()
            logFile.append(logFileInput)
            searchTypeInput = sys.argv[2]
            searchType = searchTypeInput
            #processJobsInput = sys.argv[3]
            #processJobs = processJobsInput
        except IndexError:
            searchTypeAsked = input("Do you need info or warn entries? ")
            searchType = searchTypeAsked
            #ProcessJobsAsked = input("Do you want to display the jobs in the log? ")
            #processJobs = processJobsAsked
            if logFileAskedskip == True:
                pass
            else:
                logFileAsked = input("Where is the log file? ")
                logFile.clear()
                logFile.append(os.path.join(os.getcwd(),logFileAsked))
                
    if option == "warn" or "info":
        searchType = str(option)
        
#1    
for index,file in enumerate(logFile):
    with open(os.path.join(os.getcwd(), str(logFile[index])),"r") as log:
        if (searchType):
            warnings = warning(log, searchType)
    log.close()

#1:
#try:
    #with open(os.path.join(os.getcwd(), logFile[0]),"r") as log:
        #if (searchType):
            #warnings = warning(log, searchType)
            #print(warnings)
        #if ProcessJobs == "y" or "y":
            #jobs = jobMaker(log)
            #print(jobs)
        
#except FileNotFoundError:
    #print("File not found. From single path.")

#2
#from topSection import topSection
#from jobs import jobMaker