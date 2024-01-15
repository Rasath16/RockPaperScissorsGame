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

while True:
  print("Welcome to the Rock, Paper, Scissors Game")
  choice = int(input("What do you chose? Type 1 for Rock, 2 for Paper, 3 for Scissor.\n"))
  print ("You Chose :")
  if choice == 1:
    print(rock)
  if choice == 2 :
    print(paper)
  if choice == 3:
    print(scissors)
  else:
    print("Please enter a valid number")
  print ("Computer Chose :")
  random_number= random.randint(1,3)
  if random_number == 1:
    print(rock)
  if random_number == 2:
    print(paper)
  if random_number == 3:
    print(scissors)

  if choice == 1 and random_number == 1:
    print ("DRAW")
  if choice == 1 and random_number ==2 :
    print ("YOU LOSE")
  if choice == 1 and random_number ==3 :
    print ("YOU WON")
  if choice == 2 and random_number ==1 :
    print ("YOU WON")
  if choice == 2 and random_number ==2 :
    print ("DRAW")
  if choice == 2 and random_number ==3 :
    print ("YOU LOSE")
  if choice == 3 and random_number ==1 :
    print ("YOU LOSE")
  if choice == 3 and random_number ==2 :
    print ("YOU WON")
  if choice == 3 and random_number ==3 :
    print ("DRAW")

  play_again = input("Do you want to play again? Type 'yes' to continue or any other key to exit.\n")

  if play_again.lower() != 'yes':
    print("Thanks for playing!")
    break