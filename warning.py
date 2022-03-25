import os, re, regex

def warning(logName, logContent):
    itemCount = 0
    fileName = "Warn Log Output - " + str(logName) + ".txt"
    print("Outputting Warning and Error entries for ", logName, "...")

    with open(str(fileName), "w") as output:
        for index, line in enumerate(logContent):
            x = re.search(regex.regexWarn, line)
            if x:
                itemCount += 1
                output.write("{}: {}".format(index + 1, x.string))
            else:
                continue
        output.write("Item Count: {}".format(itemCount))
        if itemCount == 0:
            output.close()
            os.rename(str(fileName), "No Good - {}.txt".format(str(logName)))
            print('No items of interest in {}'.format(str(logName)))
    output.close()
