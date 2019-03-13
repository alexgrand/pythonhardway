from quest_read import pick_up_quest


# all_texts = [[str0, 1], [str1, 2, 3], [str2, 4], [str3, 4], [str4, 5, 6], [str5], [str6]]

# all_inventory = ['', '', '', ["*** Пробка от гуанавы***"], '', '', '']

def f_list(arr):
  new_arr = []
  while arr.__contains__(''):
    arr.pop(arr.index(''))

  for item in arr:
    new_arr.extend(item.split(','))

  return new_arr

def get_texts_n_steps(line):
  texts_n_steps = []
  
  texts_n_steps.append(line[0])
  texts_n_steps.extend(f_list(line[1]))
  
  return texts_n_steps

def find_quest():
  all_quest = pick_up_quest()
  texts = []
  
  for line in all_quest:
    texts.append(get_texts_n_steps(line))
    
  return texts


all_texts = find_quest()
all_inventory = ['', '']

print(all_texts)