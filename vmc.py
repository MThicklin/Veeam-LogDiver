###
#Test file to see if we can iterate through a list of regexs instead call re.search and re.split over and over.
###
import re
import regex

lineTest = [regex.VBRMachineName, regex.VBRModule, regex.VMCSection ]
def vmcCrawl(vmcLog):
    vmcContent = vmcLog.readlines()
    print("Printing Module info...")
    for index, line in enumerate(vmcContent):
        lineConNum = 0
        #srvName = re.search(regex.VBRMachineName, line)
        #if srvName:
            #print(line)
            #continue
        for lineCon in lineTest:
            lineConNum += 1
            lineCheck = re.search(lineCon, line)
            #print("lineCheck: ", lineCon)
            lineSplit = re.split(lineCon, str(lineCheck))
            #print("lineSplit: ", lineSplit)
            if lineCheck:
                for mod in lineSplit:
                    modCheck = modCleanup(mod)
                    if modCheck == False:
                        continue
                    if lineCon == regex.VBRMachineName:
                        print("Machine Name: ", lineSplit[1])
                    elif lineCon == regex.VBRModule:
                        print("\tModule: ", lineSplit[0])
                    elif lineCon == regex.VMCSection:
                        print("Section: ", lineSplit[0])
                    #else:
                        #continue
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
