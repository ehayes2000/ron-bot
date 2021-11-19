from evaluator.evaluator import Evaluator
from min_max.game_state import GameState

class MinMax:
    def __init__(self, Evaluator):
        raise NotImplementedError

    def find_best_path(self):
        raise NotImplementedError

    def update_game_tree(self, GameState):
        raise NotImplementedError