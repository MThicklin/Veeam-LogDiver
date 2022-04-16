import os
from warn import warning

logFile = []

def logWriter():
    for file in os.listdir(os.getcwd()):
        fileName = "Warn Log Output - " + str(file) + ".txt"
        if os.path.exists(fileName):
            print('{} already exists. Skipping...'.format(fileName))
            continue
        if file.endswith(".log") and file != "VMC.log":
            logFile.append(file)

    for index, file in enumerate(logFile):
        with open(os.path.join(os.getcwd(), str(logFile[index])), "r") as log:
            logContent = log.readlines()
            fileName = "Warn Log Output - " + str(file) + ".txt"
            warning(fileName, logContent)
        log.close()