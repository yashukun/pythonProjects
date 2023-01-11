from game_data import data
import random
from replit import clear
from art import vs
from art import logo

#random pick from game data
the_dick = (random.choice(data))
user_score = 0
loop = 0

def game():
  global the_dick
  global user_score
  global loop
  print(logo)
  if loop > 0:
    print(f"Your current score: {user_score}")
  the_dick2 = (random.choice(data))
  

  
  print(f"Compare A: {the_dick['name']}, {the_dick['description']}, from {the_dick['country']}")

  print(vs)
  
  print(f"Against B: {the_dick2['name']}, {the_dick2['description']}, from {the_dick2['country']}")
  
  #ans mill gya
  if the_dick['follower_count'] > the_dick2['follower_count']:
    ans = 'A'
  else:
    ans = 'B'
  
  #swaping
  the_dick = the_dick2
  #user score and 
  
  
  user_input = input("Who has more followers?:Type 'A' or 'B':")
  
  
  if user_input == ans:
    user_score += 1
    loop = 1
    clear()
    game()
  else:
    print(f"Your final score {user_score}")
    

game()
  
