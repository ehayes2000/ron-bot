class GameState:
    def __init__(self, game_state):
        """
            @param game_state: the representation of the gamestate used by the evaluator
            @instance children: list of possible future GameState instances
        """
        self.game_state = game_state
        self.children = []
        