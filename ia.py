""" Module for the IA. """

from grid import Grid
import random

DIFFICULTY = ["dummy", "stonk"]

class Ia():

    def __init__(self, grid, difficulty=DIFFICULTY[0]):
        self.grid = grid
        self.difficulty = difficulty
        if self.difficulty == "dummy":
            self.name = "Kevin"
        else:
            self.name = "Min-Max-Boy"

    def dummy_play(self):
        """ Play randomly """
        return random.choice(self.grid.get_empty)

    @property
    def get_name(self):
        return self.name
