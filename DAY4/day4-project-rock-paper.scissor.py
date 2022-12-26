"""
## Rock Paper Scissors

#### Instructions

**Make a rock, paper, scissors game.**

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

    How you will store the user's input.
    How you will generate a random choice for the computer.
    How you will compare the user's and the computer's choice to determine the winner (or a draw).
    And also how you will give feedback to the player.
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choose_people = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choose_computer = random.randint(0,2)

rps = [rock,paper,scissors]

print(f"You choose {rps[choose_people]}")
print(f"Computer choose {rps[choose_computer]}")


if choose_people == 0 and choose_computer == 2:
  print("You win!")
elif choose_computer == 0 and choose_people == 2:
  print("You lose")
elif choose_computer > choose_people:
  print("You lose")
elif choose_people > choose_computer:
  print("You win!")
elif choose_computer == choose_people:
  print("It's a draw")                             