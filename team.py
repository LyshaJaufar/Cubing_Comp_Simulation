import cuber
from cuber import events
from cuber import cubers
import random

teams = []

class Team:
    def __init__(self, idNum):
        self.size = 12      # 1 cuber per event, for 12 events
        self.idNum = idNum
        self.teammates = {}

    def createTeam(self):
        # Randomise rankings for each event
        for event in events:       
            n = random.randint(1, len(cubers[0]))
            found = False

            while (found == False):
                for i in range(len(cubers[events.index(event)])):
                    if (cubers[events.index(event)][i].position == n):
                        if (cubers[events.index(event)][i].inTeam == True):
                            n += random.randint(1, len(cubers[0]))
                            break

                        self.teammates[event] = cubers[events.index(event)][i]
                        cubers[events.index(event)][i].inTeam = True
                        cubers[events.index(event)][i].team = self.idNum
                        found = True