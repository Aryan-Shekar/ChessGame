Chess Bot Game

Overview

This is a Chess Game built using pygame and python-chess, where the player always plays as White, and Stockfish acts as the AI opponent playing as Black. The game features smooth animations, piece selection highlights, and a checkmate message when the game ends.

Features

Player always plays as White

Stockfish AI as the Black player

Smooth animations for piece movement

Visual highlighting for selected pieces

Automatic AI move execution after player's move

Checkmate detection and message display

Requirements

Dependencies

Make sure you have the following installed:

pygame

python-chess

Stockfish (Download from Stockfish Chess)

Installation

Clone this repository:

git clone https://github.com/your-repo/chess-bot-game.git
cd chess-bot-game

Install dependencies:

pip install pygame chess

Ensure Stockfish is downloaded and placed correctly.

How to Run

Ensure the Stockfish engine path is correct in the script:

engine_path = "/path/to/stockfish"

Run the game:

python chess_game.py

Controls

Click on a piece to select it (green highlight appears)

Drag and drop or click a destination square to move

The AI automatically plays after your move

Checkmate

When checkmate occurs, a red "CHECKMATE!" message is displayed for 3 seconds before ending the game.

Notes

Ensure that pygame is installed correctly.

The chess pieces should be stored in an images/ folder.

Modify engine_path in the script to match your Stockfish installation.

License

This project is open-source. Feel free to modify and improve it!

Enjoy playing Chess against Stockfish! ♟️🚀
