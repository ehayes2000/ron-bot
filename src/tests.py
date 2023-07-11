"""
TODO
Define a set of endgame positions with easy evaluation. 
Test evaluation and minimax on these positions.
Write benchmark for minimax
"""

# Mates: 
    # k7/8/K2R4/8/8/8/8/8 w - - 0 1
    # ^ white to move mate in one (simple) -> Rd8# 
    # d6d8

    # k7/8/K2R4/8/8/8/8/8 b - - 0 1
    # ^ black to move lose mate in two (simple) -> Kb8 Rc6 Ka8 Rc8#
    # a8b8 d6c6 b8a8 c6c8


    # KR6/PP6/8/3n4/8/8/8/7k b - - 0 1
    # ^ black to move mate in one (simple) -> Nc7#
    # d5c7

    # k1r5/pp6/8/3NQ3/5B2/7K/8/8 w - - 0 1 
    # ^ white to move mate in 2 (simple) -> Qb8 Rxb8 Nc7#
    # e5b8 c8b8 d5c7

    # r4r1k/ppqn2bp/6p1/2BQNb2/2B2P2/8/PP4PP/2KR3R w - - 3 20
    # ^ white to move mate in 2 (complex) -> Qg8+ Rxg8 Nf7#
    # d5g8 f8g8 e5f7

# Tactics; 
    # Skewers:
        # 1k6/8/8/8/1r6/4K2R/8/8 b - - 0 1
        # ^ black to move and win a rook (simple) -> Rb3 + K(anywhere) Rxh3
        # b4b3 e3* b3h3

        # 1K6/4r3/8/8/4k3/8/8/1R6 w - - 0 1
        # white to move and win a rook (simple) -> Re1+ k(anywhere) Rxe7 
        # b1e1 e4* e1e7

    # Forks:
        # 8/8/1B5K/8/8/8/8/3r3k b - - 0 1
        # ^ black to move and win a bishop (simple) -> Rd6+ K(anywhere) Rxb6
        # d1d6 h6* d6b6
    
        # 8/8/3r1k2/8/8/R5N1/8/7K w - - 0 1
        # ^ white to move and win an exchange (simple) -> Ne4+ K(e*) Nxd6 Kxd6
        # g3e4 f6e* e4d6 e*d6


import unittest
import chess
from src.minimax import minimax

class TestMates(unittest.TestCase):   
    def test_mate_1(self):
        board = chess.Board("k7/8/K2R4/8/8/8/8/8 w - - 0 1")
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("d6d8"))
    
    def test_mate_2(self):
        board = chess.Board("k7/8/K2R4/8/8/8/8/8 b - - 0 1")
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("a8b8"))
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("d6c6"))
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("b8a8"))
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("c6c8"))

    def test_mate_3(self):
        board = chess.Board("KR6/PP6/8/3n4/8/8/8/7k b - - 0 1")
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("d5c7"))

    # e5b8 c8b8 d5c7
    def test_mate_4(self):
        board = chess.Board("k1r5/pp6/8/3NQ3/5B2/7K/8/8 w - - 0 1")
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("e5b8"))
        board.push(move)
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("c8b8"))
        board.push(move)
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("d5c7"))

    def test_mate_5(self):
        board = chess.Board("r4r1k/ppqn2bp/6p1/2BQNb2/2B2P2/8/PP4PP/2KR3R w - - 3 20")
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("d5g8"))
        board.push(move)
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("f8g8"))
        board.push(move)
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("e5f7"))


class TestSkewers(unittest.TestCase):
    def test_skewer_1(self):
        board = chess.Board("1k6/8/8/8/1r6/4K2R/8/8 b - - 0 1")
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("b4b3"))
        board.push(move)
        _, move = minimax(board, 3, True)
        self.assertEqual(str(move)[:2], "e3")
        board.push(move)
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("b3h3"))

    def test_skewer_2(self):
        board = chess.Board("1K6/4r3/8/8/4k3/8/8/1R6 w - - 0 1")
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("b1e1"))
        board.push(move)
        _, move = minimax(board, 3, False)
        self.assertEqual(str(move)[:2], "e4")
        board.push(move)
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("e1e7"))
        #b1e1 e4* e1e7

class TestForks(unittest.TestCase):
    def test_fork_1(self):
        board = chess.Board("8/8/1B5K/8/8/8/8/3r3k b - - 0 1")
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("d1d6"))
        board.push(move)
        _, move = minimax(board, 3, True)
        self.assertEqual(str(move)[:2], "h6")
        board.push(move)
        _, move = minimax(board, 3, False)
        self.assertEqual(move, chess.Move.from_uci("d6b6"))

    def test_fork_1(self):
        board = chess.Board("8/8/3r1k2/8/8/R5N1/8/7K w - - 0 1")
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("g3e4"))
        board.push(move)
        _, escapeCheck = minimax(board, 3, False)
        self.assertEqual(str(escapeCheck)[:3], "f6e")
        board.push(escapeCheck)
        _, move = minimax(board, 3, True)
        self.assertEqual(move, chess.Move.from_uci("e4d6"))
        _, move = minimax(board, 3, False)
        correctMove = str(escapeCheck)[:2] + "d6"
        self.assertEqual(move, chess.Move.from_uci(correctMove))
        # g3e4 f6e* e4d6 e*d6