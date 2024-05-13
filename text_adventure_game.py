import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.enemies_defeated = 0
        self.traps_cleared = 0
        self.princess_rescued = False
        self.dragon_defeated = False

    def fight_enemy(self):
        self.hp -= random.randint(10, 20)  # Simulate enemy attack
        if self.hp <= 0:
            print("Game Over! You were defeated in battle.")
            return False
        else:
            self.enemies_defeated += 1
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
            self.traps_cleared += 1
            print("You successfully cleared the trap!")
            time.sleep(1)
            return True

    def rescue_princess(self):
        if not self.dragon_defeated:
            print("You cannot rescue the princess yet. Defeat the dragon boss first.")
            return False
        elif self.enemies_defeated < 3 or self.traps_cleared < 3:
            print("You cannot rescue the princess yet. Clear all traps and defeat all enemies first.")
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

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            if not player.rest():
                break
        elif choice == "2":
            encounter_result = random.choice(["monster", "trap"])
            if encounter_result == "monster":
                print("\nYou suddenly hear a guttural growl echoing through the dungeon.")
                print("A monstrous creature emerges from the shadows, its eyes gleaming with malice.")
                print("What would you like to do?")
                print("1. Attack")
                print("2. Run away")
                action = input("Enter your choice (1-2): ")
                if action == "1":
                    print("You strike the monster!")
                    print("The monster loses 30% of its health.")
                elif action == "2":
                    if random.random() < 0.8:  # 80% chance of success to run away
                        print("You manage to escape from the monster without taking damage!")
                    else:
                        print("You attempt to run away but the monster catches you!")
                        if not player.fight_enemy():
                            break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
                    continue
            else:
                print("\nAs you move forward, you notice a faint glimmer on the ground.")
                print("You cautiously approach and realize it's a concealed trap!")
                print("What would you like to do?")
                print("1. Clear the trap")
                print("2. Continue exploring")
                action = input("Enter your choice (1-2): ")
                if action == "1":
                    if not player.clear_trap():
                        break
                elif action == "2":
                    print("You decide to look for another way to the dragon.")
                else:
                    print("Invalid choice. Please enter 1 or 2.")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        # After encountering monster or trap
        if player.enemies_defeated >= 3:
            if not player.dragon_defeated:
                print("\nAs you venture deeper into the dungeon, a fearsome dragon appears!")
                print("You must defeat the dragon to continue your quest.")
                if player.fight_enemy():
                    player.dragon_defeated = True
        else:
            print("\nWhat would you like to do now?")
            print("1. Continue exploring")
            action = input("Enter your choice (1): ")
            if action != "1":
                print("Invalid choice. Please enter 1.")

    if player.princess_rescued:
        print("\nCongratulations! You rescued the princess and won the game!")
    elif player.hp <= 0:
        print("\nGame Over! You have run out of health.")
    else:
        print("\nYou did not rescue the princess. Keep trying!")

if __name__ == "__main__":
    main()
