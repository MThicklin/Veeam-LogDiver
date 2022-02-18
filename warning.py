import re, regex

ReGex = regex.regexWarn

def warning(logName, type):
    if type == "info":
        ReGex = regex.regexInfo
        print("Outputting Info entries...")
        fileName = "Info Log Output - " + str(logName) + ".txt"
    if type == "warn":
        print("Outputting Warning and Error entries...")
        fileName = "Warn Log Output - " + str(logName) + ".txt"
    else:
        print("Defaulting to Warning and Error entries...")
        fileName = "Warn Log Output - " + str(logName) + ".txt"        

    with open(str(fileName), "w") as output:
        for index, line in enumerate(logName.readlines()):
            x = re.search(ReGex, line)
            if x:
                y = index + 1
                output.write("{}: {}".format(y, line))
                print("{}: {}".format(y, line))
            else:
                continue
    output.close()