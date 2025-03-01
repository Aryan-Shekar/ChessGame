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
GREEN = (0, 255, 0, 150)  # Transparent green for selection effect

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

# Specify the path to Stockfish engine
engine_path = "/Users/aryanshekar/Documents/Python Projects/KyleChessGame/stockfish/stockfish-macos-m1-apple-silicon"
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

selected_square = None
selected_piece_symbol = None
piece_position = None

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # Draw green highlight if a piece is selected
    if selected_square is not None:
        highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        highlight_surface.fill(GREEN)
        screen.blit(highlight_surface, (chess.square_file(selected_square) * SQUARE_SIZE, (7 - chess.square_rank(selected_square)) * SQUARE_SIZE))

def draw_pieces():
    pieces_to_draw = []
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            x = chess.square_file(square) * SQUARE_SIZE
            y = (7 - chess.square_rank(square)) * SQUARE_SIZE
            pieces_to_draw.append((piece.symbol(), x, y, square))
    
    # Draw all pieces, ensuring captured pieces do not overlay the moving piece
    for symbol, x, y, square in sorted(pieces_to_draw, key=lambda p: p[3] == selected_square):
        screen.blit(piece_images[symbol], (x, y))

def get_square(x, y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return chess.square(col, 7 - row)

def animate_move(start_pos, end_pos, piece):
    frames = 10
    delta_x = (end_pos[0] - start_pos[0]) / frames
    delta_y = (end_pos[1] - start_pos[1]) / frames

    for i in range(frames):
        draw_board()
        draw_pieces()
        screen.blit(piece_images[piece], (start_pos[0] + delta_x * i, start_pos[1] + delta_y * i))
        pygame.display.flip()
        time.sleep(0.02)

def ai_move():
    result = engine.play(board, chess.engine.Limit(time=0.5))
    move = result.move
    board.push(move)

def handle_mouse_down(pos):
    global selected_square, selected_piece_symbol, piece_position
    x, y = pos
    square = get_square(x, y)
    piece = board.piece_at(square)
    if piece:
        selected_square = square
        selected_piece_symbol = piece.symbol()

def handle_mouse_up(pos):
    global selected_square, selected_piece_symbol, piece_position
    if selected_square is not None:
        x, y = pos
        new_square = get_square(x, y)
        move = chess.Move(selected_square, new_square)
        if move in board.legal_moves:
            board.push(move)
            ai_move()
        selected_square = None
        selected_piece_symbol = None

def handle_mouse_motion(pos):
    pass

running = True
while running:
    draw_board()
    draw_pieces()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_down(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            handle_mouse_up(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            handle_mouse_motion(event.pos)

engine.quit()
pygame.quit()
