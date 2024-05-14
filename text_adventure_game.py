import random
import time

class Player:
    def __init__(self, name):
        """
        Initialize the player with name, health points, and initial states
        """
        self.name = name
        self.hp = 100
        self.princess_rescued = False
        self.dragon_defeated = False
        self.has_magical_sword = False

    def fight_enemy(self):
        """
        Simulate a fight with an enemy, causing random damage to the player
        """
        self.hp -= random.randint(10, 20)
        if self.hp <= 0:
            print("Game Over! You were defeated in battle.")
            return False
        else:
            time.sleep(1)
            return True

    def clear_trap(self):
        """
        Simulate an attempt to clear a trap with a 50% chance of success
        """
        if random.random() < 0.5:
            print("You triggered a trap and lost some health!")
            self.hp -= random.randint(5, 10)
            if self.hp <= 0:
                print("Game Over! You were defeated by a trap.")
                return False
            return True
        else:
            print("You failed to clear the trap!")
            return True

    def rest(self):
        """
        Simulate resting, with a chance to encounter a monster
        """
        if random.choice(["safe", "monster"]) == "safe":
            self.hp = min(100, self.hp + 30)
            print("You found a safe spot to rest and restored 30 health points.")
        else:
            print("You encountered a monster while searching for a safe spot to rest!")
            if self.fight_enemy():
                print("You defeated the monster, but your rest was interrupted.")
            else:
                return False
        return True

    def encounter(self):
        """
        Simulate an encounter, which can be a monster, a trap, or an empty room
        """
        encounter_result = random.choice(["monster", "trap", "empty room"])
        if encounter_result == "monster":
            print("\nYou hear heavy footsteps approaching.")
            print("A grotesque creature emerges from the darkness!")
            if self.fight_enemy():
                print("You skillfully defeat the monster, emerging victorious!")
            else:
                return False
        elif encounter_result == "trap":
            print("\nYou notice a faint glimmer on the ground.")
            print("It's a concealed trap! You attempt to clear it...")
            if not self.clear_trap():
                return False
        else:
            print("\nYou enter an empty room, taking a moment to catch your breath.")
        return True

    def search_sword(self):
        """
        Simulate searching for the magical sword with a 50% chance of success
        """
        if not self.has_magical_sword:
            if random.random() < 0.5:
                print("\nYou've found the legendary magical sword!")
                self.has_magical_sword = True
                time.sleep(1)
            else:
                print("\nYou search but find nothing of significance.")
        else:
            print("\nYou already have the magical sword.")

    def fight_dragon(self):
        """
        Simulate the final battle with the dragon if the player has the magical sword
        """
        if self.has_magical_sword and not self.dragon_defeated:
            print("\nIt's time to face Valorin, the fierce green dragon!")
            print("The ground trembles as the mighty dragon emerges.")
            time.sleep(1)
            print("The clash of steel and scales echoes through the chamber.")
            if self.fight_enemy():
                self.dragon_defeated = True
                print("\nWith a final swing, you strike true, defeating Valorin.")
                time.sleep(1)
                print("You find the princess, her eyes sparkling with gratitude.")
                self.princess_rescued = True
            else:
                return False
        elif not self.has_magical_sword:
            print("\nYou need to find the magical sword first!")
        elif self.dragon_defeated:
            print("\nYou've already defeated the dragon!")
        return True

def main():
    """
    Main function to start and run the game
    """
    print("Welcome to the Fantasy Adventure Game!")
    name = input("Enter your name:\n")
    player = Player(name)

    print("\nYou find yourself in a dark and eerie dungeon filled with traps and monsters.")
    print("Only the bravest warriors can rescue the princess.")
    print("Choose your path wisely, for danger lurks around every corner.\n")

    # Main game loop
    while not player.princess_rescued and player.hp > 0:
        print(f"\nHealth Points: {player.hp}")
        print("Choose your action:")
        print("1. Look for a safe spot to rest")
        print("2. Follow the map to the dragon")
        if not player.has_magical_sword:
            print("3. Search for the magical sword")
        if player.has_magical_sword and not player.dragon_defeated:
            print("4. Fight the dragon")

        choice = input("Enter your choice (1-4): ")

        # Process player's choice
        if choice == "1":
            if not player.rest():
                break
        elif choice == "2":
            if not player.encounter():
                break
        elif choice == "3":
            player.search_sword()
        elif choice == "4":
            if not player.fight_dragon():
                break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    # Game conclusion messages
    if player.princess_rescued:
        print("\nCongratulations! You rescued the princess and won the game!")
    else:
        print("\nGame Over! You have run out of health.")
    print("Thank you for playing the Fantasy Adventure Game!")

if __name__ == "__main__":
    main()
