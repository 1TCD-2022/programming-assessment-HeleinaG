"""
version: 1

Filename:  dinosaur.py
Author:  Heleina G.
Date:  6/07/22
Description: an informational test about dinosaurs. It will tell
you about dinosaurs and produce 10 random questions(among 15-20) for
you to answer. :)
"""

# initialize the dictionary
# dictionary = {key:value}
# key = questions, value = answers
QUESTIONS_ABOUT_DINO = {
    "question 1":"answer 1",
    "question 2":"answer 2"}



# initialize the variables
REPEAT_MENU = True
MENU_CHOICES = ["1", "2"] # temporary. 3 choices
# the scores and how many questions will be given
user_score = 0
amount_questions_given = len(QUESTIONS_ABOUT_DINO) # temporary. give only 5 random



# introduction to the program; menu
while REPEAT_MENU:
    print("""introduction abt dinosaurs rawr rawr.
Would you like to try my quiz out?

1 = yes
2 = no\n""") # temporary. more detailed
    user_menu_choice = input(">> ")

    # if user option is not 1-2, will be asked to re-enter
    while not user_menu_choice in MENU_CHOICES: 
        print("Invalid input. Please try again")
        user_menu_choice = input("""1 = yes
2 = no
        
>>""")


    # user has selected 1
    if user_menu_choice == "1":
        print("You have selected 1.")

        # start program
        # print questions
        for i in range(amount_questions_given):

            question, answer = QUESTIONS_ABOUT_DINO.popitem()
            # key = questions, value = answer
            print(question) # i want the number before questions as well
            user_answer = input("enter your answer: ")

            # if user got it correct, their score gets plus 1
            if user_answer == answer:
                user_score +=1
                print("Correct")

            else:
                print("Wrong.")

    # user has selected 2
    # quit the program (for now)
    elif user_menu_choice == "2":
        print("You have selected 2. Quitting program.")
        REPEAT_MENU = False
        break
            

    
        
