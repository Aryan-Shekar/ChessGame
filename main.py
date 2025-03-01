import pygame
import chess
import chess.engine
import os

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)

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

# Initialize chess board
board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("stockfish")  # Ensure you have Stockfish installed

# Function to draw the board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to draw pieces
def draw_pieces():
    board_fen = board.fen().split(' ')[0]
    rows = board_fen.split('/')
    for row in range(8):
        col = 0
        for char in rows[row]:
            if char.isdigit():
                col += int(char)
            else:
                screen.blit(piece_images[char], (col * SQUARE_SIZE, row * SQUARE_SIZE))
                col += 1

# Function to get square from coordinates
def get_square(x, y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return chess.square(col, 7 - row)

# Function to play AI move
def ai_move():
    result = engine.play(board, chess.engine.Limit(time=0.5))
    board.push(result.move)

# Main game loop
running = True
selected_square = None
while running:
    draw_board()
    draw_pieces()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            square = get_square(x, y)
            if selected_square is None:
                selected_square = square
            else:
                move = chess.Move(selected_square, square)
                if move in board.legal_moves:
                    board.push(move)
                    ai_move()
                selected_square = None

# Quit game
engine.quit()
pygame.quit()
