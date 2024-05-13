import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.princess_rescued = False
        self.dragon_defeated = False
        self.has_magical_sword = False

    def fight_enemy(self):
        self.hp -= random.randint(10, 20)  # Simulate enemy attack
        if self.hp <= 0:
            print("Game Over! You were defeated in battle.")
            return False
        else:
            time.sleep(1)
            return True

    def clear_trap(self):
        if random.random() < 0.5:  # 50% chance of trap triggering
            print("You triggered a trap and lost some health!")
            self.hp -= random.randint(5, 10)  # Simulate trap damage
            if self.hp <= 0:
                print("Game Over! You were defeated by a trap.")
                return False
            return True
        else:
            print("You failed to clear the trap!")
            return True

    def rescue_princess(self):
        if not self.dragon_defeated:
            print("You cannot rescue the princess yet. Defeat the dragon boss first.")
            return False
        else:
            self.princess_rescued = True
            time.sleep(1)
            return True

    def rest(self):
        result = random.choice(["safe", "monster"])
        if result == "safe":
            restored_health = 30
            self.hp = min(100, self.hp + restored_health)
            print("You found a safe spot to rest and restored 30 health points.")
        else:
            print("You encountered a monster while searching for a safe spot to rest!")
            if self.fight_enemy():
                print("You defeated the monster, but your rest was interrupted.")
            else:
                return False
        return True

def main():
    print("Welcome to the Fantasy Adventure Game!")
    name = input("Enter your name: ")
    player = Player(name)

    print("\nYou find yourself in a dark and eerie dungeon filled with traps and monsters.")
    print("Legend has it that only the bravest warriors can navigate through it and rescue the princess.")
    print("Choose your path wisely, for danger lurks around every corner.\n")

    while not player.princess_rescued and player.hp > 0:
        print("Health Points:", player.hp)
        print("\nChoose your action:")
        print("1. Look for a safe spot to rest")
        print("2. Follow the map to the dragon")

        if not player.has_magical_sword:
            print("3. Search for the magical sword")

        if player.has_magical_sword and not player.dragon_defeated:
            print("4. Fight the dragon")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not player.rest():
                break
        elif choice == "2":
            encounter_result = random.choice(["monster", "trap", "empty room"])
            if encounter_result == "monster":
                print("\nYou hear heavy footsteps approaching.")
                print("You ready your weapon as a grotesque creature emerges from the darkness!")
                print("You engage in a fierce battle with the monster.")
                if random.random() < 0.45:  # 45% chance of losing health during the encounter
                    print("During the battle, you sustain some injuries.")
                    player.hp -= random.randint(5, 15)
                else:
                    print("You skillfully defeat the monster, emerging victorious!")
            elif encounter_result == "trap":
                print("\nAs you move forward, you notice a faint glimmer on the ground.")
                print("You cautiously approach and realize it's a concealed trap!")
                print("You attempt to clear the trap...")
                if not player.clear_trap():
                    break
            else:  # Empty room encounter
                print("\nYou enter a room devoid of any dangers or treasures.")
                print("You take a moment to catch your breath and continue your journey.")
        elif choice == "3":
            if not player.has_magical_sword:
                if random.random() < 0.35:  # 35% chance to find the magical sword
                    print("\nYou've stumbled upon an ancient chest hidden in the shadows.")
                    print("Opening it, you find the legendary magical sword, shimmering with power!")
                    print("As you grasp the sword, you feel its magical energy flowing through you.")
                    player.has_magical_sword = True
                    time.sleep(1)
                else:
                    print("\nYou search the area but find nothing of significance.")
            else:
                print("\nYou already have the magical sword.")
        elif choice == "4":
            if player.has_magical_sword and not player.dragon_defeated:
                print("\nYou've obtained the magical sword. It's time to face Valorin, the fierce green dragon of legends!")
                print("Prepare yourself for the final battle!")

                # Description of the epic battle with Valorin
                time.sleep(1)
                print("\nThe ground trembles as the mighty dragon emerges from the depths of its lair, its emerald scales glistening menacingly.")
                print("With a deafening roar, Valorin unleashes a torrent of flames, but you stand firm, brandishing the magical sword.")
                print("The clash of steel and scales echoes through the chamber as you engage in a battle of wills and strength.")

                # Simulate battle with the dragon
                if player.fight_enemy():
                    player.dragon_defeated = True
                    print("\nWith a final mighty swing, you strike true, driving the magical sword deep into Valorin's heart.")
                    print("The dragon lets out a thunderous roar before collapsing to the ground, defeated.")
                    time.sleep(1)
                    print("\nAs the dust settles, you catch your breath, victorious in your quest to vanquish the mighty dragon.")
            elif not player.has_magical_sword:
                print("\nYou need to find the magical sword first!")
            elif player.dragon_defeated:
                print("\nYou've already defeated the dragon!")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

    # After defeating the dragon
    if player.princess_rescued:
        print("\nCongratulations! You rescued the princess and won the game!")
        return
    elif player.hp <= 0:
        print("\nGame Over! You have run out of health.")
        return

    # If player chooses to end the game after defeating the dragon
    print("\nWith Valorin vanquished, you explore the depths of the dragon's lair.")
    print("Amidst the rubble and treasure, you find the princess, her eyes sparkling with gratitude and admiration.")
    time.sleep(1)
    print("\nIn that moment, as you lock eyes with the princess, you realize that your journey was not just about defeating monsters.")
    print("It was about finding courage, compassion, and, perhaps, even love.")
    time.sleep(1)
    print("\nYou extend your hand to the princess, and together, you embark on a new adventure, bound by destiny and the bonds of affection.")

if __name__ == "__main__":
    main()
