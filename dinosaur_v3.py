"""
version: 3

Filename:  dinosaur.py
Author:  Heleina G.
Date:  6/07/22
Description: an informational test about dinosaurs. It will tell
you about dinosaurs and produce 5 random questions(among 10-15) for
you to answer. :)
"""

import random
import time

# initialize the dictionary
# dictionary = {key:value}
# key = questions, value = answers
QUESTIONS_ABOUT_DINO = {
    "THE DINOSAURS LIVED DURING THE ______ ERA": "mesozoic",
    "DINOSAURS ARE MAINLY DIVIDED INTO 2 CATEGORIES BASED ON THEIR ____ BONE": "pelvis",
    "ALL DINOSAURS DESCENDED FROM REPTILES CALLED ______": "archosaurs",
    "MOST DINOSAURS WERE ____ (HERBIVORES/CARNIVORES)": "herbivores",
    "WHAT CREATURE (THAT STILL CURRENTLY EXISTS) HAVE LIVED LONGER THAN DINOSAURS?": "sharks",
    "MOST SCIENTISTS BELIEVE THAT DINOSAURS DIED FROM A _____": "meteor",
    "WHAT DOES THE TERM 'DINOSAUR' MEAN?": "terrible lizard",
    "THERE ARE APPROXIMATELY ___ VALID DINOSAUR SPECIES": "700",
    "WHAT WAS THE BIG SUPERCONTINENT CALLED?": "pangea",
    "TRUE OR FALSE: DID BIRDS EVOLVE FROM DINOSAURS": "true",
    "THE VELOCIRAPTORS ARE ACTUALLY THE SIZE OF A HUMAN ____": "toddler"}


# initialize the variables
repeat_menu = True
repeat_test = True
MENU_CHOICES = ["1", "2", "3"]
# the scores and how many questions will be given
user_score = 0

# information part about dinosaurs
# menu & introduction about dinosaurs

while repeat_menu:
    # introduction to the program; menu
    # ask user if they want to play the quiz
    print("""A very short informational quiz about your
favourite reptiles, the dinosaurs!!
[It is suggested you do #2 first. :)]

    1 = start the quiz
    2 = quick information about dinosaurs!
    3 = quit the program\n""")

    user_menu_choice = input(">> ").strip()
    # user's input invalid
    while user_menu_choice not in MENU_CHOICES:
        print("Invalid input. Please try again")
        user_menu_choice = input("""    1 = start the quiz
    2 = repeat the introduction
    3 = quit the program

>>""").strip()

    # user selects 1
    if user_menu_choice == "1":
        print("You have selected 1.")

        # start program
        # print questions
        while repeat_test:  # repeats to the question instead of menu
            for counter in range(5):
                # should get random question through this
                question, answer = random.choice(list(QUESTIONS_ABOUT_DINO.items()))
                print("{}. {}?".format(counter+1, question))
                user_answer = input("enter your answer: ").strip()

                # if user got it correct, their score gets plus 1
                if user_answer.lower() == answer:
                    user_score += 1
                    print("Correct!\n")

                # user gets answer wrong, prints correct answer
                else:
                    print("""Wrong!
The correct answer is {}\n""".format(answer))

            # quiz is finished
            # scores will be given
            print("""You have done 5 questions!
your score is {} out of 5!\n""".format(user_score))

            time.sleep(2)  # pauses program for 2 seconds

            # user gets to pick whether to do more questions
            # or return to the menu or quit program
            retake_again = input("""
Would you like to take the test again?

    1 = get 5 more questions
    2 = return to menu
    3 = quit program

>> """).strip()

            # invalid user input
            while retake_again not in MENU_CHOICES:
                print("Invalid input. Please try again")
                retake_again = input("""    1 = continue with program
    2 = return to menu
    3 = quit program

>> """).strip()

            # restarts the quiz
            if retake_again == "1":
                print("test again")

            # goes back to the main menu
            elif retake_again == "2":
                print("back to menu")
                repeat_test = False
                continue

            # quits the program
            elif retake_again == "3":
                repeat_menu = False
                break

    # prints the information
    elif user_menu_choice == "2":
        print("(information will be printed)\n")

        time.sleep(2)  # pauses program for 2 seconds

        print("""The earliest dinosaurs appeared about 245 million years ago –
around the Triassic Period, the first period of the MESOZOIC ERA. This
was when most of the world’s land masses were still conjoined together,
making up the supercontinent PANGEA.

The word “DINOSAUR” came from the greek word, “Deinos Sauros” which basically
means TERRIBLE LIZARD.\n""")

        input("Enter any button to proceed: ")  # break for the user to read.

        print("""
Dinosaurs are mainly divided into two categories based on the structure
of the pelvis bone. These groups are called Saurischa (e.g., t-rex)  and Ornithischia
(e.g., stegosaurus). Though of course, dinosaurs could also be classified on their
diet, if they are meat lovers or green lovers. There are more dinosaurs that are
HERBIVORES than carnivores.

There are roughly around 700 valid dinosaur species that are named.
Dinosaurs are believed to have mostly died due to a METEOR. Though, I think, death
isn’t exactly the right term since dinosaurs pretty much just evolved into newer species;
most of them are birds.\n""")

        input("Enter any button to proceed: ")  # break for the user to read.

        print("""
Creatures that have lived longer than dinosaurs, that still exist till
this very day, are SHARKS! And also, Jurassic Park and World has been lying to you
because velociraptors are actually the size of a human TODDLER! They aren’t that big
at all.\n""")

        time.sleep(2)  # pauses program for 2 seconds

    # quits the program
    elif user_menu_choice == "3":
        print("quit")
        repeat_menu = False
        break
