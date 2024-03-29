import re
import regex

lineTest = [regex.VBRMachineName, regex.VBRModule, regex.VMCSection, regex.VMCinnerSection]

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
                        lineSplitter(line)
                    elif lineCon == lineTest[1]:
                        print("\tModule: ", lineSplit[1])
                    elif lineCon == lineTest[2]:
                        print("Section: ", lineSplit[1])
                    elif lineCon == lineTest[3]:
                        print("Inside section: ")
                        lineSplitter(line)                        
            else:
                continue

def modCleanup(line):
    modCheckFirst = re.search(regex.modDropFirst, line)
    modCheckSecond = re.search(regex.modDropSecond, line)
    modCheckThird = re.search(regex.modDropThird, line)
    if modCheckFirst:
        return False
    if modCheckSecond:
        return False
    if modCheckThird:
        return False
    else:
        return True

def lineSplitter(line):
    innerSectionList = []
    innerSectionSplit = re.split(',', line)
    for item in innerSectionSplit:
        dateCheck = re.match (regex.lStrip, item)
        if dateCheck:
            strippedItem = re.sub(regex.lStrip,'',item)
            print(strippedItem)
            continue
        print(item)
    return innerSectionList