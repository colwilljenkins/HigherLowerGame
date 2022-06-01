from art import logo
from art import vs
from game_data import data
import random
from replit import clear



print(logo)
current_score = 0
celebA = random.randint(0, 49)
celebB = random.randint(0, 49)
while celebB == celebA:
  celebB = random.randint(0, 49)
  


def play_game():
  #accessing score
  global current_score
  global celebA, celebB
  #showing statement of score if not first round  
  if current_score > 0:
    print(f'You are right! Your current score is: {current_score}')
    #changing round so have continuity
    celebA = celebB
    while celebB == celebA:
      celebB = random.randint(0, 49)
      
  #showing celebrity data
  print(f"Compare A: {(data[celebA]['name'])}, a {(data[celebA]['description'])}, from {(data[celebA]['country'])} ")
  print(vs)
  print(f"With B: {(data[celebB]['name'])}, a {(data[celebB]['description'])}, from {(data[celebB]['country'])} ")
  #user choice of a or b 
  user_input = input("\nWho has more followers?\nWrite 'A' or 'B':\n")
  #consequences of choice
  if user_input == 'A':
    if data[celebA]['follower_count'] > data[celebB]['follower_count']:
      current_score +=1
      clear()
      print(logo)
      play_game()
    else:
      clear()
      print(logo)
      print(f"Sorry that's wrong, final score: {current_score}")
  elif user_input == 'B':
    if data[celebB]['follower_count'] > data[celebA]['follower_count']:
      current_score +=1
      clear()
      print(logo)
      play_game()
    else:
      clear()
      print(logo)
      print(f"Sorry that's wrong, final score: {current_score}")

play_game()
