import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    return print(root)

with open("job.xml") as job:
    parseXML(job)