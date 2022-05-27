from bs4 import BeautifulSoup
import requests
import re
import random
import cuber, team
from team import Team
from cuber import Cuber

def main():
    if __name__ == '__main__':
        cuber.populateCuberLists()
        populateTeams()

def populateTeams():
    for i in range(8):
        team.teams.append(Team(i + 1))
        team.teams[i].createTeam()

main()