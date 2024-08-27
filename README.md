# Author

# Maria Magdalena Maluff Stabio

# Circle CI

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-MaguiMaluff/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-MaguiMaluff/tree/main)

# Maintainability

[![Maintainability](https://api.codeclimate.com/v1/badges/b59b127437142b0adc83/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-MaguiMaluff/maintainability)

# Coverage

[![Test Coverage](https://api.codeclimate.com/v1/badges/b59b127437142b0adc83/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-MaguiMaluff/test_coverage)

# How to play Chess

## Objective
- The main objective is to capture your opponent's king.

## Setup
- Chess is played on an 8x8 board.
- Each player starts with 16 pieces: 1 king, 1 queen, 2 rooks, 2 bishops, 2 knights, and 8 pawns.
- White always move first

## Movement
- **King**: Moves one square in any direction.
- **Queen**: Moves any number of squares in any direction.
- **Rook**: Moves any number of squares horizontally or vertically.
- **Bishop**: Moves any number of squares diagonally.
- **Knight**: Moves in an "L" shape: two squares in one direction and then one square perpendicular.
- **Pawn**: Moves forward one square, or two squares on its first move; captures diagonally.

## Special Moves
- **Promotion**: A pawn reaching the opposite end of the board can be promoted to any other piece (except a king).

## Winning the Game
- **Checkmate**: The game is won if the opponent's king is capture by the other player.
- **Draw**: The game can end in a draw by desicion or not enough pieces to keep playing.

# How to play on Docker

- Download the file Dockerfile

- On docker, run docker build -t my_chess . to build the image

- Run docker run -it my_chess to play