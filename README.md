# ♟️ Chess Bot Game

A Python-based chess game where you play as **White**, and **Stockfish AI** plays as **Black**. The game features smooth animations, draggable pieces, and automatic AI responses.

---

## 🚀 Features
- 🎮 **Play as White** against **Stockfish AI** (Black).
- 📜 **Legal Move Validation** – Only valid moves are allowed.
- ⚡ **Smooth Animations** – Pieces drift smoothly when moved.
- 🎯 **Checkmate Detection** – Displays a **"CHECKMATE!"** message when the game ends.
- 🔄 **Board Orientation** – Always set for the White player.
- 🏆 **AI Opponent** – Uses **Stockfish**, a strong chess engine.

---

## 🛠 Installation

### **Step 1: Install Dependencies**
Ensure you have Python installed (version **3.8+ recommended**).

Run the following command:
```
pip install pygame python-chess
```
Step 2: Download Stockfish
Download Stockfish from the official site:
👉 Stockfish Download
Extract it and note the path to the Stockfish executable.
🔧 Setup
1️⃣ Place the chess piece images in an images folder inside the project:
```
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
```
2️⃣ Set Stockfish Path
Open chess_bot_game.py and update this line with the correct path:
```
engine_path = "/Users/yourusername/path/to/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(engine_path)
```
🎮 How to Play
Run the game:
```
python chess_bot_game.py
```
Click a piece to select it (green highlight appears).
Click a destination square to move it.
AI plays automatically after you move.
Game ends with a checkmate message.
🎛 Controls
✅ Click & Release → Select and move a piece.
✅ Valid moves only → Enforced by game logic.
✅ Automatic AI Moves → Stockfish responds instantly.
🔮 Upcoming Features (To-Do List)
 Add move history tracking.
 Implement undo functionality.
 Allow different AI difficulty levels.
🏆 Credits
Stockfish – AI Chess Engine
Pygame – GUI Framework
python-chess – Chess Logic
📜 License
This project is open-source under the MIT License.

🔗 Need Help?
Feel free to contact me or open an issue! 🚀♟️

This README is now formatted properly and works in both **Jupyter Notebook** and **GitHub**! 🚀 Let me know if you need any refinements! 🎯♟️
Here is a link to some slides about the project:
https://docs.google.com/presentation/d/13eCGOtMv4up1590MPeG0IdN29ug3OfbY6y7-DBbjayc/edit?usp=sharing
