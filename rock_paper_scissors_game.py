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

import random

computer_choice = random.randint(1, 3)
computer_choice -= 1
human_choice = int(input("What do you choose? Type 0 for Rock. 1 for Paper or 2 for Scissors.  "))

if human_choice == 0:
    print(f'you choose:\n{rock}')
elif human_choice == 1:
    print(f'you choose:\n{paper}')
elif human_choice == 2:
    print(f'you choose:\n{scissors}')

if computer_choice == 0:
    print(f'computer choose:\n{rock}')
elif computer_choice == 1:
    print(f'computer choose:\n{paper}')
elif computer_choice == 2:
    print(f'computer choose:\n{scissors}')


if human_choice == 0 and computer_choice == 2:
    print('You win')
elif human_choice == 2 and computer_choice == 1:
    print('You win')
elif human_choice == 1 and computer_choice == 0:
    print("You win")
elif human_choice == computer_choice:
    print("It is a draw")
else:
    print("You lose")
