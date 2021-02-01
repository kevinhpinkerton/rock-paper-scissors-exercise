import random
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("USER_NAME", default="Player One")

print("-------------------")

print("Welcome " + user + "!")

print("-------------------")

user_input = ""
while(user_input not in ["rock", "paper", "scissors"]):
    print("Type \"Rock\", \"Paper\", or \"Scissors\": ", end='')
    user_input = input().lower()
print("You chose \"" + user_input.capitalize() + "\"")

print("-------------------")

cpu_input = random.choice(["rock", "paper", "scissors"])
print("Your opponent chose \"" + cpu_input.capitalize() + "\"")

print("-------------------")

inputs = (user_input, cpu_input)
wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
ties = [("rock", "rock"), ("scissors", "scissors"), ("paper", "paper")]

if inputs in wins:
    print("You win!")
elif inputs in ties:
    print("You tied.")
else:
    print("You lose.")

print("-------------------")

print("Good game! Thanks for playing.")
 