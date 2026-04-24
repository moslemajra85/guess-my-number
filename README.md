# Guess My Number

A simple terminal-based number guessing game written in Python.

## How it works

- The game picks a random number between 1 and 100.
- You try to guess it.
- After each guess, the game tells you whether to go higher or lower.
- The game tracks your attempts and time.
- You can type `quit` at any time to exit.

## Requirements

- Python 3.11 or later
- Optional: Docker

## Run locally

1. Open a terminal in the project folder.
2. Run:

```bash
python game.py
```

If your system uses `python3`, run:

```bash
python3 game.py
```

## Run with Docker

1. Build the image:

```bash
docker build -t guess-my-number .
```

2. Start the game:

```bash
docker run -it guess-my-number
```

## How to play

- Enter a number between 1 and 100.
- The game will respond with:
  - `Higher!` if your guess is too low
  - `Lower!` if your guess is too high
- When you guess correctly, the game shows:
  - the secret number
  - number of attempts
  - time taken
  - score

## Controls

- Type a number to guess
- Type `quit` to stop the game
- Press `Ctrl + C` to interrupt it

## Files

- [game.py](game.py) - main game logic
- [Dockerfile](Dockerfile) - container setup

## Notes

This project is intentionally small and easy to run in a terminal. You can extend it later with features like difficulty levels, high scores, or a GUI.
