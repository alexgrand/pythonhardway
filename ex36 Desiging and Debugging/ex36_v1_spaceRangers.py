from quest_read import pick_up_quest


def get_quest_elements(raw_data):
  global all_texts, all_steps, all_inventory, my_inventory
  all_texts = []
  all_steps = []
  all_inventory = []
  my_inventory = []

  for line in raw_data:
    all_texts.append(line[0])  
    all_steps.append(line[1])
    all_inventory.append(line[2])


def print_line(arr, index):
  if arr == all_inventory:
    print("У вас есть: ")
  print(arr[index].format(user_name))

def make_decision(index):
  print("________________________________________________________")
  print("________________________________________________________")
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
  global user_name
  all_quest = pick_up_quest()

  user_name = input("Введите ваше имя: ")

  get_quest_elements(all_quest)
  make_decision(0)


start()