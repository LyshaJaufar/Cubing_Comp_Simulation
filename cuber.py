# from bs4 import BeautifulSoup
# import requests
import json

events = ['222', '333', '444', '555', '666', '777',
          '333oh', 'clock', 'minx', 'pyram', 'skewb', 'sq1']

eventsConverted = {
    '222': '2x2',
    '333': '3x3',
    '444': '4x4',
    '555': '5x5',
    '666': '6x6',
    '777': '7x7',
    '333oh': "3x3 OH",
    'clock': 'CLock',
    "minx": "Megaminx",
    'pyram': "Pyraminx",
    "skewb": "Skewb",
    "sq1": "Square-1"
}


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
        url = f"https://www.worldcubeassociation.org/results/rankings/{event}/average"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")

        cuberNames = doc.find_all(class_="name")
        cuberPosition = 1
        for cuberName in cuberNames:
            cuberLink = cuberName.a
            nameSplit = (str(cuberLink).split(">"))
            if (len(nameSplit) > 2):
                cubers[eventNum].append(
                    Cuber(nameSplit[1].split("<")[0], eventsConverted[event], cuberPosition))
                cuberPosition += 1
        eventNum += 1


def populateJsonObj():
    eventNum = 0
    for event in cubers:
        jsonObj['results'].append([])
        for cuber in event:
            jsonObj['results'][eventNum].append({
                "name": cuber.name,
                "event": cuber.event,
                "position": cuber.position,
                "inTeam": cuber.inTeam
            })
        eventNum += 1
    writeToJsonFile()


def writeToJsonFile():
    jsonFile = open("cubers.json", "w")
    jsonFile.write(json.dumps(jsonObj))
    jsonFile.close()


def populateCuberListFromJsonFile():
    file = open('cubers.json')
    data = json.load(file)

    eventNum = 0
    for event in data['results']:
        cubers.append([])
        for cuber in event:
            cubers[eventNum].append(
                Cuber(cuber['name'], cuber['event'], cuber['position']))
        eventNum += 1
    file.close()


populateCuberListFromJsonFile()
# populateCuberList(events)
# populateJsonObj()
