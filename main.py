from bs4 import BeautifulSoup
import requests
import re



def main():
    if __name__ == '__main__':
        url = f"https://www.worldcubeassociation.org/results/records?show=history"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        
        cuberNames = doc.find_all(class_="name")
        
        for cuberName in cuberNames:
            link = cuberName.a
            split = (str(link).split(">"))
            if (len(split) > 2):
                print(split[1].split("<")[0])

main()