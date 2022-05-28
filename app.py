from bs4 import BeautifulSoup
import requests
import re
import random
from team import Team
from cuber import Cuber
from team import teams
import itertools
from flask import Flask, render_template

teammates = []
app = Flask(__name__)

@app.route("/")
def main():
    populateTeams()
    winner = tournament(teams)

    for key, value in winner.teammates.items():
        teammates.append(key.name)
    return render_template("index.html", name=teammates[0], name2=teammates[1], name3=teammates[2],
    name4=teammates[3], name5=teammates[4], name6=teammates[5], name7=teammates[6], name8=teammates[7],
    name9=teammates[8], name10=teammates[9], name11=teammates[10], name12=teammates[11])

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



