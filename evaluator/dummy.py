from evaluator.evaluator import Evaluator
from random import random

class Dummy(Evaluator):
    def __init__(self):
        pass
        
    def evaluate(self, game_state) -> float:
        return random()