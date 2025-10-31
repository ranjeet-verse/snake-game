# 🐍 Snake Game

A classic Snake Game implementation using Python's Turtle graphics library. Navigate the snake around the screen, collect food to grow longer, and try to achieve the highest score without hitting the walls or your own tail!

## 🎮 Features

- Smooth snake movement with keyboard controls
- Dynamic food spawning at random positions
- Real-time score tracking
- Collision detection (walls and self-collision)
- Snake grows longer with each food consumed
- Game over screen with final score display

## 🕹️ How to Play

- Use **Arrow Keys** to control the snake:
  - ⬆️ Up Arrow - Move up
  - ⬇️ Down Arrow - Move down
  - ⬅️ Left Arrow - Move left
  - ➡️ Right Arrow - Move right

- Eat the red food to grow longer and increase your score
- Avoid hitting the walls or your own tail
- Try to achieve the highest score possible!

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/snake-game.git
cd snake-game
```

2. Run the game:
```bash
python main.py
```

## 📋 Requirements

- Python 3.x
- Turtle graphics (built-in with Python)

## 📁 Project Structure
```
snake-game/
│
├── main.py          # Main game loop and logic
├── snake.py         # Snake class with movement logic
├── food.py          # Food class for random spawning
└── scoreboard.py    # Scoreboard class for score tracking
```

## 🎯 Game Rules

- The snake moves continuously in the direction it's facing
- Eating food increases your score by 1 and adds a segment to the snake
- The game ends when you hit a wall or collide with your own body
- You cannot reverse direction (e.g., if moving right, can't immediately go left)

## 🛠️ Built With

- Python
- Turtle Graphics Module

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Your Name - [Your GitHub Profile](https://github.com/YOUR_USERNAME)

## 🙏 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built as a Python learning project
