# SPACE RANGERS QUESTS

from questsText import *

user_name = input("Ваше имя? > ")
inventory = []

def check_availability(lvl, choice_number):
  try:
    choice = int(choice_number)
    available_choices = all_texts[lvl][1]
    return available_choices >= choice
  except:
    return False

def decisions_tree(lvl):
  user_choice = input("> ")
  choice_available = check_availability(lvl, user_choice)

  if (user_choice) == "1" and choice_available:
    lvl += 1
  elif (user_choice) == "2" and choice_available:
    lvl += 2

  print(">>> lvl=",lvl)
  print(">>> all_Texts[lvl]=", all_texts[lvl])
  print_out(lvl, user_name)
  put_in_inventory(lvl)
  print_inventory()
  decisions_tree(lvl)

def print_out(lvl, *args):
  print(all_texts[lvl][0].format(*args))

def print_inventory():
  print("****Ваш инвентарь:****")

  if len(inventory) == 0: print("ВАШ ИНВЕНТАРЬ ПУСТ.")

  for item in inventory:
    print(f"{item}\n")

def put_in_inventory(lvl):
  if len(all_texts[lvl]) == 3:
    inventory.append(all_texts[lvl][2])

def start():
  decision_lvl = 0
  print_out(decision_lvl, user_name)
  decisions_tree(decision_lvl)

start()