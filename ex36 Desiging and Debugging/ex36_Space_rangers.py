# SPACE RANGERS QUESTS

from sys import exit
from questsText import *

user_name = input("Ваше имя? > ")
inventory = []

def start():
  decision_tree(0, user_name)

def print_one_text(index, str_format):
  print(all_texts[index][0].format(str_format))

def decision_tree(index, str_format):
  print_one_text(index, str_format)
  user_choice = input("> ")

  try:
    user_choice = int(user_choice)

    if user_choice < len(all_texts[index]) and user_choice != 0:
      user_choice = all_texts[index][user_choice]
    else:
      user_choice = index

    decision_tree(user_choice, str_format)

  except:
    if user_choice == 'exit':
      return
    
    print(">>> Если вы хотите выйти напишите exit")
    decision_tree(index, str_format)

start()