import numpy as np

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

    # TODO include move count
    # TODO include castling
    # TODO include player colro

    def serialize_as_bitboards(self, board=None, is_white=None):
        if self.board is None and board is None:
            raise ValueError('self.board is uninitialized. set self.board or pass into function call.')
        
        bitboards = np.zeros(shape=(12, 8, 8))
        
        for index, piece in board.piece_map().items():
            piece_str = str(piece)
            bitboard_index = None
            if piece_str not in self.bitboard_piece_index:
                bitboard_index = self.bitboard_piece_index[piece_str.upper()] + 6
            else:
                bitboard_index = self.bitboard_piece_index[piece_str]
            if is_white is not None:
                pass
            bitboards[bitboard_index, index // 8, index % 8] = 1
     
            if self.is_white is not None:
                bitboards = self._flip_by_color(bitboards, self.is_white)
            else:
                bitboards = self._flip_by_color(bitboards, is_white)
        return [bitboards, None, None, None]

    # flib bitboards st the color being played is always on the bottom
    def _flip_by_color(self, bitboards, is_white):
        if not self.is_white and not is_white:
            raise ValueError ('is_white uninitialized. set self.is_white or pass to callee.')
        if is_white:
            for i in range(len(bitboards)):
                bitboards[i] = np.flip(bitboards[i], axis=0)
        return bitboards

    def _flip_vertical(self, bitboard):
        k1 = int(0x00FF00FF00FF00FF)
        k2 = int(0x0000FFFF0000FFFF)
        bitboard = ((bitboard >>  8) & k1) | ((bitboard & k1) <<  8)
        bitboard = ((bitboard >> 16) & k2) | ((bitboard & k2) << 16)
        bitboard = (bitboard  >> 32)       |  (bitboard       << 32)
        return bitboard

    def mirror_horizontal(x):
        k1 = int(0x5555555555555555)
        k2 = int(0x3333333333333333)
        k4 = int(0x0f0f0f0f0f0f0f0f)
        x = ((x >> 1) & k1) | ((x & k1) << 1);
        x = ((x >> 2) & k2) | ((x & k2) << 2);
        x = ((x >> 4) & k4) | ((x & k4) << 4);
        return x;
        
    def serialize_as_bitboards_bitwise(board, is_white=None):
        kings = board.kings
        knights = board.knights
        queens = board.queens  
        pawns = board.pawns
        rooks = board.rooks
        bishops = board.bishops
        white_bitmask = board.occupied_co[0]

serializer = SerializeBoard()
import chess
board = chess.Board()

pawns = board.pawns
bitmask = board.occupied_co[0]
print(pawns & bitmask)

