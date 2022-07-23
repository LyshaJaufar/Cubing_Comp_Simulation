from bs4 import BeautifulSoup
import requests
import re
import random
import json

events = ['222', '333', '444', '555', '666', '777', '333oh', 'clock', 'minx', 'pyram', 'skewb', 'sq1']
cubers = []
jsonObj = {
    "results": [

    ]
}

class Cuber:
    def __init__(self, name, event, position):
        self.name = name
        self.event = event
        self.position = position
        self.inTeam = False

def populateCuberList(events):
    eventNum = 0
    for event in events:
        cubers.append([])
        url = f"https://www.worldcubeassociation.org/results/rankings/{event}/average";
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
                    
        cuberNames = doc.find_all(class_="name") 
        cuberPosition = 1
        for cuberName in cuberNames:  
            cuberLink = cuberName.a
            nameSplit = (str(cuberLink).split(">"))
            if (len(nameSplit) > 2):
                cubers[eventNum].append(Cuber(nameSplit[1].split("<")[0], event, cuberPosition))
                cuberPosition += 1
        eventNum += 1

def populateJsonObj():
    for event in cubers:
        for cuber in event:
            jsonObj['results'].append({
                "name": cuber.name,
                "event": cuber.event,
                "position": cuber.position,
                "inTeam": cuber.inTeam
            })

    writeToJsonFile()

def writeToJsonFile():
    jsonFile = open("cubers.json", "w")
    jsonFile.write(json.dumps(jsonObj))
    jsonFile.close()


populateCuberList(events)
populateJsonObj()
