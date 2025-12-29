# Python Hangman Game
A terminal-based Hangman game that fetches random words via a REST API.

Author: Maheswar S

## Features
- Fetches random words using the Random Word API.
- Dynamic ASCII art that updates as you lose lives.
- Cross-platform terminal clearing (Windows/Linux/Mac).

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python hangman_game.py`

## How to Play
1. The game will fetch a random 5-letter word.
2. You have 8 attempts to guess the letters.
3. Every wrong guess draws a part of the hangman and reduces your score.
4. Try to guess the word before the hangman is complete!

