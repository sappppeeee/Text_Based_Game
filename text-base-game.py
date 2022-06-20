# Text Base Game
# Mohammed Shourov
# 6-4-2022
# ITCS 1950 V0801 2022SS - Intro to Game Development
# Homework 6 

# Imports module
import random
import time
import string
import sys

# Importing from character/difficulty path file
from character_difficulty_path import *

# line formating function
def line_formating_function():
  print('------------------------------------------------------------------------')

# intro function
def intro():
  print('------------------------------------------------------------------------')
  print('--------------------------Dungeons And Bosses---------------------------')
  print('''Imagine if you are summoned into a medieval world as an adventurer,
who has been exlporeing dungeons, leveling up and becoming more 
powerful to reach the end of the dungeons to conquer it. And you 
have finaly reached the last level/boss. And  you don't know what 
to expect as your going into theboss room.''')
  # put a time delay
  time.sleep(2)
  print('''This text-based game revolves around you solving math problems
to defeating the RPG boss. The program will randomly pick a boss
for you (from Black Dragon, Hell Hound, and The White Witch).
First, you will enter your name into the program. Then, you
will input the difficulty level to determine the difficulty of
the math problems(From Easy =+,- / Medium = +,-,* / Hard = +,-,*, %).
Then you will have to choose Class or Character.''')
  print('------------------------------------------------------------------------')
  # put a time delay
  time.sleep(2)
  print('------------------------------Ganme Rules:------------------------------')
  print('Get 3 righ answer to defeat the Boss')
  print('''Pick difficulty : Easy / Medium / Hard
                :  +,- /  +,-,* / +,-,*,/''')
  # put a time delay
  time.sleep(2)
  print('''  Pick class/     : Warrior, Assassin
  character       : Mage and Berserker.''')
  print('------------------------------------------------------------------------')
  print('PLZ ENTER EVERYTHING WITH THE RIGHT SPELLING')
  time.sleep(2)
  print('PLZ ENTER EVERYTHING WITH THE RIGHT SPELLING')
  print('PLZ ENTER EVERYTHING WITH THE RIGHT SPELLING')
  time.sleep(2)
  print('PLZ ENTER EVERYTHING WITH THE RIGHT SPELLING')
  print('------------------------------------------------------------------------')

# Time Delay function 
def timedelay():
  time.sleep(2)
  print('------------------------------------------------------------------------')
  print('------------------------------------------------------------------------')

# name function 
def name_print(playername):
  print('              Welcome Dungeons And Bosses:', playername)

# random_boss function
def random_boss():
  print('Randomly spawning A Boss...')
  # put a time delay
  time.sleep(2)
  randomboss1 = random.randint(1, 3) #randomize the boss
  if 1 == randomboss1:
    print('-------------------------------Hell Hound-------------------------------')
  if 2 == randomboss1:
    print('----------------------------The White Witch-----------------------------')
  if 3 == randomboss1:
    print('------------------------------Black Dragon------------------------------')

# character selection
def character_selection_print():
  print('                          Now Pick A Character                          ')
  print('                Warrior or Assassin or Mage or Berserker                ')

# character selection print statments
def character_selection(character_selected, playername):
  print('----> ',playername,' Have Picked: ', character_selected)
  print('------------------------------------------------------------------------')

# math problems print statements function
def math_problems(difficulty_setting, character_selected, playername):
  time.sleep(2)
  print('------------------------------------------------------------------------')
  print(playername,'You have picked:')
  print('            difficulty: ',difficulty_setting)
  print('             character: ', character_selected)
  print('                       Starting the Math Problems                       ')

# call all function
def callallfunction():
  # intro
  intro()
  #time delay
  timedelay()
  # name input
  playername = input('Enter Your Game Name:').upper()
  # name output
  name_print(playername)
  # line formating function
  line_formating_function()
  # random boss 
  random_boss()
  # line formating function
  line_formating_function()
  # difficulty input
  difficulty_setting = input('Pick difficulty : Easy / Medium / Hard'+': ').lower()
  # line formating function
  line_formating_function()
  # character info
  character_selection_print()
  # character input
  character_selected = input('Enter Your Character: ').lower()
  # character output
  character_selection(character_selected, playername)
  
  # character/difficulty path 
  # warrior path
  if character_selected == 'warrior':
    math_problems(difficulty_setting, character_selected, playername)
    # line formating function
    line_formating_function()
    math_problems_warrior(difficulty_setting)
  
  # assassin path
  if character_selected == 'assassin':
    math_problems(difficulty_setting, character_selected, playername)
    # line formating function
    line_formating_function()
    math_problems_assassin(difficulty_setting)
  
  # mage path
  if character_selected == 'mage':
    math_problems(difficulty_setting, character_selected, playername)
    # line formating function
    line_formating_function()
    math_problems_mage(difficulty_setting)
  
  # berserker path
  if character_selected == 'berserker':
    math_problems(difficulty_setting, character_selected, playername)
    # line formating function
    line_formating_function()
    math_problems_berserker(difficulty_setting)

  if character_selected == 'berserker' and character_selected == 'assassin' and character_selected == 'mage' and character_selected == 'berserker':
      print('Wrong Input?')
      print('Wrong Input?')

# main Function
def main():
  line_formating_function()
  line_formating_function()
  
  print('''While This Program is Running, If You Were to Enter a INCORRECT INPUT:
It will bring you back to this line "Enter Yes or No 
To Run The Program: ", Unless, If it's a  TypeError''')
  time.sleep(2)
  
  # To Allow the User to Start and Restart the Program
  while True:
    #  Input to Run The Program
    program_run = input("Enter Yes or No To Run The Program: ").lower()
    #  Loop through the input
    if program_run == "yes":
      time.sleep(2)
      callallfunction()
      continue
    elif program_run == "no":
      time.sleep(2)
      print('Terminating Program............')
      time.sleep(5)
      break
    else:
      time.sleep(2)
      print("Enter Either         ---->    Yes Or No")
      print("To Quite             ---->    Enter Either No")



  line_formating_function()
  line_formating_function()

main()