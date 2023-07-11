from chess.engine import Cp, Mate
import math
import chess

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
            return Cp(-99999)
        else:
            return Cp(99999)
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
    
def minimax(board, depth, maximizing_player, alpha=Cp(-math.inf), beta=Cp(math.inf)): 
    if depth == 0 or board.is_checkmate() or board.legal_moves.count() == 0:
        print((5- depth) * "  ", "^",evaluate(board), end="\n")
        return evaluate(board), None
    if maximizing_player:
        best_score, best_move = Cp(-math.inf), None
        for move in board.legal_moves:
            board.push(move)
            print((6 - depth) * "  ", move)
            score, _ = minimax(board, depth - 1, False)
            board.pop()
            if score > beta:
                break
            alpha = max(alpha, score)
           
            if score > best_score:
                best_score, best_move = score, move
        return best_score, best_move    
    else:
        best_score, best_move = Cp(math.inf), None
        for move in board.legal_moves:
            board.push(move)
            print((6 - depth) * "  ", move)
            score, _ = minimax(board, depth - 1, True)
            board.pop()
            if score < alpha:
                break
            beta = min(beta, score)
            if score < best_score:
                best_score, best_move = score, move
    
        return best_score, best_move
