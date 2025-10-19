# 🚀 Space Explorer: Xenovita Escape 🌌

**Author:** Romeo Bartha  
**Date:** 25/11/2024  

## 🌟 Description
*Space Explorer: Xenovita Escape* is a text-based adventure game where the player is stranded on a mysterious planet called **Xenovita**. The goal is to explore the planet, solve puzzles, collect fuel ⛽, and escape before running out of oxygen 🫧.

Players navigate different discoveries on the planet, solve riddles or math puzzles to gain fuel, and carefully manage their oxygen levels to survive and escape.

---

## 🛠️ Features
- **Planet Exploration 🪐:** Explore multiple discoveries on Xenovita.  
- **Puzzles 🧩:** Solve riddles or math problems to collect fuel.  
- **Fuel Collection ⛽:** Fuel is required to power the rocket and escape.  
- **Oxygen Management 🫧:** Oxygen decreases with each exploration. Monitor carefully!  
- **Replayable 🔄:** Randomized puzzles provide a unique experience each time.  
- **Menu System 📜:** Options to explore, review fuel locations, check oxygen/fuel, or quit.  

---

## 🎮 Gameplay Instructions
1. **Start the Game:** Run the script to begin your adventure.  
2. **Explore Discoveries 🪐:** Choose a location on Xenovita to explore.  
3. **Solve Puzzles 🧩:** Complete riddles or math puzzles to earn fuel.  
4. **Monitor Resources 🫧⛽:** Keep track of oxygen and fuel levels.  
5. **Escape 🚀:** Collect at least **100L of fuel** before oxygen runs out to escape the planet.  
6. **Game Over 💀:** If oxygen reaches 0 before collecting enough fuel, the game ends and you must restart.  

---

## 📚 Classes Overview
- **Planet 🌍:** Tracks discoveries and clues.  
- **Player 👨‍🚀:** Manages oxygen, fuel, and location.  
- **Puzzle (abstract) 🧩:** Base class for different puzzle types.  
  - **RiddlePuzzle 🪐:** Presents riddles to the player.  
  - **MathPuzzle ➗:** Presents random math problems.  
- **Space 🌌:** Handles game flow, menus, exploration, and puzzle integration.  

---

## 💻 Installation and Requirements
- **Python 3.8+** is required.  
- Install dependencies:  
```bash
pip install colorama
