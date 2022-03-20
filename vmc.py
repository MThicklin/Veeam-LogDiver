import re, regex

def vmcCrawl(vmcLog):
    vmcContent = vmcLog.readlines()
    print("Printing Module info...")
    for index,line in enumerate(vmcContent):
        srvName = re.search(regex.VBRMachineName, line)
        if srvName:
            print(line)
        moduleLine = re.search(regex.VBRModule,line)
        module = re.split(regex.VBRModule, str(moduleLine))
        if len(module) > 1:
            for mod in module:
                modCheck = modCleanup(mod)
                if mod == 'None' or modCheck == False:
                    continue
                else:
                    print("\tModule: ", mod)
        titles = re.search('(?:={23})([\w\s-]*)(?:={26})',line)
        title = re.split('[={24}]([\w\s-]*)[={26}]', str(titles))
        if len(title) > 1:
            for words in title:
                modCheck = modCleanup(words)
                if words == 'None' or words == '' or modCheck == False:
                    continue
                else:
                    print("\t\tSection: ", words)
        hostLine = re.search('HostID:', line)
        if hostLine:
            hostId = re.split(',', line)
            for host in hostId:
                print("\t\t\tHost ID: ",host)
        #print("\t\tPrint line: ",line)

def modCleanup(line):
    modCheckFirst = re.search(regex.modDropFirst, line)
    modCheckSecond = re.search(regex.modDropSecond, line)
    if modCheckFirst:
        return False
    if modCheckSecond:
        return False
    else:
        return True