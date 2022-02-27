import re, regex

def topSection(file, topSec):
    fileName = "Top Section for " + str(file) + ".txt"
    secContent = topSec.readlines()
    with open(str(fileName), "w") as output:
        for line in secContent:
            y = re.search(regex.VBRMachineName, str(secContent))
            z = re.search(regex.VBRos, str(secContent))
        print("Machine Name: ", y, " OS: ", z)
        try:
            output.write("{}:\nMachine Name: {}\nOS: {}".format(file,y,z))
        except AttributeError:
            if y:
                z = "Not Found"
            else:
                y = "Not Found"
            output.write("{}:\nMachine Name: {}\nOS: {}".format(file,y,z))
    output.close()