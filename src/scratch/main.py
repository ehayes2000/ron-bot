
import chess
import chess.svg
from IPython.display import SVG, display
from chess.engine import Cp
import math

def evaluate(position): 
    """
        parameters:
            position: chess.Board
        returns:
            score: int 

        a simple evaluation function that returns a score based soley on piece value
        p=100, N=300, B=300, R=500, Q=900, K=0
        """
    if position.is_checkmate():
        if position.turn is chess.WHITE:
            return Cp(-9999)
        else:
            return Cp(9999)
    piece_values = {
        'p': -100,
        'n': -300,
        'b': -300,
        'r': -500,
        'q': -900,
        'P': 100,
        'N': 300,
        'B': 300,
        'R': 500,
        'Q': 900,
    }
    score = 0
    for i in position.__str__():
        if i in piece_values:
            score += piece_values[i]    
    return Cp(score)



def minimax(board, depth, maximizing_player): 
    if depth == 0 or board.is_checkmate():
        return evaluate(board), None
    if maximizing_player:
        best_score, best_move = Cp(-math.inf), None
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax(board, depth - 1, False)
            board.pop()
            if score > best_score:
                best_score, best_move = score, move
        return best_score, best_move    
    else:
        best_score, best_move = Cp(math.inf), None
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax(board, depth - 1, True)
            board.pop()
            if score < best_score:
                best_score, best_move = score, move
        return best_score, best_move



def main():
    board = chess.Board()
    display(SVG(chess.svg.board(board=board)))
  
    board = chess.Board()
    print(board)
    while not board.is_game_over():
        _, move = minimax(board, 3, True)
        board.push(move)
        chess.svg.board(board=board, size=400)
if __name__ == "__main__":
    main()