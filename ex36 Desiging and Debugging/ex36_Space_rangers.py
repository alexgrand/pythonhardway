# SPACE RANGERS QUESTS

from sys import exit
from questsText import *

user_name = input("Ваше имя? > ")
inventory = []

def start():
  decision_tree(0, user_name)

def print_all_text(index, f_string):
  print(all_texts[index][0].format(f_string))

def decision_tree(index, f_string):
  print_all_text(index, f_string)
  get_inventory(index)
  user_choice = input("> ")

  try:
    user_choice = int(user_choice)

    if user_choice < len(all_texts[index]) and user_choice != 0:
      user_choice = all_texts[index][user_choice]
    else:
      user_choice = index

    decision_tree(user_choice, f_string)

  except:
    if user_choice == 'exit':
      return
    
    print(">>> Если вы хотите выйти напишите exit")
    decision_tree(index, f_string)

def get_inventory(index):
  for item in all_inventory:
    if item[0] == index and not inventory.__contains__(item[1]):
      inventory.append(item[1])

  if len(inventory) > 0:
    print("У вас есть: ")
    # for item in inventory:
    #   print(item)
    print(inventory)


start()