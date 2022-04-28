import re

VBRMachineName = re.compile('MachineName:\s(\[[a-zA-Z0-9 \-\_]*\])')
VBRModule = re.compile('(Veeam.Backup.\w+.exe|Veeam.Backup.\w+.dll)')

VMCSection = re.compile('(?:={23,26})([\w\s-]*)')
VMCinnerSection = re.compile('(HostID:|ProxyID:|PlatformId:|ProtectionGroupID:|Proxy types:)+')

lStrip = re.compile('(\[[0-9]{2}.+[0-9]{4}\s([0-9]{2}:)+[0-9]{2}]\s<[0-9]{2,4}>\s\w{4,7})\s*')

modDropFirst = re.compile('<re.Match object')
modDropSecond = re.compile('\'>')

Warn = re.compile('(Warning|Error|WARN|ERR|isCorrupted=True|>>|absent)+')
CliUpd = re.compile('(Warning)\s+(\[ClientUpdate\])')

LogFileName = re.compile('(?<=\/)\w*(\.\d)*(\.log)')