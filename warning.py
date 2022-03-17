import os, re, regex

def warning(logName, logContent, type):
    ReGex = regex.regexWarn
    itemCount = 0
    if type == "info":
        ReGex = regex.regexInfo
        fileName = "Info Log Output - " + str(logName) + ".txt"
        print("Outputting Info entries for ", fileName, "...")
    elif type == "warn":
        fileName = "Warn Log Output - " + str(logName) + ".txt"
        print("Outputting Warning and Error entries for ", fileName, "...")
    else:
        fileName = "Warn Log Output - " + str(logName) + ".txt"
        print("Defaulting to Warning and Error entries for ", fileName, "...")

    with open(str(fileName), "w") as output:
        for index, line in enumerate(logContent):
            x = re.search(ReGex, line)
            if x:
                itemCount += 1
                output.write("{}: {}".format(index + 1, x.string))
            else:
                continue
        output.write("Item Count: {}".format(itemCount))
        if itemCount == 0:
            output.close()
            os.rename(str(fileName), "No Good - {}".format(str(logName)))
    output.close()
