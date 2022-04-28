import re
import regex

lineTest = [regex.VBRMachineName, regex.VBRModule, regex.VMCSection, regex.VMCinnerSection]
sectionTest = []

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
                        print("Machine Name: ", lineSplit[1])
                    elif lineCon == lineTest[1]:
                        print("\tModule: ", lineSplit[1])
                    elif lineCon == lineTest[2]:
                        print("Section: ", lineSplit[1])
                    elif lineCon == lineTest[3]:
                        innerSectionSplit = re.split(',', line)
                        print("Inside section: ")
                        for item in innerSectionSplit:
                            dateCheck = re.match (regex.lStrip, item)
                            if dateCheck:
                                strippedItem = re.sub(regex.lStrip,'',item)
                                print(strippedItem)
                                continue
                            print("\t",item)
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
