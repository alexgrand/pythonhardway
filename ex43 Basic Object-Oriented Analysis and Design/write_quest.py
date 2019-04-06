import json

def input_question(question):
  question = f"|{question}|"
  question = f"\n{'-' * len(question)}\n{question}\n{'-' * len(question)}\n"
  answer = input(question)

  return answer


class Raw_Scene(object):
  def __init__(self):
    self.scene = {}
    self.name = ''
    self.text = ''
    self.steps = {}
    self.inventory = {}
  
  def put_name(self):
    name = input_question("Название сцены?")

    if name != '' and self.check_usr_input(name):
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

  def check_usr_input(self, u_input):
    print("\n","=" * 20, "\n")
    print(u_input)

    is_correct_input = input_question('Эти данные верны? (y/n)')

    if is_correct_input == 'y':
      return True
    else:
      print("ВВЕДИТЕ КОРРЕКТНЫЕ ДАННЫЕ.")
      print("*" * 105)
      return False
    
  def put_text(self):
    user_input = input_question("Текст сцены? \n(вместо 'enter'и создания абзаца, пишите *n*) >")
    
    formatted_input = self.format_usr_text(user_input, 70)
    
    if self.check_usr_input(formatted_input):
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

      if self.check_usr_input(f"{input_step_text}:\n{input_next_step}"):
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


      if self.check_usr_input(f"{inv_name}: {inv_amount}"):
        self.inventory[inv_name] = inv_amount

      print(f"Инвентарь сцены: {self.inventory}")
      print("*" * 105)
      self.put_inventory()
    
    elif is_inventory == '' or is_inventory != 'n':
      self.put_inventory()

  def change_data(self):
    must_be_changed = input_question("Что вы хотите изменить? Введите через пробел (name/text/inventory/steps) \nЕсли хотите поменять все, нажмите enter:\n")
    
    if not must_be_changed:
      self.make()
    else:
      must_be_changed = must_be_changed.split()
      
      for func in must_be_changed:
        try:
          fn = getattr(self, f"put_{func}")
          fn()
        except:
          print("=" * 20)
          print(f"\n\nПеременной {func} не существует. Введите правильное значение!")
          self.change_data()
          return
      
      self.make(True)

  def make(self, has_change = False):
    if not has_change:
      self.put_name()
      self.put_text()
      self.put_inventory()
      self.put_steps()

      
    self.scene[self.name] = {}
    scene = self.scene[self.name]
    scene['text'] = self.text
    scene['inventory'] = self.inventory
    scene['steps'] = self.steps

    self.show()

    if not self.check_usr_input(''):
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
      return
  
  def add_unused_steps(self, scene):
    if self.steps.__contains__(scene.name):
      self.steps.remove(scene.name)

    steps = list(scene.steps.values())

    for step in steps:
      step = step.get('next_step')
      
      if step != 'end' and not self.names.__contains__(step):
        self.steps.append(step)
    
  def check_scene(self):
    check_scene = input_question('Желаете ли проверить какую либо сцену? (y/n)')

    if check_scene == 'y':

      print(f"Доступные сцены: {self.names}")
      check_scene = input_question('Через пробел вводите сцены, которые хотите проверить. Либо нажмите enter, если все.')

      if check_scene == '':
        self.show()
      
      else:
        check_scene = check_scene.split()

        for name in check_scene:
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

  # def change_scene(self):
  #   scenes_to_change = change_scene.split()

  #       for name in scenes_to_change:
  #         try:
  #           # найти сцену по name в self.scenes и запустить сцена.change_data
  #           index = self.names.index(name)

  #           self.scenes[index].change_data()

  #         except:
  #           # если сцены с таким именем нет - тогда выдать ошибку и заставить снова выбрать сцену для изменения через check_scene в конце return
  #           print("=" * 20)
  #           print(f"\n\n Сцены с именем {name} не существует.")
  #           self.check_scene()
  #           return

  def show(self):
    for scene in self.scenes:
      scene.show()
    


all_scenes = All_Scenes()
all_scenes.create()

