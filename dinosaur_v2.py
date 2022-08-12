"""
version: 2

Filename:  dinosaur.py
Author:  Heleina G.
Date:  6/07/22
Description: an informational test about dinosaurs. It will tell
you about dinosaurs and produce 10 random questions(among 15-20) for
you to answer. :)
"""

import random
import time

# initialize the dictionary
# dictionary = {key:value}
# key = questions, value = answers
QUESTIONS_ABOUT_DINO = {
    "THE DINOSAURS LIVED DURING THE ______ ERA":"mesozoic",
    "DINOSAURS ARE MAINLY DIVIDED INTO 2 CATEGORIES BASED ON THEIR ____ BONE":"pelvis",
    "ALL DINOSAURS DESCENDED FROM REPTILES CALLED ______":"archosaurs",
    "MOST DINOSAURS WERE ____":"herbivores",
    "WHAT CREATURE (THAT STILL CURRENTLY EXISTS) HAVE LIVED LONGER THAN DINOSAURS?":"sharks",
    "MOST SCIENTISTS BELIEVE THAT DINOSAURS DIED FROM A _____":"meteor",
    "WHAT DOES THE TERM 'DINOSAUR' MEAN?":"terrible lizard",
    "THERE ARE APPROXIMATELY ___ VALID DINOSAUR SPECIES":"300/900 idk yet",
    "WHAT WAS THE BIG SUPERCONTINENT CALLED?":"pangea",
    "TRUE OR FALSE: DID BIRDS EVOLVE FROM DINOSAURS":"true",
    "THE VELOCIRAPTORS ARE ACTUALLY THE SIZE OF A HUMAN ____":"toddler"}

# initialize the variables
repeat_menu = True
MENU_CHOICES = ["1", "2", "3"] 
# the scores and how many questions will be given
user_score = 0
amount_questions_given = len(QUESTIONS_ABOUT_DINO) # temporary. give only roughly 5



# information part about dinosaurs
# menu & introduction about dinosaurs



while repeat_menu:
    # introduction to the program; menu 
    print("""A very short informational quiz about your
favourite scary reptiles, the dinosaurs!! 

    1 = start the quiz
    2 = repeat the introduction
    3 = quit the program\n""") # temporary. more detailed

    user_menu_choice = input(">> ")

    while not user_menu_choice in MENU_CHOICES: 
        print("Invalid input. Please try again")
        user_menu_choice = input("""    1 = start the quiz
    2 = repeat the introduction
    3 = quit the program
        
>>""")


    # user selects 1
    if user_menu_choice == "1":
        print("You have selected 1.")

        # start program
        # print questions
        for question, answer in QUESTIONS_ABOUT_DINO.items():
            print(question)# i want the number before questions as well and the question randomly
            user_answer = input("enter your answer: ")

            # if user got it correct, their score gets plus 1
            if user_answer.lower() == answer: #doesn't work
                user_score +=1
                print("Correct")

            else:
                print("Wrong.")

        print("""You have done 5 questions!
your score is {} out of {}""".format(user_score,amount_questions_given))

    elif user_menu_choice == "2":
        print("print the information psl")

    elif user_menu_choice == "3":
        print("quit")
        repeat_menu = False
        break

    
        
