import math
import random
from typing import Any

# base player class
class Player:
    def __call__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move
    def get_move(self, game):
        pass

# use inheritance to create a random computer and human player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

