import random

print("Welcome!")

user_input = ""
while(user_input not in ["rock", "paper", "scissors"]):
    print("Type \"Rock\", \"Paper\", or \"Scissors\"")
    user_input = input().lower()

cpu_input = random.choice(["rock", "paper", "scissors"])

print("You chose \"" + user_input.capitalize() + "\"")
print("Your opponent chose \"" + cpu_input.capitalize() + "\"")

inputs = (user_input, cpu_input)
wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
ties = [("rock", "rock"), ("scissors", "scissors"), ("paper", "paper")]

if inputs in wins:
    print("You win!")
elif inputs in ties:
    print("You tied.")
else:
    print("You lose.")

print("Good game!")
