import numpy as np
from scipy.ndimage.interpolation import shift

bitboard_map = {'P': 0,
                'N': 1,
                'B': 2,
                'Q': 3,
                'K': 4,
                'R': 5}

def serialize_board(board, is_white):
    bitboards_2d = _get_bitboards_2d(board)
    castling_rights = _get_castling_rights(board)
    
    if not is_white:
        for i in range(len(bitboards_2d)):
            bitboards_2d[i] = _rotate_180(bitboards_2d[i])
        castling_rights = _rotate_180(castling_rights)

    features = np.empty(shape=0, dtype=bool)
    for bitboard in bitboards_2d:
        features = np.append(features, bitboard.reshape(64))
    features = np.append(features, castling_rights.reshape(4))
    features = np.append(features, board.turn)
    return features
    
def _get_castling_rights(board):
   return np.array([[board.has_kingside_castling_rights(chess.WHITE),
                     board.has_queenside_castling_rights(chess.WHITE)],
                    [board.has_kingside_castling_rights(chess.BLACK),
                     board.has_queenside_castling_rights(chess.BLACK)]],
                    dtype=bool)

def _get_bitboards_2d(board):
    bitboards = [np.zeros(shape=(8, 8), dtype=bool) for i in range(12)]
  
    for index, piece in board.piece_map().items():
        board_index = None
        if str(piece) in bitboard_map:
            board_index = bitboard_map[str(piece)]
        else:
            board_index = bitboard_map[str(piece).upper()] + 6
        bitboards[board_index][7 - (index // 8), 7 - (index % 8)] = True

    return bitboards

def _rotate_180(bitboard):
    return np.rot90(np.rot90(bitboard)[0])
    