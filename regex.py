regexSection = '={67}'
regexDate = '(\[[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}]\s<[0-9]{2,4}>\s\w{4,7})'
regexVBRFilePath = '([CDEF]:\\\Program\sFiles\\\Veeam\\\Backup\sand\sReplication\\\Backup\\\)'
regexFileVersion = '(File\sVersion\s\[([0-9]{2}.[0-9].[0-9].[0-9]{1,4})\])'
regexComments = '(Comments)\s(\[Private\sFix\s)(KB[0-9]{8},)(CF-[0-9]{2})'

jobSection = '======================== CURRENT JOBS =========================='
VBRMachinenameLine = 'MachineName:\s\[([a-z A-Z 0-9]*)\],\sOS:\s\[[a-z A-Z 0-9(.)\]]*'
VBRMachineName = '\[([a-z A-Z 0-9]*)\]'
VBRos = 'OS:\s\[[a-z A-Z 0-9(.)\]]*'
regexWarn = '(Warning|Error)+'
regexInfo = '(Info)+'
regexCliUpd = '(Warning)\s\s\s\s\s\s(\[ClientUpdate\])'

regexBackupJob = '(\[Backup\sJob\s(\w)*\])+'
regexBackupId = '\(([0-9a-z]{8})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{4})-([0-9a-z]{12})\)'
regexJobState = '(Job\sstate:)'
regexSchedule = '(Schedule\soptions)\s\((enabled|disabled)\):'
regexAdvanced = '(Advanced:)\s'
regexLStrip = '\[([0-9]{2}).([0-9]{2}).([0-9]{4})\s[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s<[0-9]{2,4}>\s\w+\s*==\s\s'