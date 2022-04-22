import re

VBRMachineName = re.compile('MachineName:\s(\[[a-zA-Z0-9 \-\_]*\])')
VBRModule = re.compile('(Veeam.Backup.\w+.exe|Veeam.Backup.\w+.dll)')
VMCSection = re.compile('(?:={23,26})([\w\s-]*)')

Date = re.compile('(\[[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}]\s<[0-9]{2,4}>\s\w{4,7})')

modDropFirst = re.compile('<re.Match object')
modDropSecond = re.compile('\'>')

Warn = re.compile('(Warning|Error|WARN|ERR|isCorrupted=True|>>|absent)+')
CliUpd = re.compile('(Warning)\s+(\[ClientUpdate\])')

BackupJob = re.compile('(\[Backup\sJob\s(\w)*\])+')
BackupId = re.compile('\(([0-9a-z]{8})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{12})\)')
JobState = re.compile('(Job\sstate:)')
Schedule = re.compile('(Schedule\soptions)\s\((enabled|disabled)\):')
Advanced = re.compile('(Advanced:)\s')
LStrip = re.compile('\[([0-9]{2}).([0-9]{2}).([0-9]{4})\s[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s<[0-9]{2,4}>\s\w+\s*==\s\s')

LogFileName = re.compile('(?<=\/)\w*(\.\d)*(\.log)')

wipRegex = re.compile('([a-zA-Z"\s])+:([\w"/\-\s])+')
#This regex is for the inside of the sections for VMC.py