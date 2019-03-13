def pick_up_quest():
  all_lines_formatted = []
  available_quests = ['menzols']
  print("Какой квест вы хотите пройти?")
  print("Доступны квесты: ", available_quests)
  chosen_quest = input("> ")

  if available_quests.__contains__(chosen_quest):
    all_quest_lines = read_all_quest(chosen_quest)
    all_lines_formatted = format_all_lines(all_quest_lines)
    return all_lines_formatted
  else:
    return pick_up_quest()
  

def read_all_quest(quest_name):
  txt = open(f"{quest_name}.txt", encoding='utf-8')
  all_lines = txt.read().split('\n')
  
  txt.close()
  return all_lines

def format_all_lines(all_lines):
  formatted_lines = []
  for line in all_lines:
    formatted_lines.append(get_formated_line(line))

  return formatted_lines

def get_formated_line(text_line):
  next_steps = text_line.split('*next_step*')
  string = ''.join(next_steps[0])
  next_steps.pop(0)

  if text_line.__contains__('*inventory*'):
    inventory = next_steps.pop()
    inventory = inventory.replace('*inventory*', '')
  else:
    inventory = ''
    next_steps.pop()
  
  next_steps = next_steps[0].split(',')

  string = string.replace('*-*', '\n')
  string = string.replace('*next_step*', '')
  string = string.replace('*inventory*', '')

  return [string, next_steps, inventory]