###
#Test file to see if we can iterate through a list of regexs instead call re.search and re.split over and over.
###
import re
import regex

lineTest = [regex.VBRMachineName, regex.VBRModule, regex.VMCSection, regex.wipRegex ]
def vmcCrawl(vmcLog):
    vmcContent = vmcLog.readlines()
    print("Printing Module info...")
    for index, line in enumerate(vmcContent):
        for lineCon in lineTest:
            lineCheck = re.search(lineCon, line)
            lineSplit = re.split(lineCon, str(lineCheck))
            if lineCheck:
                for mod in lineSplit:
                    modCheck = modCleanup(mod)
                    if modCheck == False:
                        continue
                    if lineCon == lineTest[0]:
                        print("Machine Name: ")
                    elif lineCon == lineTest[1]:
                        print("\tModule: ")
                    elif lineCon == lineTest[2]:
                        print("Section: ")
                    elif lineCon == lineTest[3]:
                        print("Inside section: ")
                    else:
                        continue
                    print(lineSplit[1])
#Moved the print for linesplit outside of the IF statements.l
            else:
                continue

def modCleanup(line):
    modCheckFirst = re.search(regex.modDropFirst, line)
    modCheckSecond = re.search(regex.modDropSecond, line)
    if modCheckFirst:
        return False
    if modCheckSecond:
        return False
    else:
        return True
