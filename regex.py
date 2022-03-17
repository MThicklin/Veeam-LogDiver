import re

regexDate = '(\[[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}]\s<[0-9]{2,4}>\s\w{4,7})'
regexVBRFilePath = ''
regexVBRModType = '(File\sVersion\s\[([0-9]{2}.[0-9].[0-9].[0-9]{1,4})\])'
regexComments = '(Comments)\s(\[Private\sFix\s)(KB[0-9]{8},)(CF-[0-9]{2})'

VBRMachineName = 'MachineName:\s(\[[a-zA-Z0-9 \-\_]*\])'
VBRos = 'OS:\s([a-zA-Z0-9 (.)\[\]])+'
regexWarn = '(Warning|Error|WARN|ERR|isCorrupted=True)+'
regexInfo = '(Info)+'
regexCliUpd = '(Warning)\s\s\s\s\s\s(\[ClientUpdate\])'

regexBackupJob = '(\[Backup\sJob\s(\w)*\])+'
regexBackupId = '\(([0-9a-z]{8})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{12})\)'
regexJobState = '(Job\sstate:)'
regexSchedule = '(Schedule\soptions)\s\((enabled|disabled)\):'
regexAdvanced = '(Advanced:)\s'
regexLStrip = '\[([0-9]{2}).([0-9]{2}).([0-9]{4})\s[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s<[0-9]{2,4}>\s\w+\s*==\s\s'

regexLogFileName = '(?<=\/)\w*(\.\d)*(\.log)'

regexVmcTitles = re.compile("(?:={23})([\w\s-]*)(?:={26})")

regexVmcTitles2 = re.compile("([\w\s-]*)")