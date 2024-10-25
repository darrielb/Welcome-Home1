## This program will take the user on the 'Welcome Home Halloween Adventure'!
# The user will follow a pre-written script designed to take them
# through a spooky adventure!
# @author DARRIELL BUTLER
# @version 10/12/24

# INTRODUCTION
# Welcome Home!
# You are at home, resting on your couch, enjoying a fall evening.
# Suddenly, you hear a knock at the door.
# As you approach the door, you realize today is 10/31! The visitors are trick-or-treaters!
# Your objective is to survive the night!

# START GAME
# You can give the trick-or-treaters chocolate bars or jawbreakers.
# You grab your candy of choice to give to the trick-or-treaters.

# SETUP
print("Welcome Home!")
print() # Inserting line breaks for formatting purposes
print("You are at home, resting on your living room couch, enjoying a fall evening.")
print("Suddenly, you hear a knock at the door.")
print()
print("As you approach the door, you realize today is 10/31! The visitors are trick-or-treaters!")
print("You have two options: give the trick-or-treaters chocolate bars, or jawbreakers.\nYou grab your candy of choice to give to the trick-or-treaters.")
print()
print("Objective: Gain a score of 100 to unlock the true ending!")
print()

score = 0  # User starts with a score of 0. A score of 100 unlocks the true ending

while True:  # This outer loop allows the user to restart the entire game after a 'Game Over'

    # BEGIN
    print("Choose 'chocolate bars' or 'jawbreakers'")  # Prompt the user for a choice to initialize the game
    candyChoice = input("> ")

    # CANDY CHOICE A
    if candyChoice == "-1":  # Check if the user entered the sentinel to restart. The user will restart from this point
        continue  # Restarts the game loop in case of an invalid input

    if candyChoice.lower() == "chocolate bars":  # '.lower()' allows the user to input upper or lowercase, at random
        print("You decide on the chocolate bars.")
        print() # Inserting line breaks for formatting purposes
        print("As you open the door to greet the trick-or-treaters, you realize no one is there...")
        input("Press 'Enter' to continue...")
        print()
        print("Do you want to close the door, or step outside and look for them?")
        print("Choose 'close door' or 'step outside'")
        doorChoice = input("> ")

        # DOOR CHOICE A
        if doorChoice == "-1":
            continue  # Restarts the game loop

        # ENDING A, 10 points
        if doorChoice.lower() == "close door":
            print("You start to close the door, but you hear a creaking noise from the floor behind you...")
            print()
            input("Press 'Enter' to continue...")
            print()
            print("As you turn around, you are face-to-face with a masked slasher!")
            print()
            input("Press 'Enter' to continue...")
            print()
            print("Before you can react, the masked slasher attacks you.")
            print("You are dead...")
            print()
            score = 10  # Assign 10 points for Ending A
            input("Press 'Enter' to continue")
            print()
            print("The End")
            print()
            print("Your Score Is:", score) # Prints user score after obtaining an ending
            print()
            print("Ending A") # Displays which ending user has obtained

            restart = input("Press '-1' to restart")  # Restart after 'Game Over'
            if restart == "-1":
                continue  # Restarts the game loop in case of an invalid input, or a 'Game Over'
            else:
                break  # Exits the game loop and allows for restart, instead of a 'crash' or 'end program' message.

        # DOOR CHOICE B, ENDING B 20 points
        elif doorChoice.lower() == "step outside":
            print("You step outside...")
            print()
            print("You hear a loud crash from the living room you were just in...")
            print()
            input("Press 'Enter' to continue...")
            print()
            print("You turn around hurriedly and enter the house.")
            print("As you enter the living room, you are confronted with a masked slasher!")
            print()
            input("Press 'Enter' to continue...")
            print()
            print("You arm yourself with the iron poker near the fireplace...")
            input("Press 'Enter' to continue...")
            print()
            print("You battle with the masked slasher until they flee through the front door...")
            input("Press 'Enter' to continue...")
            print()
            print("Congratulations! You survived the 'Welcome Home Halloween Adventure!'")
            print()
            score = 20  # Assign 20 points for Ending B
            input("Press 'Enter' to continue")
            print()
            print("The End")
            print()
            print("Your Score Is:", score)
            print()
            print("Ending B")

            restart = input("Press '-1' to restart")  # Restart after 'The End'. Enables user to restart without exiting.
            if restart == "-1":
                continue
            else:
                break

        else:
            print("Invalid choice. Please enter 'close the door' or 'step outside'.")  # Restart after invalid choice.
            restart = input("Press '-1' to restart")
            if restart == "-1":
                continue
            else:
                break

    # CANDY CHOICE B
    elif candyChoice.lower() == "jawbreakers":
        print("You decide on the jawbreakers.")
        print("As you reach for the jawbreakers, a gloved hand grabs your arm!")
        print()
        input("Press 'Enter' to continue...")
        print()
        print("You look up to find a masked slasher in your home!")
        input("Press 'Enter' to continue...")
        print()

        # FIGHT OR FLIGHT
        print("Choose 'fight' or 'flight'")
        fearChoice = input("> ")

        if fearChoice == "-1":
            continue

        # FIGHT, ENDING C 30 Points
        if fearChoice.lower() == "fight":
            print("You chose to fight!")
            input("Press 'Enter' to continue...")
            print()
            print("You attack the masked slasher! They unhand you and you run to the kitchen\nto arm yourself!")
            print("You grab a knife, attack the slasher, and run safely away to find the police!")
            input("Press 'Enter' to continue...")
            print()
            print("As you run away, the police enter your home and arrest the masked slasher.")
            input("Press 'Enter' to continue...")
            print()
            print("Congratulations! You survived the 'Welcome Home Halloween Adventure!'")
            print()
            score = 30  # Assign 30 points for Ending C
            input("Press 'Enter' to continue")
            print()
            print("The End")
            print()
            print("Your Score Is:", score)
            print()
            print("Ending C")

            restart = input("Press '-1' to restart")
            if restart == "-1":
                continue
            else:
                break

        # FLIGHT (TRUE ENDING, ENDING D, 10 POINTS)
        elif fearChoice.lower() == "flight":
            print("You successfully pull yourself away from the slasher...")
            print()
            input("Press 'Enter' to continue...")
            print()
            print("As you free yourself, you run upstairs and hide in your bedroom...")
            print()
            input("Press 'Enter' to continue...")
            print()
            print("While you hide in your bedroom, you hear a voice yell 'Police! Hands up!'")
            print("The police witnessed the masked slasher attempt to attack you from the street.")
            print()
            input("Press 'Enter' to continue...")
            print()
            print("The slasher does not obey...")
            input("Press 'Enter' to continue")
            print()
            print("The police attack the masked slasher, rendering them harmless...")
            print("The police inform you that you are safe to exit the bedroom...")
            input("Press 'Enter' to continue")
            print()
            print("Congratulations! You survived the 'Welcome Home Halloween Adventure!'")
            print()
            input("Press 'Enter' to continue")
            print()
            score = 100  # Award 100 points for the true ending, Ending D
            if score == 100:
                print("You have unlocked the true ending,\nEnding D!")
            print()
            input("Press 'Enter' to continue")
            print()
            print("The End")
            print()
            print("Your Score Is:", score)

            restart = input("Press '-1' to restart")