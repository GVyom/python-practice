#Day 4 of 100 Days of Code
#Topics covered:
#Nested lists, logical operators, randomisation, index errors
#modules - pre written code that we can import and use in our program - random is one of the module in python that we can use to generate random numbers, random choices etc. We will be using this module to make a rock paper scissors game

import random
gx_choice = input("rock, paper, scissors?: ").lower()
variables = ["rock","paper","scissors"]
co_choice = random.choice(variables)

print(gx_choice)
print(co_choice)

if gx_choice == "rock" and co_choice == "paper":
    print("You lose")
elif gx_choice == "rock" and co_choice == "scissors":
    print("You win")
elif gx_choice == "paper" and co_choice == "rock":
    print("You win")
elif gx_choice == "paper" and co_choice == "scissors":  
    print("You lose")
elif gx_choice == "scissors" and co_choice == "rock":
    print("You lose")
elif gx_choice == "scissors" and co_choice == "paper":
    print("You win")
elif gx_choice == co_choice:
    print("It's a draw")
else:
    print("Please put input in valid format")