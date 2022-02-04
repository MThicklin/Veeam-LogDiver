import re, regex

def topSection(log):
    x = re.match(regex.VBRMachinenameLine, str(log))
    y = re.match(regex.VBRMachineName, str(x))
    z = re.match(regex.VBRos, str(x))
    print("Machine Name is: ", y, " OS is: ", z)

#try:
    #hostinfo = argv[0]
    #if hostinfo == 'Y' or 'y':
        #hostinfo = True
    #logFile = argv[1]
    #search = argv[2]
#except IndexError:
    #hostinfo = input('Do you want info on the host for this log?')
    #if hostinfo == 'Y' or 'y':
        #hostinfo = True
    #logFile = input("Where is your log?")
    #search = input("Am I looking for something specific?")