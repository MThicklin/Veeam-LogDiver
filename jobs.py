#from parseXML import parseXML

#class job:
    #job.name = line[1]
    #job.id = line[2]
    #job.result = line[3]
    #job.state = line[4]

def jobMaker(log):
    logLines = log.readlines()
    for index,line in enumerate(logLines):
        if line:
            Name = line.partition("Name:")
            JobState = line.partition("Job state:")
            ScheduleOptions = line.partition("Schedule options")
            Advanced = line.partition("Advanced:")

            nameList = list(Name[2:3])
            jobStateList = list(JobState[2:3])
            scheduleOptionsList = list(ScheduleOptions[2:3])
            advancedList = list(Advanced[2:3])

            #This function will parse the 'Advanced' section of current jobs.  Need to work on parseXML.
            #parseXML(advancedList)

            print(nameList, jobStateList, scheduleOptionsList, advancedList)
            
            #job.append(list(filter(regexName.match, Name)))

            #print(job)


    else:
            print ("End Of file")