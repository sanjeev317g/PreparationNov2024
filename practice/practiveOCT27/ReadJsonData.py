import json

def readJsonData():
    with open("practice\practiveOCT27\data.json", "r") as file:
        data = json.load(file)
        print(data["skills"])

readJsonData()

