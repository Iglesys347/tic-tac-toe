""" Module for the IA. """

from math import inf
from game import Game
import random
import copy

DIFFICULTY = ["dummy", "stonk"]


class Ia():

    def __init__(self, game, drawing, difficulty=DIFFICULTY[0]):
        self.game = game
        self.difficulty = difficulty
        if self.difficulty == "dummy":
            self.name = "Kevin"
        else:
            self.name = "Min-Max-Boy"
        self.drawing = drawing

    def dummy_play(self):
        """ Play randomly """
        return random.choice(self.game.get_grid.get_empty)

    @property
    def get_name(self):
        return self.name

    def min_max_play(self):
        return make_best_move(self.game, self.drawing)

    def play(self):
        if self.name == "Kevin":
            return self.dummy_play()
        else:
            return self.min_max_play()


def make_best_move(game, ia_color):
    # best_score = -inf
    # best_move = None
    # game_copy = copy.deepcopy(game)

    # print(game_copy.get_grid.get_empty)
    # for move in game_copy.get_grid.get_empty:
    #     print(move)
    #     game_copy.play_for_ia(move)
    #     score = minimax(False, ia_color, game_copy)
    #     game_copy.unplay_for_ia()
    #     if (score > best_score):
    #         best_score = score
    #         best_move = move
    # print(best_score, best_move)
    _, best_move = minimax(False, ia_color, game)
    return best_move  # game.play_for_ia(best_move)


def minimax(ai_turn, ia_color, game):
    if game.full_grid():
        return (0, None)
    elif game.won():
        return (1, None) if game.get_current_player is ia_color else (-1, None)

    scores = []
    game_copy = copy.deepcopy(game)
    for move in game_copy.get_grid.get_empty:
        game_copy.play_for_ia(move)
        score, _ = minimax(not ai_turn, switch_player(ia_color),
                           game_copy.switch_player())
        scores.append(score)
        game_copy.unplay_for_ia()
    return (max(scores), move) if ai_turn else (min(scores), move)


def switch_player(player):
    if player == "x":
        return "o"
    else:
        return "x"


if __name__ == "__main__":
    g = Game("x")
    ia = Ia(g, "o", "stonk")
    ia.play()
