import re, regex
from sys import argv

ReGex = regex.regexWarn
fileName = ""
EntriesToFind = ""

try:
    EntriesToFind = argv[2]
except IndexError:
    EntriesToFind = input("Do you need info or warn entries? ")

with open(argv[1], "r") as log:
    try:
        if EntriesToFind == "info":
            ReGex = regex.regexInfo
            print("Outputting Info entries...")
            fileName = "Info Log Output - " + str(argv[1]) + ".txt"
        if EntriesToFind == "warn":
            print("Outputting Warnings and Errors entries...")
            fileName = "Warn Log Output - " + str(argv[1]) + ".txt"
        with open(str(fileName), "w") as output:
            for index, line in enumerate(log.readlines()):
                x = re.search(ReGex, line)
                if x:
                    y = index + 1
                    output.write("{}: {}".format(y, line))
                    #print("{}: {}".format(y, line))
                else:
                    continue
    finally:
        output.close()
log.close()