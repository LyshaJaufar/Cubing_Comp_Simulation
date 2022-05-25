from bs4 import BeautifulSoup
import requests
import re
import random

cubers2 = {}
cubers3 = {}
cubers4 = {}
cubers5 = {}
cubers6 = {}
cubers7= {}
cubersOH = {}
cubersClock = {}
cubersMega = {}
cubersPyra = {}
cubersSkewb = {}
cubersSquan = {}

events = ['222', '333', '444', '555', '666', '777', '333oh', 'clock', 'minx', 'pyram', 'skewb', 'sq1']
eventList = [cubers2, cubers3, cubers4, cubers5, cubers6, cubers7, cubersOH, cubersMega, cubersPyra, cubersSquan, cubersSkewb]
teams = []

def main():
    if __name__ == '__main__':
        populateEventLists()
        createTeam()


               
def populateEventLists():
    for event in events:
            
        url = f"https://www.worldcubeassociation.org/results/rankings/{event}/average";
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
            
        cuberNames = doc.find_all(class_="name") 
        i = 1
        cuberPosition = 1
        for cuberName in cuberNames:  
            cuberLink = cuberName.a
            nameSplit = (str(cuberLink).split(">"))
            if (len(nameSplit) > 2):
                for i in range(len(eventList)):
                    if event == eventList[i]:
                        print(eventList[i])
                        (eventList[i])[cuberPosition] = nameSplit[1].split("<")[0]

                cuberPosition += 1
    print(eventList[0])


def createTeam():
    
    for i in range(8):
        teams.append({})
        counter = 0
        for event in events:
            randomList = []
            for j in range(len(cubers3)):
                n = random.randint(1, len(cubers3))
                while n in randomList:
                    n = random.randint(1, len(cubers3))
                randomList.append(n)

            # teams[i]["2x2"] = {eventList[0][randomList[counter]]}
                
            if event == "222":
                teams[i]["2x2"] = {cubers2[randomList[counter]] : randomList[counter]}
            elif event == "333":
                teams[i]["3x3"] = {cubers3[randomList[counter]] : randomList[counter]}
            elif event == "444":
                teams[i]["4x4"] = {cubers4[randomList[counter]] : randomList[counter]}
            elif event == "555":
                teams[i]["5x5"] = {cubers5[randomList[counter]] : randomList[counter]}
            elif event == "666":
                teams[i]["6x6"] = {cubers6[randomList[counter]] : randomList[counter]}
            elif event == "777":
                teams[i]["7x7"] = {cubers7[randomList[counter]] : randomList[counter]}
            elif event == "333oh":
                teams[i]["OH"] = {cubersOH[randomList[counter]] : randomList[counter]}
            elif event == "minx":    
                teams[i]["Megaminx"] = {cubersMega[randomList[counter]] : randomList[counter]}
            elif event == "pyram":
                teams[i]["Pyraminx"] = {cubersPyra[randomList[counter]] : randomList[counter]}
            elif event == "skewb":
                teams[i]["Skewb"] = {cubersSkewb[randomList[counter]] : randomList[counter]}
            elif event == "sq1":
                teams[i]["Squan"] = {cubersSquan[randomList[counter]] : randomList[counter]}
            elif event == "clock":
                teams[i]["Clock"] = {cubersClock[randomList[counter]] : randomList[counter]}
            counter += 1

    print(teams[0])
main()