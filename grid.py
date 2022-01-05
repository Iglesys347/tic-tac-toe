"""
Module representing the grid of the tic-tac-toe.
"""
from itertools import product

CELLS_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Grid():
    """
    The cells numerotation is pesented as follow :
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    """

    def __init__(self):
        self.size = 3
        self.cells = dict()
        for elt in CELLS_NUMBERS:
            self.cells[elt] = " "
        self.empty = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.last_move = None

    def reset(self):
        self.cells = [[" "] * self.size] * self.size
        self.empty = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def play(self, number, drawing):
        if number in CELLS_NUMBERS and self.is_empty(number):
            self.last_move = number
            self._change_cell(number, drawing)
            self.empty.remove(number)
        else:
            raise(ValueError)

    def unplay(self):
        """ Remoove last moove. """
        self._change_cell(self.last_move, " ")
        self.empty.append(self.last_move)

    def is_empty(self, number):
        return number in self.empty

    @property
    def get_empty(self):
        return self.empty

    def _change_cell(self, number, drawing):
        self.cells[number] = drawing

    @property
    def get_cells(self):
        return self.cells

    def draw_txt(self):
        print(f" {self.value(1)} | {self.value(2)} | {self.value(3)}")
        print(f"---+---+---")
        print(f" {self.value(4)} | {self.value(5)} | {self.value(6)}")
        print(f"---+---+---")
        print(f" {self.value(7)} | {self.value(8)} | {self.value(9)}")

    def is_full(self):
        return not " " in self.cells.values()

    def value(self, number):
        return self.cells[number]

    def display_cells_numbers(self):
        print(" 1 | 2 | 3")
        print("---+---+---")
        print(" 4 | 5 | 6")
        print("---+---+---")
        print(" 7 | 8 | 9")


if __name__ == "__main__":
    """ For testing purpose. """
    g = Grid()
    #g.play(5, "x")
    for i in range(1, 10):
        g.play(i, "x")
    g.draw_txt()
    print(g.is_full())
