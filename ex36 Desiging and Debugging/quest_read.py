
def pick_up_quest():
  available_quests = ['menzols']
  print("Какой квест вы хотите пройти?")
  print("Доступны квесты: ", available_quests)
  chosen_quest = input("> ")

  is_available = check_quest_availability(available_quests, chosen_quest)

  if is_available:
    all_quest_lines = read_all_quest(chosen_quest)
    return format_all_lines(all_quest_lines)

  else:
    print("Такого квеста пока нет!")
    pick_up_quest()



def check_quest_availability(all_quests, quest_name):
  if all_quests.__contains__(quest_name):
    return True
  return False

def read_all_quest(quest_name):
  txt = open(f"{quest_name}.txt", encoding='utf-8')
  all_lines = txt.read().split('\n')
  
  txt.close()
  return all_lines

def format_all_lines(all_lines):
  formatted_lines = []
  for line in all_lines:
    formatted_lines.append(format_line(line))

  return formatted_lines

def format_line(text_line):
  string_and_steps = get_formated_arr(text_line, '*next_step*')
  string = string_and_steps[0]
  next_steps = string_and_steps[1]

  string_and_inventory = get_formated_arr(string, '*inventory*')
  string = string_and_inventory[0]
  inventory = string_and_inventory[1]
  
  string = string.replace('*-*', '\n')
  string = string.replace('*next_step*', '')
  string = string.replace('*inventory*', '')

  return [string, next_steps, inventory]

def get_formated_arr(text_line, form):
  formated_string = text_line.split(form)
  string = ''.join(formated_string[0])
  formated_string.pop(0)

  return [string, formated_string]



pick_up_quest()