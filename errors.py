import json

try:
    with open("errors.json") as errorFile:
        errorList = json.load(errorFile)
finally:
    print("Errors.json can't be found!!")