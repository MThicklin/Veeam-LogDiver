import sys
from vmc import vmcCrawl
from clean import cleaner
from stow import stower
from stow import stow4me
from logWrite import logWriter

logName = ""

if sys.argv[1] == "clean":
    print("Cleaning all Log diver txt files.")
    cleaner(0)

if sys.argv[1] == "nuke":
    print("Nuclear Option Activated...")
    print("ALL NON/-LOGDIVER FILES WILL BE DELETED...")
    cleaner(1)

if sys.argv[1] == "stow":
    folderName = input("Name the folder to stow the files in: ")
    stower(folderName)

if sys.argv[1] == "stow4me":
    stow4me()

if sys.argv[1] == "vmc":
    try:
        with open("VMC.log", "r") as vmcLog:
            vmcCrawl(vmcLog)
        vmcLog.close()
    except FileNotFoundError:
        print(
            "VMC.log Not found."
        )

if sys.argv[1] == "crawl":
    logWriter()