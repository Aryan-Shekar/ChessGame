import pygame
import chess
import chess.engine
import os
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
GREEN = (0, 255, 0, 100)  # Transparent green for selection effect
RED = (255, 0, 0)  # Red for checkmate text

# Directory containing the chess piece images
image_dir = 'images'

# Filenames of the chess piece images
piece_images_files = {
    'p': 'Chess_pdt60.png',  # Black Pawn
    'r': 'Chess_rdt60.png',  # Black Rook
    'n': 'Chess_ndt60.png',  # Black Knight
    'b': 'Chess_bdt60.png',  # Black Bishop
    'q': 'Chess_qdt60.png',  # Black Queen
    'k': 'Chess_kdt60.png',  # Black King
    'P': 'Chess_plt60.png',  # White Pawn
    'R': 'Chess_rlt60.png',  # White Rook
    'N': 'Chess_nlt60.png',  # White Knight
    'B': 'Chess_blt60.png',  # White Bishop
    'Q': 'Chess_qlt60.png',  # White Queen
    'K': 'Chess_klt60.png'   # White King
}

# Load images
piece_images = {}
for piece, filename in piece_images_files.items():
    image_path = os.path.join(image_dir, filename)
    image = pygame.image.load(image_path)
    piece_images[piece] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
font = pygame.font.Font(None, 72)  # Font for checkmate text

# Initialize chess board
board = chess.Board()

# Specify the path to Stockfish engine
engine_path = "/Users/aryanshekar/Documents/Python Projects/KyleChessGame/stockfish/stockfish-macos-m1-apple-silicon"
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

selected_square = None
selected_piece = None
moving_piece_pos = None
player_color = chess.WHITE  # Player is always White

def draw_checkmate():
    text = font.render("CHECKMATE!", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)  # Pause to display the message

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            x = chess.square_file(square) * SQUARE_SIZE
            y = (7 - chess.square_rank(square)) * SQUARE_SIZE
            screen.blit(piece_images[piece.symbol()], (x, y))

def ai_move():
    result = engine.play(board, chess.engine.Limit(time=0.5))
    move = result.move
    board.push(move)
    draw_board()
    draw_pieces()
    pygame.display.flip()
    if board.is_checkmate():
        time.sleep(1)
        draw_checkmate()

def handle_mouse_up(pos):
    global selected_square, selected_piece
    if selected_square is not None:
        x, y = pos
        file = x // SQUARE_SIZE
        rank = 7 - (y // SQUARE_SIZE)
        new_square = chess.square(file, rank)
        move = chess.Move(selected_square, new_square)
        if move in board.legal_moves:
            board.push(move)
            draw_board()
            draw_pieces()
            pygame.display.flip()
            ai_move()
        selected_square = None
        selected_piece = None

running = True
while running:
    draw_board()
    draw_pieces()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            file = x // SQUARE_SIZE
            rank = 7 - (y // SQUARE_SIZE)
            square = chess.square(file, rank)
            piece = board.piece_at(square)
            if piece and piece.color == player_color:
                selected_square = square
                selected_piece = piece.symbol()
        elif event.type == pygame.MOUSEBUTTONUP:
            handle_mouse_up(event.pos)

engine.quit()
pygame.quit()
