import time
import sys
import random
gamevillian = ['Demogorgon', 'Mind Flayer', 'Demodog']


def get_gamevillian():
    villian = random.choice(gamevillian)
    return villian


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    villian = get_gamevillian()
    print_pause("You find yourself lost and scared in a dark forest.")
    print_pause("The hair on the back of your neck stands at "
                "attention as you feel you are being watched.")
    print_pause(f"You have heard that this forest is home to a {villian}.")
    print_pause("To your left is a path to a wooden fort and to your "
                "right a path to a tunnel to the upside down.\n")


def wooden_fort(items):
    print_pause("You look to your left and head down the "
                "path the the wooden fort.")
    print_pause("You hear a noise behind you and you start to run.")
    print_pause("You trip, and quickly get up and jump into "
                "the wooden fort to hide.")
    print_pause("In the corner you see an evil looking box.")
    war_hammer(items)


def Tunnel_Upside(items):
    print_pause("You head down the path to your right and slowly "
                "enter the tunnel to the Upside Down.")
    print_pause(f"Quickly the terrifying monster emerges from the shadows and "
                "moves towards you with intent to attack.")
    choice = input("Do you want to fight the monster or run away? "
                   "(fight or run)\n").lower()
    if choice == 'fight':
        if "Warhammer" in items:
            print_pause("The monster swings at you barely missing "
                        "as you duck out of the way.")
            print_pause("You raise your Warhammer and swing as hard as "
                        "you can dealing a fatal blow to the demon creature.")
            print_pause("You crawl back through the tunnel to "
                        "the forest victorious!")
        else:
            print_pause("You grab a stick off the ground and as you lift "
                        "it up the powerful monster attacks killing you "
                        "with a fatal blow. You Lose.")
    elif choice == 'run':
        print_pause("You quickly scurry back through the tunnel and "
                    "into the forest to safety..but you hear rustling "
                    "as the monster seems to be coming after you.")
        location_choice(items)
    else:
        print_pause("Sorry, I don't understand.")
        Tunnel_Upside(items)


def war_hammer(items):
    print_pause("Would you like to open the box?")
    open = input("Press 1 to open the box.\n"
                 "Press 2 to NOT open the box.\n")
    if open == '1':
        print_pause("You open the box and find a Warhammer.")
        print_pause("You pick up your new found Warhammer and "
                    "decide to leave the wooden for and head "
                    "back into the forest")
        items.append("Warhammer")
        location_choice(items)
    elif open == '2':
        print_pause("You cowardly decide to not open the box and "
                    "slowly enter back in to the forest.")
        location_choice(items)
    else:
        print_pause("Sorry, I do not understand")
        war_hammer(items)


def location_choice(items):
    print_pause("where would you like to go?")
    location = input("Press 1 to go to the Wooden Fort on the left.\n"
                     "Press 2 to go to the Tunnel to the upside "
                     "down on the right.\n")
    if location == '1':
        wooden_fort(items)
    elif location == '2':
        Tunnel_Upside(items)
    else:
        location_choice(items)


def playagain(items):
    playagain = input('Do you want to play again? (y/n)').lower()
    if playagain == 'yes' or playagain == 'y':
        play_game()
    if playagain == 'n' or playagain == 'no':
        sys.exit("Thank you for playing. Goodbye!")


def play_game():
    items = []
    intro()
    location_choice(items)
    playagain(items)


play_game()
