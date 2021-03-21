import chess
import chess.svg

board = chess.Board()
print(board.legal_moves)

svg = chess.svg.piece(chess.Piece.from_symbol("R"))

board = chess.Board()
svg = chess.svg.board(board, size=350)  

f = open("test.svg", "w")
f.write(svg)
f.close()
