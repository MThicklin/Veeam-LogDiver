#from parseXML import parseXML
import re, regex
#class job:
#job.name = line[1]
#job.id = line[2]
#job.result = line[3]
#job.state = line[4]

jobList = []

def jobMaker(jobLines):
    logLines = jobLines.readlines()
    for index, line in enumerate(logLines):
        if re.search(regex.regexBackupJob, line):
            cleanBackupLine = re.sub(regex.regexLStrip, '', line)
            print(index, ": ", cleanBackupLine)
            jobList.append(index, ": ", cleanBackupLine)
        elif re.search(regex.regexJobState, line):
            cleanJobStateLine = re.sub(regex.regexLStrip, '', line)
            print(index, ": ", cleanJobStateLine)
        elif re.search(regex.regexSchedule, line):
            cleanScheduleLine = re.sub(regex.regexLStrip, '', line)
            print(index, ": ", cleanScheduleLine)
        elif re.search(regex.regexAdvanced, line):
            cleanAdvancedLine = re.sub(regex.regexLStrip, '', line)
            print(index, ": ", cleanAdvancedLine)
print(jobList)
        