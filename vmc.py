import re
import regex


def vmcCrawl(vmcLog):
    vmcContent = vmcLog.readlines()
    print("Printing Module info...")
    for index, line in enumerate(vmcContent):
        srvName = re.search(regex.VBRMachineName, line)
        if srvName:
            print(line)
        moduleLine = re.search(regex.VBRModule, line)
        module = re.split(regex.VBRModule, str(moduleLine))
        if len(module) > 1:
            for mod in module:
                modCheck = modCleanup(mod)
                if mod == 'None' or modCheck == False:
                    continue
                else:
                    print("\tModule: ", mod)
        titles = re.search(regex.regexVMCSection, line)
        title = re.split(regex.regexVMCSection, str(titles))
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
                print("\t", host)
        proxyLine = re.search('ProxyID', line)
        if proxyLine:
            proxyID = re.split(',', line)
            for proxy in proxyID:
                print("\t\t", proxy)
        proxyTypes = re.search('Proxy types: ', line)
        if proxyTypes:
            proxyItems = re.split(',', line)
            for type in proxyItems:
                print("\t\t", type)
        platformLine = re.search('PlatformId:', line)
        if platformLine:
            platformItems = re.split(',', line)
            insideLine = re.search('\{', line)
            insideLineEnd = re.search('\}', line)
            insideJob = False
            for platformItem in platformItems:
                if platformItem == insideLine:
                    insideJob = True
                while insideJob == True:
                    print("\t\t\t", platformItem)
                    if platformItem == insideLineEnd:
                        insideJob == False
                        continue
                print("\t\t\t", platformItem)

    print("DK: ", line)


def modCleanup(line):
    modCheckFirst = re.search(regex.modDropFirst, line)
    modCheckSecond = re.search(regex.modDropSecond, line)
    if modCheckFirst:
        return False
    if modCheckSecond:
        return False
    else:
        return True
