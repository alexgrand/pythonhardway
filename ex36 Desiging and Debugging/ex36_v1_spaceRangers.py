from quest_read import pick_up_quest


def get_quest_elements(raw_data):
  texts = []
  steps = []
  inventory = []

  for line in raw_data:
    texts.append(line[0])  
    steps.append(line[1])
    inventory.append(line[2])
  
  return [texts, steps, inventory]

def print_line(arr, index):
  if arr == all_inventory:
    print("У вас есть: ")
  print(arr[index].format(user_name))

def make_decision(index):
  print_line(all_texts, index)
  check_inventory(index)
  print_inventory()
  user_choice = input("> ")

  try:
    user_choice = int(user_choice)

    if user_choice <= len(all_steps[index]) and user_choice != 0:
      user_choice = int(all_steps[index][user_choice - 1])
    else:
      user_choice = index

    make_decision(user_choice)

  except:
    if user_choice == 'exit':
      return
    
    print("Введите правильный вариант или exit")
    make_decision(index)


def check_inventory(index):
  if index != 0 and not my_inventory.__contains__(all_inventory[index]):
    if all_inventory[index] != '':
      my_inventory.append(all_inventory[index])

def print_inventory():
  if len(my_inventory) > 0:
    print("У вас есть:")
    print(my_inventory)

def start():
  global all_texts, all_steps, all_inventory, user_name, my_inventory
  all_quest = pick_up_quest()

  user_name = input("Введите ваше имя: ")

  all_quest_lines = get_quest_elements(all_quest)
  all_texts = all_quest_lines[0]
  all_steps = all_quest_lines[1]
  all_inventory = all_quest_lines[2]
  my_inventory = []
  make_decision(0)


start()