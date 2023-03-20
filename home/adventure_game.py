import time
import random
player_power = 0
enemy_power = 0


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt).lower()
        if choice == option1:
            break
        elif choice == option2:
            break
        else:
            print_pause("Invalid input. Try again.")
    return choice


def intro():
    print_pause("You are sleeping in your bed.")
    print_pause("Suddenly, you feel uneasy and wake up with a jolt.")
    print_pause("Strange! You are no longer in your bedroom.")
    print_pause("You find youselves in a giant dark room.")
    print_pause("There is eerie silence.")
    print_pause("You feel terrified.")
    print_pause("You see a big door.")
    print_pause("You turn the door knob, but it wont open.")
    print_pause("In the middle of the room, you find"
                " 2 glowing bottles of potion.")
    print_pause("You find a note asking you to pick one potion to drink.")


def bottle_1():
    print_pause("You drink the potion in bottle 1.")
    print_pause("A small wooden box appears.")
    print_pause("You open it and find a golden key and a silver key.")
    choice = valid_input("Pick a key. Enter 1 for Golden"
                         " or 2 for Silver.\n", "1", "2")
    if choice == '1':
        print_pause("You unlock the door and finds youself"
                    " back in your bedroom.")
        print_pause("You are safe.")
        print_pause("YOU WON!!!")
    elif choice == '2':
        print_pause("You unlock the door but you find yourself"
                    " back in the same giant dark room.")
        print_pause("GAME OVER")


def bottle_2():
    print_pause("You drink the potion in bottle 2.")
    print_pause("The room suddenly fills with smoke and an evil laugh.")
    print_pause("A scary looking troll appears.")
    while True:
        choice = input("Enter F to fight or R to run away.\n")
        if choice == 'F':
            player_power = random.randint(0, 10)
            enemy_power = random.randint(0, 10)
            if player_power > enemy_power:
                print_pause("You win the fight! YAY!!!")
            else:
                print_pause("The troll defeats you and"
                            " you are dead. GAME OVER")
            break
        elif choice == 'R':
            print_pause("You try to run but there is no"
                        "way out of the room.\n"
                        " The troll attacks and kills you.\n"
                        " GAME OVER")
            break
        else:
            print_pause("Enter a valid input")
    return choice


def pick_bottle():
    choice = valid_input("Pick a bottle. Press 1 or 2.\n", "1", "2")
    if choice == '1':
        bottle_1()
    elif choice == '2':
        bottle_2()


def play_game():
    intro()
    pick_bottle()


def play_again():
    while True:
        choice = input("Would you like to play again? Enter Y or N\n")
        if choice == 'N':
            print_pause("Thanks for playing. GOOD BYE!.")
            break
        elif choice == 'Y':
            play_game()
            break
        else:
            print_pause("Invalid output. Try again.")
    return choice


play_game()
play_again()
