options=["stone","paper","scissors"]

import random

user_choice=None
win=0
for i in range(5):
    comp_choice=random.choice(options)
    while True:
        try:
            user=int(input("Enter a number between 1 & 3:\n1. Stone\n2. Paper\n3. Scissors\n\n"))
            if user in range(1,4):
                break
            else:
                print("\nTry again\n")
        except:
            print("\nTry again\n")
    if user==1:
        user_choice="stone"
    elif user==2:
        user_choice="paper"
    else:
        user_choice="scissors"
    print("\nYou chose", user_choice, "& System chose",comp_choice)
    if user_choice==comp_choice:
        print("Draw")
    elif user_choice=="stone" and comp_choice=="scissors" or user_choice=="paper" and comp_choice=="stone" or user_choice=="scissors" and comp_choice=="paper":
        print("You win")
        win=win+1
    else:
        print("You lose")
if win>2:
    print(f"You won {win} times. You won the match.")
else:
    print(f"You won {win} times. You lost the match.")


