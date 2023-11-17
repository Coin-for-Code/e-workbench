import numpy as np
from numpy.random import randint

# For now just a random players. Player is represented by number
all_players = randint(1,10,10)

# Should be passed through CLI 
number_of_teams = 2

def check_players(players):
    assert isinstance(players, list)
    for player in players:
        assert isinstance(player, SoccerPlayer)

class SoccerPlayer:
    pass

class Team:
    def __init__(self, players):
        check_players(players)
        self.players = players
