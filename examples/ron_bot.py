from evaluator.evaluator import Dummy
from min_max.min_max import MinMax
import chess

def main():
    rons_brain = Dummy()
    ron_bot = MinMax(rons_brain)   
    game = None #TODO instantiate chess game
    player_turn = True # player goes first
    while game:
        if player_turn:
            # get user input and update game
            player_turn = False
        else 
            game.update_state(ron_bot.find_best_path[0])
            player_turn = True

if __name__ == "__main__":
    main()