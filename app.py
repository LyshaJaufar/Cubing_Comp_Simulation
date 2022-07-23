from bs4 import BeautifulSoup
import requests
import re
import random
from team import Team
from cuber import Cuber
from team import teams
import itertools

eventsInit = ['222', '333', '444', '555', '666', '777', '333oh', 'clock', 'minx', 'pyram', 'skewb', 'sq1']
teammates = []
events = []

def main():
    populateTeams()
    winner = tournament(teams)
    print(winner)

def populateTeams():
    for i in range(8):
        teams.append(Team(i + 1))
        teams[i].createTeam()

def compete(team1, team2):
    team1Points = team2Points = 0
    for (cuber1, cuber2) in zip(team1.teammates, team2.teammates):
        team1Points += 1 if cuber1.position < cuber2.position else 0
        team2Points += 1 if cuber2.position < cuber1.position else 0

    winner = team1 if team1Points > team2Points else team2
    return winner

def tournament(teams):
    semiFinalists = []
    finalists = []
    for i in range(0, len(teams) - 1, 2):
        semiFinalists.append(compete(teams[i], teams[i + 1]))

    finalists.append(compete(semiFinalists[0], semiFinalists[1]))
    finalists.append(compete(semiFinalists[2], semiFinalists[3]))

    return compete(finalists[0], finalists[1])

main()