import re

regexDate = re.compile('(\[[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}]\s<[0-9]{2,4}>\s\w{4,7})')

VMCSection = re.compile('(?:={24})([\w\s-]*)(?:={26})')

VBRMachineName = re.compile('MachineName:\s(\[[a-zA-Z0-9 \-\_]*\])')

VBRModule = re.compile('(Veeam.Backup.\w+.exe|Veeam.Backup.\w+.dll)')

modDropFirst = re.compile('<re.Match object')
modDropSecond = re.compile('\'>')

regexWarn = re.compile('(Warning|Error|WARN|ERR|isCorrupted=True|>>|absent)+')
regexInfo = re.compile('(Info)+')
regexCliUpd = re.compile('(Warning)\s+(\[ClientUpdate\])')

regexBackupJob = re.compile('(\[Backup\sJob\s(\w)*\])+')
regexBackupId = re.compile('\(([0-9a-z]{8})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{12})\)')
regexJobState = re.compile('(Job\sstate:)')
regexSchedule = re.compile('(Schedule\soptions)\s\((enabled|disabled)\):')
regexAdvanced = re.compile('(Advanced:)\s')
regexLStrip = re.compile('\[([0-9]{2}).([0-9]{2}).([0-9]{4})\s[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s<[0-9]{2,4}>\s\w+\s*==\s\s')

regexLogFileName = re.compile('(?<=\/)\w*(\.\d)*(\.log)')