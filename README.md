Space Explorer: Xenovita Escape

Author: Romeo Bartha
Date: 25/11/2024

Description

Space Explorer: Xenovita Escape is a text-based adventure game where the player is stranded on a mysterious planet called Xenovita. The goal of the game is to explore the planet, solve puzzles, collect fuel, and escape before running out of oxygen.

The player must navigate different discoveries on the planet, solve riddles or math puzzles to gain fuel, and carefully manage their oxygen levels to survive and escape.

Features

Planet Exploration: Players can explore multiple discoveries on the planet.

Puzzles: Includes both riddles and math puzzles that need to be solved to collect fuel.

Fuel Collection: Fuel is required to power the rocket and escape Xenovita.

Oxygen Management: Oxygen decreases with every exploration. Players must monitor oxygen levels carefully.

Replayable: Puzzles are randomized to provide a different experience every time.

Menu System: Options to explore, review fuel locations, check oxygen/fuel levels, or quit the game.

Gameplay Instructions

Start the Game: Run the game script to begin your adventure.

Explore Discoveries: Choose from available discoveries on Xenovita to explore.

Solve Puzzles: Complete a riddle or math puzzle at each location to earn fuel.

Monitor Resources: Keep an eye on your oxygen and fuel levels.

Escape: Collect at least 100L of fuel before oxygen runs out to escape the planet successfully.

Game Over: If oxygen reaches 0 before you collect enough fuel, the game ends, and you must restart.

Classes Overview

Planet: Represents the planet and tracks discoveries and clues.

Player: Represents the player’s oxygen, fuel, and location.

Puzzle (abstract): Base class for different types of puzzles.

RiddlePuzzle: Presents riddles to the player.

MathPuzzle: Presents random math problems.

Space: Handles the game flow, menu, exploration, and puzzle integration.

Installation and Requirements

Python 3.8+ is required to run the game.

Install required dependencies:

pip install colorama


Run the game:

python space_explorer.py

Game Controls

1: Explore a new discovery

2: Review fuel locations discovered

3: Check current oxygen and fuel levels

4: Quit the game

Notes

Each discovery consumes a random amount of oxygen (10–25%).

Fuel gained per puzzle solved is randomized between 10–30L.

The game provides ASCII art for a visual feel of exploration and success/failure.

Credits

Developed by Romeo Bartha

Uses Colorama for colored text output.
