from bs4 import BeautifulSoup
import requests
import re

cubers = {}


def main():
    if __name__ == '__main__':
        url = f"https://www.worldcubeassociation.org/results/rankings/333/average";
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        
        cuberNames = doc.find_all(class_="name")
        cuberPsts = doc.find_all(class_="pos")
        
        i = 1
        for cuberName in cuberNames:
            cuberLink = cuberName.a
            nameSplit = (str(cuberLink).split(">"))
            if (len(nameSplit) > 2):
                cubers[int(cuberPsts[i].string)] = nameSplit[1].split("<")[0]
                i += 1

        print(cubers)
                

main()