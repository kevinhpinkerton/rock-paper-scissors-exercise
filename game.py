import random
import os
from dotenv import load_dotenv

print("-------------------")

load_dotenv()
user = os.getenv("USER_NAME", default="Player One") #gets username from .env file.
print("Welcome " + user + "!")

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

inputs = (user_input, cpu_input) #groups both selections.
#possible outcomes:
wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
ties = [("rock", "rock"), ("scissors", "scissors"), ("paper", "paper")]

#matches selections with possible outcomes.
if inputs in wins:
    print("You win!")
elif inputs in ties:
    print("You tied.")
else:
    print("You lose.")

print("-------------------")

print("Good game! Thanks for playing.")
 