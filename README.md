# 🎮 Connect-4
A classic Connect Four game implementation with a twist - built on a 5x4 board using Python and Pygame!

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
## 🎯 About
Connect-4 is a two-player connection game where players take turns dropping colored discs into a vertically suspended grid. This implementation features a unique 5x4 board configuration, providing a fresh take on the classic game. Built with Pygame, it offers smooth graphics, sound effects, and an intuitive user interface.
## ✨ Features
- **Custom Board Size**: 5 columns × 4 rows grid for faster gameplay
- **Two-Player Mode**: Play against a friend on the same computer
- **Visual Feedback**: Smooth animations and clear disc placement
- **Audio Effects**: Engaging sound effects for moves and wins
- **Clean UI**: Intuitive interface with custom fonts and graphics
- **Game Logic**: Smart win detection for horizontal, vertical, and diagonal connections
## 🚀 Installation
### Prerequisites
- Python 3.7 or higher
- pip package manager
### Setup Instructions
1. **Clone the repository**
```bash
git clone https://github.com/Eradboi/Connect-4.git
cd Connect-4
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Run the game**
```bash
python main.py
```
## 🎲 How to Play
1. Launch the game by running `main.py`
2. Player 1 (Red) goes first
3. Click on a column to drop your disc
4. Players alternate turns
5. First player to connect 4 discs in a row wins!
## 📖 Game Rules
- Players take turns dropping one disc per turn
- Discs fall to the lowest available position in the selected column
- Win by connecting **4 discs** in a row:
- Horizontally ➡️
- Vertically ⬇️
- Diagonally ↘️ or ↙️
- The round ends in a draw if the board fills up with no winner
## 📁 Project Structure
```
Connect-4/
│
├── Assets/          # Game graphics and images
├── Audio/           # Sound effects and music files
├── Font/            # Custom fonts for UI
├── main.py          # Main game file
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```
## 📦 Requirements
The game requires the following Python packages (listed in `requirements.txt`):
```
pygame
```
Install all dependencies with:
```bash
pip install -r requirements.txt
```
## 🤝 Contributing
Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request
### Ideas for Contributions
- Add AI opponent with difficulty levels
- Implement online multiplayer
- Add more board size options
- Create a tournament mode
- Add themes and customization options
- Improve animations and visual effects
## 📝 License
This project is open source and available under the MIT License.
## 👤 Author
**Eradboi**
- GitHub: [@Eradboi](https://github.com/Eradboi)
## 🙏 Acknowledgments
- Inspired by the classic Connect Four game by Milton Bradley
- Built with [Pygame](https://www.pygame.org/)
- Thanks to all contributors and players!
## 📸 Screenshots
*Coming soon! Screenshots of gameplay will be added here.*
---
<div align="center">
**Enjoy the game! If you like this project, please give it a ⭐**
  
Made with ❤️ and Python
</div>
