""" Main program. """

from game import Game
from ia import Ia


def get_other_drawing(drawing):
    if drawing == "x":
        return "o"
    else:
        return "x"


f = open("welcome.txt", "r")
print(f.read())

print("Do you want to play with a friend (1) ? If you don't have friend you can play against our friendly IA ;) (2)")
print("Please type 1 or 2 :")
choice = input()

winner = None

if choice == "1":
    print("I'm glad you have friend to play with !")
    print("1st player, please choose beteween x and o (simply type x or o)")
    first_player = input()

    game = Game(first_player)
    game_finished = False

    while not game_finished:
        game_finished = "0"
        while game_finished == "0":
            print(
                f"Player {game.get_current_player} please enter the cell number in which you want to play (you can show the diffent cell numbers by typing '?'")
            comm = input()
            if comm == "?":
                game.get_grid.display_cells_numbers()
            else:
                game_finished = game.turn(int(comm))
        game.switch_player()
else:
    print("Which IA do you want to chalenge :")
    print("    1 : Kevin, a dummy IA (we don't even know if he knows the rules)")
    print("    2 : Min-Max-Boy, he maybe have a stange name but this guy is definitively very strong at tic-tac-toe")
    if input() == "1":
        ia_kind = "dummy"
    else:
        ia_kind = "stonk"
    print("Good choice !")
    print("Do you want to start or let the IA start ? (type 1 for starting, 2 to let the IA start).")
    if input() == "1":
        ia_starting = False
    else:
        ia_starting = True
    print("Finally, do you want the x or the o ? (type 'x' or 'o')")
    player_drawing = input()
    ia_drawing = get_other_drawing(player_drawing)

    if ia_starting:
        game = Game(ia_drawing)
    else:
        game = Game(player_drawing)
    game_finished = False

    ia = Ia(game, ia_drawing, ia_kind)

    while not game_finished:
        if game.current_player == player_drawing:
            game_finished = "0"
            while game_finished == "0":
                print(
                    f"Player {game.get_current_player} please enter the cell number in which you want to play (you can show the diffent cell numbers by typing '?'")
                comm = input()
                if comm == "?":
                    game.get_grid.display_cells_numbers()
                else:
                    game_finished = game.turn(int(comm))
        else:
            print(f"{ia.get_name} : Let me think...")
            game_finished = game.turn(ia.play())
        if game.won():
            winner = game.get_current_player
        game.switch_player()

if winner:
    print(f"Well done {winner} you won !")
else:
    print("It's a draw !")
