Chess Bot Game
A Python-based chess game where you play as White, and Stockfish AI plays as Black. The game features smooth animations, draggable pieces, and automatic AI responses.

Features
🎮 Play as White against Stockfish AI (Black).
📜 Legal Move Validation – Only valid moves are allowed.
⚡ Smooth Animations – Pieces drift smoothly when moved.
🎯 Checkmate Detection – Displays a "CHECKMATE!" message when the game ends.
🔄 Board Orientation – Always set for the White player.
🏆 AI Opponent – Uses Stockfish, a strong chess engine.
Installation
1️⃣ Install Dependencies
Ensure you have Python installed (version 3.8+ recommended).

Install required libraries:

sh
Copy
Edit
pip install pygame python-chess
2️⃣ Download Stockfish
Download Stockfish from the official site: Stockfish Download
Extract it and note the path to the Stockfish executable.
Setup
Place the chess piece images in an images folder:

Copy
Edit
images/
├── Chess_pdt60.png
├── Chess_rdt60.png
├── Chess_ndt60.png
├── Chess_bdt60.png
├── Chess_qdt60.png
├── Chess_kdt60.png
├── Chess_plt60.png
├── Chess_rlt60.png
├── Chess_nlt60.png
├── Chess_blt60.png
├── Chess_qlt60.png
├── Chess_klt60.png
Set Stockfish Path Update the following line in chess_bot_game.py to match your Stockfish path:

python
Copy
Edit
engine_path = "/Users/yourusername/path/to/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(engine_path)
How to Play
Run the game:
sh
Copy
Edit
python chess_bot_game.py
Click a piece to select it (green highlight).
Click a destination square to move it.
AI plays automatically after you move.
Game ends with a checkmate message.
Controls
Click & Release → Select and move a piece.
Valid moves only → Enforced by game logic.
Automatic AI Moves → Stockfish responds instantly.
Upcoming Features (To-Do)
 Add move history tracking.
 Implement undo functionality.
 Allow different AI difficulty levels.
Credits
Stockfish – AI Chess Engine
Pygame – GUI Framework
python-chess – Chess Logic
License
This project is open-source under the MIT License.

Let me know if you need any changes! 🚀♟️
