###
#Test file to see if we can iterate through a list of regexs instead call re.search and re.split over and #over.
###
import re
import regex

lineTest = ["regex.VBRModule"]
def vmcCrawl(vmcLog):
    vmcContent = vmcLog.readlines()
    print("Printing Module info...")
    for index, line in enumerate(vmcContent):
        srvName = re.search(regex.VBRMachineName, line)
        if srvName:
            print(line)
            continue
        for lineCon in lineTest:
            lineCheck = re.search(lineCon, line)
            lineSplit = re.split(lineCon, str(lineCheck))

            if len(str(lineSplit)) > 1:
                for mod in lineSplit:
                    modCheck = modCleanup(mod)
                    if mod == 'None' or modCheck == False:
                        continue
                    if str(lineCon) == "regex.VBRModule":
                         print("\tSection: ", mod)
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
