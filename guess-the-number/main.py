import random
from art import logo



#difficulty selection
def play_game():

    Difficuly = input("Chose you difficulty type 'easy' or 'hard':")
    the_number = random.randint(1, 101)

    if Difficuly == 'hard':
        lives = 5
    elif Difficuly == 'easy':
        lives = 10
    else:
        lives = 0
        print("invalid input")

    #gameon
    flag = 0
    while lives >= 1:
        flag = 1
        user = int(input(f"Your have {lives} remaining.Guess the Number: "))
        if user == the_number:
            print(f"You win. The number was {the_number}")
            break
        elif user < the_number:
            print("Too Low")
            lives -= 1
        elif user > the_number:
            print("Too High")
            lives -= 1

    if lives == 0 and flag == 1:
        print(f"you lost.the number was {the_number}")


#intro
print(logo)
print("Welcome To Number Guessing Game.")
print("Number Will Be Picked From 1 to 100.")
print("Your Task is To Guess The Number.")

while input("Want To Play The Game? type 'y' to play or type 'n':") == 'y':
    play_game()
    
