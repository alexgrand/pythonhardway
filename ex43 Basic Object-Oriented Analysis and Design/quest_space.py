import json
from os import listdir
from utils import *

class Raw_Scene(object):
  def __init__(self):
    self.scene = {}
    self.name = ''
    self.text = ''
    self.steps = {}
    self.inventory = {}
  
  def put_name(self):
    name = input_question("Название сцены?")

    if name != '' and check_usr_input(name):
      self.name = name
    else: 
      self.put_name()
  
  def format_usr_text(self, u_input, max_line_size):
    line = ''
    str_to_repl = '*n*'
    u_input = u_input.replace(str_to_repl, f" {str_to_repl} ")
    words_list = u_input.split(' ')

    formatted_str = ''

    for word in words_list:
      if len(line) + len(word) < max_line_size:
        if word.__contains__(str_to_repl):
          formatted_str += line
          line = word.replace(str_to_repl, (f"\n{' ' * 8}"))
        else:
          line += word + ' '
      else:
        formatted_str += line

        if word.__contains__(str_to_repl):
          word = word.replace(str_to_repl, (f"\n{' ' * 8}"))
          line = word + ' '
        else:
          line = "\n    " + word + ' '
    
    formatted_str += line + '\n'

    return formatted_str
    
  def put_text(self):
    user_input = input_question("Текст сцены? \n(вместо 'enter' и создания абзаца, пишите *n*) >")
    
    formatted_input = self.format_usr_text(user_input, 70)
    
    if check_usr_input(formatted_input):
      self.text = formatted_input
    else:
      self.put_text()

  def put_steps(self, step_num = 1):
    input_step_text = input_question(f"Введите текст для шага № {step_num} >")
    input_next_step = input_question("Введите название сцены, куда шаг ведет. Если это последняя сцена, введите 'end'")

    if input_step_text == '' or input_next_step == '':
      print("ВВЕДИТЕ КОРРЕКТНЫЕ ДАННЫЕ.")
      self.put_steps(step_num)

    else:

      if check_usr_input(f"{input_step_text}:\n{input_next_step}"):
        self.steps[str(step_num)] = {}
        step = self.steps[str(step_num)]
        step['text'] = f"\t{step_num}. {input_step_text}."
        step['next_step'] = input_next_step

        is_next_step = input_question("Есть ли еще шаг? (y/n) >")
        
        if is_next_step == 'y':
          step_num += 1
          self.put_steps(step_num)

      else:
        self.put_steps(step_num)
    
  def put_inventory(self):
    is_inventory = input_question("Есть ли(еще) инвентарь, который добавляется в этой сцене? (y/n)")

    if is_inventory == 'y':
      inv_name = input("Введите название единицы инвентаря > ")
      inv_amount = input("Введите количество либо наименование >")
      int_or_str = input("Это количество или признак? (1/2)>")

      if int_or_str == '1':
        try:
          inv_amount = int(inv_amount)
        except: 
          print(f"{inv_amount} - это не число! В наказание вводите этот инвентарь заново!")
          self.put_inventory()


      if check_usr_input(f"{inv_name}: {inv_amount}"):
        self.inventory[inv_name] = inv_amount

      print(f"Инвентарь сцены: {self.inventory}")
      self.put_inventory()
    
    elif is_inventory == '' or is_inventory != 'n':
      self.put_inventory()

  def change_data(self):
    must_be_changed = input_question("Что вы хотите изменить? Введите через пробел (name/text/inventory/steps) или нажмите enter:")
    
    if must_be_changed == '':
      self.inventory = {}
      self.steps = {}
      self.make()
    else:
      must_be_changed = must_be_changed.split()
      
      for prop in must_be_changed:
        try:
          setattr(self, prop, {})
          fn = getattr(self, f"put_{prop}")
          fn()
        except:
          print("=" * 20)
          print(f"\n\nПеременной {prop} не существует. Введите правильное значение!")
          self.change_data()
          return
      
      self.make(True)

  def create(self):
    self.scene = {}
    self.scene[self.name] = {}
    scene = self.scene[self.name]
    scene['text'] = self.text
    scene['inventory'] = self.inventory
    scene['steps'] = self.steps

    return self.scene

  def make(self, has_change = False):
    if not has_change:
      self.put_name()
      self.put_text()
      self.put_inventory()
      self.put_steps()

    self.create()

    self.show()

    if not check_usr_input(''):
      self.change_data()
    
    return self.scene
        
  def show(self):
    print("\n","=" * 20, "\n")
    print("\t" + self.name)
    print(self.text)

    for item in self.inventory:
      print("\t", item, f"[{self.inventory[item]}]")
    
    print("\n")

    for step in self.steps:
      print(self.steps[step]['text'], f"[{self.steps[step]['next_step']}]")
    
    return self.scene

  def get(self):
    return list(self.scene.keys())[0], list(self.scene.values())[0]

class All_Scenes(object):
  def __init__(self):
    self.scenes = []
    self.steps = []
    self.names = []

  def create(self):
    make_new_scene = input_question(f'Шаги квеста без сцены: {self.steps}\nСоздать новую сцену? (y/n)')


    if make_new_scene == 'y':
      new_scene = Raw_Scene()
      new_scene.make()
      name = new_scene.name

            
      self.names.append(name)
      self.add_unused_steps(new_scene)
      self.scenes.append(new_scene)
      self.create()

    elif make_new_scene != 'n':
      self.create()

    else:
      if len(self.steps) > 0:
        print('ВНИМАНИЕ! У вас есть шаги, для которых не написаны сцены!')
        self.create()
      
      self.check_scene()
      self.change_scene()
      self.remove_scene()
      return
  
  def add_unused_steps(self, scene):
    if self.steps.__contains__(scene.name):
      self.steps.remove(scene.name)

    steps = list(scene.steps.values())

    for step in steps:
      step = step.get('next_step')
      
      if step != 'end' and not self.names.__contains__(step):
        if not self.steps.__contains__(step):
          self.steps.append(step)
    
  def check_scene(self):
    check_scene = input_question('Желаете ли прочитать какую либо сцену? (y/n)')

    if check_scene == 'y':

      print(f"Доступные сцены: {self.names}")
      check_scene = input_question('Через пробел вводите сцены, которые хотите прочитать. Либо нажмите enter, если все.')

      if check_scene == '':
        self.show()
      
      else:
        scenes_to_check = check_scene.split()

        for name in scenes_to_check:
          try:
            index = self.names.index(name)
            self.scenes[index].show()

          except:
            print(f"\nВнимание! Сцены {name} не существуют")
            self.check_scene()
        
        return

    elif check_scene != 'n':
      self.check_scene()

    else:
      return

  def change_scene(self):
    change_scene = input_question("Желаете ли вы изменить какую либо сцену? (y/n) ")

    if change_scene ==  'y':
      print(f_string("Доступные сцены: "))
      print(self.names)
      change_scene = input_question("Какую сцену(ы) вы желаете изменить? Введите через пробел или нажмите enter")

      if change_scene == '':
        for scene in self.scenes:
          scene.change_data()
      else:
        scenes_to_change = change_scene.split()
        
        for name in scenes_to_change:
          try:
            index = self.names.index(name)
            self.scenes[index].change_data()
          
          except:
            print(f"ВНИМАНИЕ! {name} СЦЕНЫ НЕТ!")
            self.change_scene()
        
        return

      self.check_scene()
      self.change_scene()
    elif change_scene != 'n':
      self.change_scene()
    else:
      return

  def remove_scene(self):
    to_remove = input_question('Желаете ли удалить какую либо сцену? (y/n)')

    if to_remove == 'y':
      print(f_string('Доступные сцены: '))
      print(self.names)
      to_remove = input_question('Напишите через пробел сцены, подлежащие удалению.')

      scenes_to_remove = to_remove.split()

      for name in scenes_to_remove:
        if self.names.__contains__(name):
          is_sure = input_question(f'Вы уверены что хотите удалить {name} из квеста? (y/n)')

          if is_sure == 'y':
            index = self.names.index(name)
            self.scenes.pop(index)
            self.names.pop()
        else:
          print(f_string(f"ВНИМАНИЕ! Сцены {name} не существует!"))
          self.remove_scene()
          return

    elif to_remove != 'n':
      self.remove_scene()
    else:
      return

  def show(self):
    for scene in self.scenes:
      scene.show()

  def get(self):
    json_dict = {}

    for scene in self.scenes:
      name, content = scene.get()
      json_dict[name] = content

    return json_dict

class File(object):
  def __init__(self):
    self.file = ''
    self.path = 'quests/'
    self.name = 'default'
    self.text = ''
    self.scenes = ''

  def name_it(self):
    ask_quest_name = input_question("Введите название для написанного квеста.")

    if ask_quest_name == '':
      self.name_it()
    else:
      is_correct = check_usr_input(ask_quest_name)

      if not is_correct:
        self.name_it()
        return
      else:
        self.name = ask_quest_name
    
    return self.name

  def write(self):
    scenes_dict = self.scenes.get()
    self.text = json.dumps(scenes_dict, ensure_ascii=False)

    self.file = open(f"{self.path}{self.name}.json", mode='w', encoding="utf-8")
    self.file.write(self.text)
    self.file.close()

    return self.text
  
  def read(self):
    self.choose()
    self.file = open(f"{self.path}{self.name}.json", mode='r', encoding='utf-8')
    self.text = json.loads(self.file.read())
    self.file.close()

    keys = list(self.text.keys())
    all_scenes = All_Scenes()

    for key in keys:
      content = self.text.get(key)
      scene = Raw_Scene()
      scene.name = key
      scene.text = content.get('text')
      scene.steps = content.get('steps')
      scene.inventory = content.get('inventory')
      scene.create()
      
      all_scenes.names.append(key)
      all_scenes.scenes.append(scene)
    
    self.scenes = all_scenes
    return self.scenes

  def add(self):
    self.read()
    self.scenes.create()
    self.write()

  def choose(self):
    available_quests = listdir(self.path)
    quests = []

    for quest in available_quests:
      quests.append(quest.replace('.json', ''))

    print(f_string("Доступные квесты: "))
    print(quests)

    self.name = input_question("Выберете квест")

    if quests.__contains__(self.name):
      return self.name
    else:
      print(f"Квеста '{self.name}' не существует! Введите правильное название квеста.")
      self.choose()

  def create(self):
    self.scenes = All_Scenes()
    self.scenes.create()
    self.name_it()

    self.write()

    return self.scenes
  
  def change(self):
    self.read()
    self.scenes.change_scene()
    self.write()

    return self.text

  def get(self):
    self.read()
    return self.scenes.get()

  def remove(self):
    self.read()
    self.scenes.remove_scene()
    self.write()
  
  def start(self):
    from v2 import game
    return

  def show(self):
    self.read()
    self.scenes.show()

  def action(self):
    print(f_string("Выберите действие или напишите exit:"))
    print("\t1. Написать новый Квест")
    print("\t2. Прочитать Квест.")
    print("\t3. Изменить сцены Квеста.")
    print("\t4. Добавить сцены Квеста")
    print("\t5. Удалить сцены из квеста")
    print("\t6. Пройти Квест")
    user_action = input("> ")

    if user_action == '1':
      self.create()
    elif user_action == '2':
      self.show()
    elif user_action == '3':
      self.change()
    elif user_action == '4':
      self.add()
    elif user_action == '5':
      self.remove()
    elif user_action =='6':
      self.start()
    elif user_action == 'exit':
      return
    else:
      self.action()
      return

    self.action()    

class Status(object):
  def __init__(self):
    self.current = {}
  
  def add(self):
    st_name = input_question("Введите название состояния.")

    if self.has(st_name):
      print(f"\nВНИМАНИЕ! Состояние {st_name} уже существует!\n")
      self.add()
      return 

    st_text = input_question("Текст состояния.")
    u_input = input_question("Эти данные верны?(y/n)")

    if is_yes(u_input, self.add):
      self.current[st_name] = st_text
    
    return st_name, st_text

  def change(self):
    print(f_string("Доступные состояния:"))
    print(self.current)

    u_input = input_question("Введите через пробел, что вы хотите изменить либо 'enter', если все. Это удалит эти сцены")

    if u_input == '':
      self.current = {}
      self.add()
    else:
      u_input = u_input.split()

      for name in u_input:
        if self.has(name):
          self.remove(name)
          self.add()
        else:
          print(f"\nВнимание состояния {name} не существует!")
          self.change()
          return
    return True

  def get(self):
    return self.current

  def has(self, name):
    return self.current.__contains__(name)

  def remove(self, name):
    if self.has(name):
      self.current.pop(name)
      return True
    else:
      print(f"\n Состояние {name} удалить невозможно. Отсутствует.")
      return

fl = File()

status = Status()
print(status.add())
print(status.change())
print(status.get())