"""
Module representing a game of tic-tac-toe.
"""

from grid import Grid


class Game():

    def __init__(self, begining_player):
        self.grid = Grid()
        self.current_player = begining_player

    def reset(self, begining_player):
        self.grid.reset()
        self.current_player = begining_player

    def is_finished(self):
        return self.full_grid() or self.won()

    def full_grid(self):
        return self.grid.is_full()

    def switch_player(self):
        if self.current_player == "x":
            self.current_player = "o"
        else:
            self.current_player = "x"

    def won(self):
        """
        This code is bad as f*ck there is certainly a way to improve it
        """
        return self.grid.value(1) == self.current_player\
                and self.grid.value(2) == self.current_player\
                and self.grid.value(3) == self.current_player\
            or self.grid.value(4) == self.current_player\
                and self.grid.value(5) == self.current_player\
                and self.grid.value(6) == self.current_player\
            or self.grid.value(7) == self.current_player\
                and self.grid.value(8) == self.current_player\
                and self.grid.value(9) == self.current_player\
            or self.grid.value(1) == self.current_player\
                and self.grid.value(4) == self.current_player\
                and self.grid.value(7) == self.current_player\
            or self.grid.value(2) == self.current_player\
                and self.grid.value(5) == self.current_player\
                and self.grid.value(8) == self.current_player\
            or self.grid.value(3) == self.current_player\
                and self.grid.value(6) == self.current_player\
                and self.grid.value(9) == self.current_player\
            or self.grid.value(1) == self.current_player\
                and self.grid.value(5) == self.current_player\
                and self.grid.value(9) == self.current_player\
            or self.grid.value(3) == self.current_player\
                and self.grid.value(5) == self.current_player\
                and self.grid.value(7) == self.current_player\

    def turn(self, cell_number):
        try:
            self.grid.play(cell_number, self.current_player)
            self.grid.draw_txt()
            return self.is_finished()
        except ValueError:
            print("Wrong drawing or cell number")

    @property
    def get_current_player(self):
        return self.current_player

    @property
    def get_grid(self):
        return self.grid

if __name__ == "__main__":
    g = Game("x")
    g.turn(1)