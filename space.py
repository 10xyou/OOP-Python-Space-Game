"""
Author: Romeo Bartha

Date: 25/11/2024

Description: Player gets spawned on a planet, the planet has different new discoveries such as a new civilization. The player has to go around to find clues to reavel each clue has a little puzzle
which the user has to complete to gain fuel, this fuel is needed for the rocket ship to escape this planet, the player has an oxygen tank with a certain amount of bubbles in it and they're slowly
decreasing with time. Aim of the game is to get through the challenges with enough oxygen tank and enough fuel to leave the planet and head back home.

"""



import random
import time
from colorama import Fore, Back, Style

class Planet:
    def __init__(self, name):
        self.name = name
        self.__clues = []
        self.__discovered = False

    def discover(self): # Marks the planet as discovered
        self.__discovered = True
        print(f"\033[96mYou've landed on {self.name}. A strange and mysterious place awaits!\033[0m") 

    def add_clue(self, clue):
        # Function to add the fuel found
        self.__clues.append(clue)

    def review_clues(self):
        # Returns the fuel found at different spots
        return self.__clues

class Player:
    def __init__(self, name):
        self.name = name
        self.oxygen = 100  # oxygen starts at 100 bubbles
        self.fuel = 0      # fuel collected starts at 0
        self.location = None # Location is set to none

    def explore(self, location):
        
        
        self.location = location
        print(f"{self.name} begins exploring the {location}.")
        oxygen_loss = random.randint(10, 25) # Losing oxygen randomly between 10 and 25
        self.oxygen -= oxygen_loss
        if self.oxygen < 0:  # Ensure oxygen doesn't go below 0
            self.oxygen = 0
        print("\n")
        print(f"🫧 Remaining oxygen: {'🫧' * (self.oxygen // 10)} ({self.oxygen}%)") # Displays the current oxygen left in the tank
        

    def collect_fuel(self, amount):
        amount = random.randint(10, 30) # Fuel is randomly found from 10 to 30
        self.fuel += amount
        print(f"Fuel collected: {amount}L. Total fuel: {self.fuel}L.") # Displays the fuel collected

    def has_sufficient_fuel(self):
        return self.fuel >= 100 # Returns the fuel if its over 100

class Puzzle:
    def __init__(self, description):
        self.description = description

    def solve(self):
        raise NotImplementedError("Subclasses should implement this method.")

class RiddlePuzzle(Puzzle):
    riddles = [
        ("I keep my face turned away, hide my dark side every day. What am I?", "Moon"),
        ("Sailors of the void, wearing suits of armor, exploring where none have before. Who are we?", "Astronauts"),
        ("With me, you see the stars so bright, peering into the deep, dark night.?", "Telescope"),
        (" I’m a giant ball of gas, shining bright in the sky, without me, life on Earth would surely die", "Sun"),
        ("I’m a red , dusty and dry, with the largest volcano and canyons that are high", "Mars"),
        ("Huge explosion of a star, when I die, I shine bright from afar.", "Supernova"),
        ("Planet is known as the “Blue Planet” because of its vast oceans", "Earth"),
    ] # Riddles based on planets
    
    riddle_used = [] # List to store the riddles used in the game so no repetition is occured
    
    def __init__(self): 
        print("\n")
        super().__init__("Solve the riddle to proceed.")
        if not RiddlePuzzle.riddles:
            print("There are no more riddles available")
            self.riddle, self.answer = "", ""
        else:
            self.riddle, self.answer = random.choice(self.riddles) # Randomizes a riddle
            RiddlePuzzle.riddles.remove((self.riddle, self.answer)) # Removes the riddle from the list
            RiddlePuzzle.riddle_used.append((self.riddle, self.answer)) # Appends the used riddle to the riddle_used list
            

    def solve(self):
        print(self.description)
        print(self.riddle)
        answer = input("Enter your answer: ").strip().lower() # Asks the user to enter answer and makes it lower case
        return answer == self.answer.lower()

class MathPuzzle(Puzzle):
    def __init__(self):
        print("\n"*3)
        super().__init__("Solve the math puzzle to proceed.")

    def solve(self):
        print(self.description)
        num1, num2 = random.randint(1, 10), random.randint(1, 10) # Randomize number from 1 to 10
        print(f"What is {num1} * {num2}?")# Asks
        try:
            answer = int(input("Enter your answer: "))
            return answer == num1 * num2
        except ValueError:
            print("Invalid input! Answer must be a number.") # Error validation to make sure it is a number
            return False

class Space:
    def __init__(self, name="Astronaut"):
        self.player = Player(name)
        self.planet = Planet("Xenovita")
        self.running = True
        self.completed = False
        self.discoveries = ["The Great Red Spot", "Sea of Tranquility", "Fra Mauro Highlands", "Ocean of Storms", "NGC 604", "The Tharsis Bulge", "Olympus Mons"] # Areas on the planet the player can visit

    def start_game(self):
        time.sleep(1)
        print(Style.BRIGHT + "\033[34mWelcome to Planet Xenovita!.\033[0m")
        time.sleep(1)
        print(Style.BRIGHT + "\n\033[34mYour mission is to escape Xenovita.\033[0m")
        time.sleep(1)
        print(Style.BRIGHT + "\n\033[34mYou start with 100% Oxygen and 0L Fuel amount.\033[0m")
        time.sleep(1)
        print(Style.BRIGHT + "\n\033[34mYour aim is to get to 100L of fuel to escape the Planet and go back to earth. \033[0m")
        time.sleep(1)
        print(Style.BRIGHT + "\n\033[34mGood Luck.\033[0m")
        time.sleep(3)
        print(rf"""
    _..._
      .'     '.      _
     /    .-""-\   _/ \\
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|{self.player.name} _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'.;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \
          `-._/._/
        """)

        time.sleep(2)
        print("\n"*40)
        self.planet.discover()
        self.run_game()

    def run_game(self):
        while self.running:
            
            if self.player.oxygen <= 0:
                print("\033[40mYou ran out of oxygen! You died!. Game over.\033[0m")
                print("""
⠀⠀⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⡰⠋⢙⣿⣦⡀⠀⠀⠀⠀⠀
⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿⣿⣆⠀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⣫⠟⠋⠀⠀⠀⠀
⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢹⣿⣿⣧⣿⣿⣆⡹⣖⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⠏⢧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⢳⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⠏⠀⠀⠀⠀⠀⠀
""")

                self.start_game()
            
            if self.player.has_sufficient_fuel(): # If the fuel goes over 100 the game is finished and the player escapes with the rocket.
                print("\033[42mYou have collected enough fuel to leave the planet!\033[0m")
                print("\033[42mCongratulations, you escaped Xenovita!\033[0m")
                print("""
                           *     .--.
                                / /  `
               +               | |
                      '         \\ \\__,
                  *          +   '--'  *
                      +   /\\
         +              .'  '.   *
                *      /======\\      +
                      ;:.  _   ;
                      |:. (_)  |
                      |:.  _   |
            +         |:. (_)  |          *
                      ;:.      ;
                    .' \\:.    / `.
                   / .-'':._.'`-. \\
                   |/    /||\\    \\|
              _..--\"\"\"````\"\"\"--.._
           _.-'``                    ``'-._
         -'                                '-
                    
""")


                self.running = False
                self.completed = True
                break

            self.display_menu()

    def display_menu(self):
    
        # Menu for the game
        print(Style.BRIGHT + "\nMenu:")
        print(Style.BRIGHT + "1. Explore a new discovery")
        print(Style.BRIGHT + "2. Review Fuel location")
        print(Style.BRIGHT + "3. Check fuel and oxygen levels")
        print(Style.BRIGHT + "4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n"*40)
            self.explore_discovery()
        elif choice == "2":
            print("\n"*40)
            clues = self.planet.review_clues()
            if clues:
                print("Fuel found so far:")
                for clue in clues:
                    print(f"\033[33m- {clue}\033[0m")
            else:
                print("No fuel found yet.")
        elif choice == "3":
            print("\n"*40)
            print(Style.BRIGHT + f"\033[35m🫧 Oxygen level: {'🫧' * (self.player.oxygen // 10)} ({self.player.oxygen}%)\033[0m")
            print(Style.BRIGHT + f"\033[35mFuel collected: {self.player.fuel}L\033[0m")
        elif choice == "4":
            print("Exiting game. Goodbye!")
            self.running = False
        else:
            print("Invalid choice. Try again.")

    def explore_discovery(self):
        if not self.discoveries:
            print("You've explored all available discoveries.")
            return
        
        print("Choose a discovery to explore:")
        for i, discovery in enumerate(self.discoveries, start=1): #For loop to print the list of the discoveries
            print(f"{i}. {discovery}")
        try:
            choice = int(input("Enter your choice: ")) - 1
            print("\n"*50)

            if 0 <= choice < len(self.discoveries):
                discovery = self.discoveries.pop(choice)
                self.player.explore(discovery)

                puzzle = random.choice([RiddlePuzzle(), MathPuzzle()])
                if puzzle.solve():
                    print(f"\033[32mYou solved the puzzle at {discovery}!\033[0m")
                    self.player.collect_fuel(25)
                    self.planet.add_clue(f"Fuel found at {discovery}")
                    time.sleep(3)
                    print("\n"*40)
                else:
                    print(f"\033[31mYou failed to solve the puzzle at {discovery}. No fuel collected.\033[0m")
                    time.sleep(3)
                    print("\n"*40)
            else:\
                print("Invalid choice.")
        except ValueError:
            print("Invalid input! Please enter a number.")
