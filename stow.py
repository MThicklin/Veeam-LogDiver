import os
import shutil

def stower(folderName):
    filesMoved = 0
    srcPath = os.getcwd()
    destPath = os.path.join(srcPath, folderName)
    try:
        os.mkdir(destPath)
    except FileExistsError:
        pass
        
    for file in os.listdir(srcPath):
        if file.endswith(".txt") or file.endswith(".log"):
            shutil.move(srcPath +"\\"+file, destPath +"\\"+ file)
            filesMoved += 1
    print("{} files stowed away in {}".format(filesMoved, folderName))


def stow4me():
    folderList = []
    folderCount = 0
    for folders in os.listdir(os.getcwd()):
        isdir = os.path.isdir(folders)
        if isdir and folders != '__pycache__':
            print("folders: ", folders)
            folderList.append(folders)
            folderCount += 1
        else:
            continue
    print('Found {} folders.'.format(folderCount))
    for folderCounter, folder in enumerate(folderList):
        print("{} : {}".format(folderCounter, folder))
    folderNum = input("choose folder number to stow: ")
    if int(folderNum) > len(folderList):
        print("Number enter exceeds the list...")
    else:
        stower(folderList[int(folderNum)])