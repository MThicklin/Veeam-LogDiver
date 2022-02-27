import re, regex

def vmcCrawl(vmcLog):
    vmcContent = vmcLog.readlines()
    for index, line in enumerate(vmcContent):
        count = index + 1
        x = re.search(regex.regexVmcTitles, str(line))
        y = re.split(regex.regexVmcTitles, str(x))
        if y[0] == 'None':
            print("{}".format(line))
        if y[0] != 'None':
            print("Line {}:\n{}".format(count,y))
            continue
                        