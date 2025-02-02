import json

with open("config.json", "r") as j:
    mydata = json.load(j)

    print(mydata["host"])