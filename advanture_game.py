import random
import time


def the_game():
    item = []
    actor = random.choice(['troll', 'dragon', 'vampire', 'Goblin', 'pirate'])
    intro(actor)
    choose(item, actor)


def print_p(message):
    print(message)
    time.sleep(2)


def intro(actor):
    print_p("You find yourself standing in an open field,"
            " filled with grass and yellow wild flowers.")
    print_p("Rumor has it that a "+actor+" is somewhere"
            " around here, and has been terrifying the nearby village ...")
    print_p("In front of you is a house.")
    print_p("To your right is a dark cave.")
    print_p("In your hand you hold your trusty"
            " (but not very effective) dagger.")


def choose(item, actor):
    print_p("Enter 1 to knock on the door of the house.")
    print_p("Enter 2 to peer into the cave.")
    print_p("What would you like to do?")
    choice = input("(Please enter 1 or 2).")
    if choice == "1":
        house(item, actor)
    if choice == "2":
        cave(item, actor)
    else:
        choose(item, actor)


def house(item, actor):
    print_p("you approach the door of the house")
    print_p("you are about to knock when the door opens"
            "and out steps a "+actor+".")
    print_p("Eep! This is the "+actor+"'s house!")
    print_p("The "+actor+" attacks you!")
    print_p("you feel a bit under-preprad for this,"
            "what with only having a tiny dagger.")
    fight(item, actor)


def fight(item, actor):
    actions = input("Would you like to (1) fight or (2) run away?!")
    if actions == "1" and "Sworod of Ogoroth" not in item:
        print_p("you do your best...")
        print_p("but your dagger is no match for the "+actor+"")
        print_p("you have been defeated!")
        play_again()
    if actions == "1" and "Sworod of Ogoroth" in item:
        print_p("As the "+actor+" moves to attack,"
                " you unsheath your new sword.")
        print_p("The Sword of Ogoroth shines brightly in your"
                " hand as you brace yourself for the attack.")
        print_p("But the "+actor+" takes one look at "
                "your shiny new toy and runs away!")
        print_p("You have rid the town of the "+actor+"."
                " You are victorious!")
        play_again()
    elif "2" in actions:
        print_p("you run away fast out of the house."
                " Luckily, you don't seem to"
                "have been followed by "+actor+".")
        choose(item, actor)
    else:
        play_again()


def cave(item, actor):
    while True:
        if "Sworod of Ogoroth" not in item:
            print_p("You peer cauiously into the cave.")
            print_p("It turns out to be only a very small cave.")
            print_p("your eye catches a glint of metal behind a rock.")
            print_p("You have found the magical Sworod of Ogoroth!")
            print_p("You walk back out to the field.")
            print_p("You discard your silly old dagger"
                    " and take the sword with you.")
            print_p("You walk back out to the field.")
            item.append("Sworod of Ogoroth")
            choose(item, actor)
        if "Sworod of Ogoroth" in item:
            print_p("You peer cautiously into the cave.")
            print_p("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
            print_p("You walk back out to the field.")
            choose(item, actor)


def play_again():
    while True:
        q = str(input("Would you like to play again? (y/n)"))
        if q == "n":
            print_p("Thanks for playing! See you next time.")
            exit(0)
        elif q == "y":
            print_p("Excellent! Restarting the game ...")
            the_game()
        else:
            play_again()


the_game()
