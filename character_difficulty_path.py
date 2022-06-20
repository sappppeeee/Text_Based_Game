# Text Base Game
# character/difficulty path file
# Mohammed Shourov
# 6-4-2022
# ITCS 1950 V0801 2022SS - Intro to Game Development
# character/difficulty path  

# imports module
import string
import random
import time

# warrior path
def math_problems_warrior(difficulty_setting):
	
  needed_right_guessed = 3
  needed_wrong_guessed = 3

  # Counters
  wrong_guessed = 0
  right_guessed = 0
  # Math
  while right_guessed < needed_right_guessed and wrong_guessed < needed_wrong_guessed:
    numList = [1,2,3,4,5,6,7,8,9]
    num1 = random.choice(numList)
    num2 = random.choice(numList)
  # Easy
    if difficulty_setting == 'easy':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Easy = ['+','-']
      random_operations_Easy = random.choice(operations_Easy)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Easy,' ', num2,' ?')
    # random operations 
      if random_operations_Easy == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Easy == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Medium
    if difficulty_setting == 'medium':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Medium = ['+','-','*']
      random_operations_Medium = random.choice(operations_Medium)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Medium,' ', num2,' ?')
    # random operations 
      if random_operations_Medium == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Medium == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Medium == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Hard
    if difficulty_setting == 'hard':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Hard = ['+','-','*','/']
      random_operations_Hard = random.choice(operations_Hard)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Hard,' ', num2,' ?')
    # random operations 
      if random_operations_Hard == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Hard == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '/':
        not_rounded_answer = num1 / num2
        # print(not_rounded_answer)
        answer = round(not_rounded_answer,2)
        # print('-----------------------',answer,'-----------------------')
        time.sleep(2)
        print("Round The Answer By 2 Decimals")
        print("Example : 0.33333333 should be 0.33")
        player_answer = float(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          
          print('Wrong Guessed: ', wrong_guessed)
  # Wrong Input
    if difficulty_setting != 'easy' and difficulty_setting != 'medium' and difficulty_setting != 'hard':
      time.sleep(2)
      print('Wrong Input?')
      right_guessed = right_guessed + 1
  # won
    if right_guessed == needed_right_guessed:
      time.sleep(2)
      print('Congratulations, you have Won!!!!!!!')
      print('Congratulations, you have Won!!!!!!!')
  # loss
    if wrong_guessed == needed_wrong_guessed:
      time.sleep(2)
      print('Congratulations, you have lost!!!!!!')
      time.sleep(2)
      print('Good Luck Next Time')

# assassin path
def math_problems_assassin(difficulty_setting):
	
  needed_right_guessed = 3
  needed_wrong_guessed = 2

  # Counters
  wrong_guessed = 0
  right_guessed = 0
  # Math
  while right_guessed < needed_right_guessed and wrong_guessed < needed_wrong_guessed:
    numList = [1,2,3,4,5,6,7,8,9]
    num1 = random.choice(numList)
    num2 = random.choice(numList)
  # Easy
    if difficulty_setting == 'easy':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Easy = ['+','-']
      random_operations_Easy = random.choice(operations_Easy)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Easy,' ', num2,' ?')
    # random operations 
      if random_operations_Easy == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Easy == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Medium
    if difficulty_setting == 'medium':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Medium = ['+','-','*']
      random_operations_Medium = random.choice(operations_Medium)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Medium,' ', num2,' ?')
    # random operations 
      if random_operations_Medium == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Medium == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Medium == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Hard
    if difficulty_setting == 'hard':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Hard = ['+','-','*','/']
      random_operations_Hard = random.choice(operations_Hard)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Hard,' ', num2,' ?')
    # random operations 
      if random_operations_Hard == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Hard == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '/':
        not_rounded_answer = num1 / num2
        # print(not_rounded_answer)
        answer = round(not_rounded_answer,2)
        # print('-----------------------',answer,'-----------------------')
        time.sleep(2)
        print("Round The Answer By 2 Decimals")
        print("Example : 0.33333333 should be 0.33")
        player_answer = float(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          
          print('Wrong Guessed: ', wrong_guessed)
  # Wrong Input
    if difficulty_setting != 'easy' and difficulty_setting != 'medium' and difficulty_setting != 'hard':
      time.sleep(2)
      print('Wrong Input?')
      right_guessed = right_guessed + 1
  # won
    if right_guessed == needed_right_guessed:
      time.sleep(2)
      print('Congratulations, you have Won!!!!!!!')
      print('Congratulations, you have Won!!!!!!!')
  # loss
    if wrong_guessed == needed_wrong_guessed:
      time.sleep(2)
      print('Congratulations, you have lost!!!!!!')
      time.sleep(2)
      print('Good Luck Next Time')

# mage path
def math_problems_mage(difficulty_setting):
	
  needed_right_guessed = 4
  needed_wrong_guessed = 3

  # Counters
  wrong_guessed = 0
  right_guessed = 0
  # Math
  while right_guessed < needed_right_guessed and wrong_guessed < needed_wrong_guessed:
    numList = [1,2,3,4,5,6,7,8,9]
    num1 = random.choice(numList)
    num2 = random.choice(numList)
  # Easy
    if difficulty_setting == 'easy':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Easy = ['+','-']
      random_operations_Easy = random.choice(operations_Easy)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Easy,' ', num2,' ?')
    # random operations 
      if random_operations_Easy == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Easy == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Medium
    if difficulty_setting == 'medium':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Medium = ['+','-','*']
      random_operations_Medium = random.choice(operations_Medium)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Medium,' ', num2,' ?')
    # random operations 
      if random_operations_Medium == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Medium == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Medium == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Hard
    if difficulty_setting == 'hard':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Hard = ['+','-','*','/']
      random_operations_Hard = random.choice(operations_Hard)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Hard,' ', num2,' ?')
    # random operations 
      if random_operations_Hard == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Hard == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '/':
        not_rounded_answer = num1 / num2
        # print(not_rounded_answer)
        answer = round(not_rounded_answer,2)
        # print('-----------------------',answer,'-----------------------')
        time.sleep(2)
        print("Round The Answer By 2 Decimals")
        print("Example : 0.33333333 should be 0.33")
        player_answer = float(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          
          print('Wrong Guessed: ', wrong_guessed)
  # Wrong Input
    if difficulty_setting != 'easy' and difficulty_setting != 'medium' and difficulty_setting != 'hard':
      time.sleep(2)
      print('Wrong Input?')
      right_guessed = right_guessed + 1
  # won
    if right_guessed == needed_right_guessed:
      time.sleep(2)
      print('Congratulations, you have Won!!!!!!!')
      print('Congratulations, you have Won!!!!!!!')
  # loss
    if wrong_guessed == needed_wrong_guessed:
      time.sleep(2)
      print('Congratulations, you have lost!!!!!!')
      time.sleep(2)
      print('Good Luck Next Time')

# berserker path
def math_problems_berserker(difficulty_setting):
	
  needed_right_guessed = 5
  needed_wrong_guessed = 5

  # Counters
  wrong_guessed = 0
  right_guessed = 0
  # Math
  while right_guessed < needed_right_guessed and wrong_guessed < needed_wrong_guessed:
    numList = [1,2,3,4,5,6,7,8,9]
    num1 = random.choice(numList)
    num2 = random.choice(numList)
  # Easy
    if difficulty_setting == 'easy':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Easy = ['+','-']
      random_operations_Easy = random.choice(operations_Easy)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Easy,' ', num2,' ?')
    # random operations 
      if random_operations_Easy == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Easy == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Medium
    if difficulty_setting == 'medium':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Medium = ['+','-','*']
      random_operations_Medium = random.choice(operations_Medium)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Medium,' ', num2,' ?')
    # random operations 
      if random_operations_Medium == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Medium == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Medium == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
  # Hard
    if difficulty_setting == 'hard':
      time.sleep(2)
      print('You have picked: ',difficulty_setting,' Difficulty Setting')
      operations_Hard = ['+','-','*','/']
      random_operations_Hard = random.choice(operations_Hard)
      time.sleep(2)
      print("what's ", num1,' ', random_operations_Hard,' ', num2,' ?')
    # random operations 
      if random_operations_Hard == '+':
        answer = num1 + num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations      
      if random_operations_Hard == '-':
        answer = num1 - num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '*':
        answer = num1 * num2
        player_answer = int(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          time.sleep(2)
          print('Wrong Guessed: ', wrong_guessed)
    # random operations 
      if random_operations_Hard == '/':
        not_rounded_answer = num1 / num2
        # print(not_rounded_answer)
        answer = round(not_rounded_answer,2)
        # print('-----------------------',answer,'-----------------------')
        time.sleep(2)
        print("Round The Answer By 2 Decimals")
        print("Example : 0.33333333 should be 0.33")
        player_answer = float(input("      :"))
      # Right
        if player_answer == answer:
          time.sleep(2)
          print("You've guessed it right!!!")
          print('-----------------------',answer,'-----------------------')
          right_guessed = right_guessed + 1
          time.sleep(2)
          print('Right Guessed: ',right_guessed)
      # Wrong
        if player_answer != answer:
          time.sleep(2)
          print("You've guessed it wrong!")
          print('-----------------------',answer,'-----------------------')
          wrong_guessed = wrong_guessed + 1
          
          print('Wrong Guessed: ', wrong_guessed)
  # Wrong Input
    if difficulty_setting != 'easy' and difficulty_setting != 'medium' and difficulty_setting != 'hard':
      time.sleep(2)
      print('Wrong Input?')
      right_guessed = right_guessed + 1
  # won
    if right_guessed == needed_right_guessed:
      time.sleep(2)
      print('Congratulations, you have Won!!!!!!!')
      print('Congratulations, you have Won!!!!!!!')
  # loss
    if wrong_guessed == needed_wrong_guessed:
      time.sleep(2)
      print('Congratulations, you have lost!!!!!!')
      time.sleep(2)
      print('Good Luck Next Time')