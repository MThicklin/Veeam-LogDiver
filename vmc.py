import re, regex

def vmcCrawl(vmcLog):
    vmcContent = vmcLog.readlines()
    print("Printing Module info...")
    for index,line in enumerate(vmcContent):
        a = re.search('(Module:\s\[[A-Z:]+\\\w.+Veeam.+.exe|Veeam.+.dll)', line)
        b = re.split('(Veeam.+.exe|Veeam.+.dll)', str(a))
        c = re.search('(?:={23})([\w\s-]*)(?:={26})',line)
        if a == None and len(b) == 1:
            if c:
                print("c: ",c)
            else:
                print("\tc line: ",line)
            
        else:
            print("b: ",b)
            print("\tb line: ",line)
            
    #for line in vmcContent:    
        #x = re.search(regex.regexVmcTitles, line)
        #y = re.split(regex.regexVmcTitles, str(x))
        #if y == 'None':
        #    continue
        #else:
        #    print("y: ", y)
