import numpy as np
import chess

class SerializeBoard:
    def __init__(self, board=None, is_white=None):
        self.board = board
        self.is_white = is_white
        self.bitboard_piece_index = {'P': 0, 
                                     'R': 1,
                                     'N': 2,
                                     'B': 3,
                                     'Q': 4,
                                     'K': 5}

    def _flip_vertical(self, bitboard):
        k1 = int(0x00FF00FF00FF00FF)
        k2 = int(0x0000FFFF0000FFFF)
        bitboard = ((bitboard >>  8) & k1) | ((bitboard & k1) <<  8)
        bitboard = ((bitboard >> 16) & k2) | ((bitboard & k2) << 16)
        bitboard = (bitboard  >> 32)       |  (bitboard       << 32)
        return bitboard

    def _mirror_horizontal(self, bitboard):
        k1 = int(0x5555555555555555)
        k2 = int(0x3333333333333333)
        k4 = int(0x0f0f0f0f0f0f0f0f)
        bitboard = ((bitboard >> 1) & k1) | ((bitboard & k1) << 1);
        bitboard = ((bitboard >> 2) & k2) | ((bitboard & k2) << 2);
        bitboard = ((bitboard >> 4) & k4) | ((bitboard & k4) << 4);
        return bitboard;

    
    def _rotate_180(self, bitboard):
        return self.mirror_horizontal(self.flip_vertical(bitboard))

    def _serialize_castling_rights(self, board, is_white):
        raise NotImplementedError('write this method')

    def serialize_as_bitboards_bitwise(self, board, is_white):
        if is_white is None and self.is_white is None:
            raise ValueError('is_white uninitialized. Initialize self.is_white or pass in function call')

        white_mask = board.occupied_co[chess.WHITE]
        black_mask = board.occupied_co[chess.BLACK]

        bitboards = [
            board.pawns   & white_mask,  # w_pawns
            board.rooks   & white_mask,  # w_rooks
            board.knights & white_mask,  # w_knights
            board.bishops & white_mask,  # w_bishops
            board.queens  & white_mask,  # w_queen
            board.kings   & white_mask,  # w_king
            board.pawns   & black_mask,  # b_pawns
            board.rooks   & black_mask,  # b_rooks
            board.knights & black_mask,  # b_knights
            board.bishops & black_mask,  # b_bishops
            board.queens  & black_mask,  # b_queen
            board.kings   & black_mask,  # b_king
        ]

        # orientate st player is always at bottom of board
        if is_white is False or self.is_white is False:
            for i in range(len(bitboards)):
                bitboards[i] = self._rotate_180(bitboards[i])

        return bitboards
    


board = chess.Board()
board.push(chess.Move.from_uci('e2e4'))
serializer = SerializeBoard()
bitboards = serializer.serialize_as_bitboards_bitwise(board, True)

import sys
sys.path.append('../')
from ext.bitboard_viewer import show_bitboard

for i in bitboards:
    print(end='\n')
    show_bitboard(i)

