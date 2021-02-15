import random
import os
from dotenv import load_dotenv

print("-------------------")

load_dotenv()
PLAYER_NAME = os.getenv("USER_NAME", default="Player One") #gets username from .env file.
print("Welcome " + PLAYER_NAME + "!")

print("-------------------")

rps = ["rock", "paper", "scissors"]

user_input = ""
#loops until user input is correct. 
while(user_input not in rps): 
    print("Type \"Rock\", \"Paper\", or \"Scissors\": ", end='')
    user_input = input().lower() #formats and stores user input.
print("You chose \"" + user_input.capitalize() + "\".")

print("-------------------")

cpu_input = random.choice(rps) #stores random selection.
print("Your opponent chose \"" + cpu_input.capitalize() + "\".")

print("-------------------")

#matches inputs/selections with possible outcomes.
if (user_input, cpu_input) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
    print("You win!")
elif user_input == cpu_input:
    print("You tied.")
else:
    print("You lose.")

print("-------------------")

print("Good game! Thanks for playing.")
 