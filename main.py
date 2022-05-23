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
                if event == "222":
                    cubers2[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "333":
                    cubers3[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "444":
                    cubers4[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "555":
                    cubers5[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "666":
                    cubers6[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "777":
                    cubers7[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "333oh":
                    cubersOH[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "minx":    
                    cubersMega[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "pyram":
                    cubersPyra[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "skewb":
                    cubersSkewb[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "sq1":
                    cubersSquan[cuberPosition] = nameSplit[1].split("<")[0]
                elif event == "clock":
                    cubersClock[cuberPosition] = nameSplit[1].split("<")[0]
                cuberPosition += 1

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
                
            if event == "222":
                teams[i]["2x2"] = cubers2[randomList[counter]]
            elif event == "333":
                teams[i]["3x3"] = cubers3[randomList[counter]]
            elif event == "444":
                teams[i]["4x4"] = cubers4[randomList[counter]]
            elif event == "555":
                teams[i]["5x5"] = cubers5[randomList[counter]]
            elif event == "666":
                teams[i]["6x6"] = cubers6[randomList[counter]]
            elif event == "777":
                teams[i]["7x7"] = cubers7[randomList[counter]]
            elif event == "333oh":
                teams[i]["OH"] = cubersOH[randomList[counter]]
            elif event == "minx":    
                teams[i]["Megaminx"] = cubersMega[randomList[counter]]
            elif event == "pyram":
                teams[i]["Pyraminx"] = cubersPyra[randomList[counter]]
            elif event == "skewb":
                teams[i]["Skewb"] = cubersSkewb[randomList[counter]]
            elif event == "sq1":
                teams[i]["Squan"] = cubersSquan[randomList[counter]]
            elif event == "clock":
                teams[i]["Clock"] = cubersClock[randomList[counter]]
            counter += 1
main()