import random

c_actions = ["rock", "paper", "scissors"]
u_action = input("Enter your choice (rock, paper or scissors): ")
u_action = u_action.lower()
c_action = random.choice(c_actions)

if u_action == c_action:
  print("Both players chose " + u_action + ", It's a tie!")
elif u_action == "rock":
  if c_action == "scissors":
    print("You chose " + u_action + ", Computer chose " + c_action + ", You win!")
  else:
    print("You chose " + u_action + ", Computer chose " + c_action + ", You lose!")
elif u_action == "paper":
  if c_action == "rock":
    print("You chose " + u_action + ", Computer chose " + c_action + ", You win!")
  else:
    print("You chose " + u_action + ", Computer chose " + c_action + ", You lose!")
elif u_action == "scissors":
  if c_action == "paper":
    print("You chose " + u_action + ", Computer chose " + c_action + ", You win!")
  else:
    print("You chose " + u_action + ", Computer chose " + c_action + ", You lose!")


