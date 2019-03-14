def pick_up_quest():
  all_lines_formatted = []
  available_quests = ['menzols1']
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
  all_lines = txt.read()
  
  txt.close()
  return all_lines

def format_all_lines(all_lines):
  quest_text = format_line(all_lines, '*quest_text*')
  quest_steps = format_line(all_lines, '*quest_steps*')
  quest_inventory = format_line(all_lines, '*quest_inventory*')

  f_quest_text = format_text(quest_text)
  f_quest_steps = format_data(quest_steps)
  f_quest_inventory = format_data(quest_inventory)

  print(">>> f_quest_inventory=", f_quest_inventory)

  return [f_quest_text, f_quest_steps, f_quest_inventory]

def format_line(all_lines, formatter):
  formatted_line = all_lines.split(formatter)
  
  return formatted_line[1]

def format_text (text):
  text = text.split('\n')
  new_text = []

  for line in text:
    new_text.append(line.replace('*-*', '\n'))
  
  return new_text

def format_data(data):
  data = data.split(' ')
  all_data = []

  for step in data:
    if step.__contains__(','):
      step = step.split(',')

    all_data.append(step)

  return all_data
