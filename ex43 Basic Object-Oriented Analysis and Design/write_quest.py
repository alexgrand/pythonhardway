import json

all_scenes = {
  'begining': {
    'text': """
      \t{}, вы опытный бизнесмен со стажем предпринимательской 
      деятельности - именно такой агент нужен НИИ этнографии и 
      космоархеологии имени Грега Рафмана. Наш институт имеет научную 
      станцию на планете Боннасис (система Процион), которая занимается 
      изучением местных низкоразвитых племен - мензолов. 
      \tДля исследований нам необходимо получить у этих племен ценный 
      артефакт - медного идола. Получить его возможно только одним 
      способом - купить. Мы пытались это сделать, но потерпели неудачу. 
      Теперь мы готовы выплатить 65535 cr тому, кому удастся выкупить 
      у аборигенов этот артефакт. Важно сделать это до 5 Мая 3019, 
      когда мы планируем собрать специальную конференцию по этому 
      поводу. По прибытии на станцию вас встретят наши научные 
      сотрудники, которые ознакомят вас с деталями.
    """,
    'steps': {
      '1': {
        'text': '\t1. Начать сначала',
        'next_step': 'camp',
      },
    },
  },
  'camp': {
    'text': """
      \tВы достигли лагеря ученых-этнографов и посадили свой корабль 
      на стоянке. Лагерь представлял собой площадку, огороженную 
      деревянным частоколом, с пластиковыми палатками и одним 
      металлическим домиком посередине. Вы не успели как следует 
      осмотреться, как к вам подошел человек, одетый в меховую куртку,
      с костяными бусами на шее и в уборе из листьев на голове.
      \t- Приветствую вас, {}, - он протянул вам руку. - Мы ждем вас со
       дня на день. Как долетели?
      \t- Спасибо, весьма комфортно, - вы пожали ему руку, с трудом
      преодолев опасение заразиться какой-нибудь местной экзотической 
      болезнью.
      \t- Я Рене Маккалистер, начальник этой станции. Давайте выпьем
      по стаканчику гуанавы, и я введу вас в курс дела. Вы скоро 
      поймете, какого рода услуги нам требуются и для чего вы нам нужны.
      \tВы вошли в одну из пластиковых палаток. К вашему удивлению, 
      внутри она оказалась весьма цивилизованной - мебель, аппаратура, 
      кровать с водяным матрасом в углу. Маккалистер посадил вас за 
      стол, поставил два стакана и большую бутыль с темным коричневым 
      напитком. Маккалистер сделал несколько попыток открыть пробку; 
      наконец ему это удалось, но пробка отскочила и упала прямо 
      под вашим стулом. Произнеся какое-то местное ругательство, 
      ученый принялся искать пробку под столом и рядом с собой.
      """,
    'steps': {
      '1': {
        'text': '\t1. Поднять пробку и положить в карман',
        'next_step': 'take_probe',
      },
      '2': {
        'text': '\t2. Поднять пробку и отдать Маккалистеру',
        'next_step': 'give_probe'
      },
    },
  },
  'give_probe': {
    'text': """
      \tПробка была очень красивой - из мягкой породы красного дерева,
      инкрустированная изящным узором из золотистого пластика. Вы 
      протянули ее Маккалистеру.
      \t- Очень правильный поступок с точки зрения мензольской 
      психологии! - прокомментировал он ваши действия. - Запомните:
      даже если мензол выбросил какую-то вещь, она все равно принадлежит
      ему! И вы не можете ею завладеть, просто подняв ее с земли. 
      Вы все равно должны будете эту вещь купить. Впрочем, есть 
      одно исключение: если мензол выбросил вещь на деревенскую 
      свалку, то это значит, что она ему не нужна. Любой может взять
      ее оттуда бесплатно, хотя это и считается дурным тоном... 
      Ну, ладно. Так как я не мензол, то я дарю вам эту пробку в 
      качестве сувенира, а также для наглядной иллюстрации различия 
      наших культур.
      \tС этими словами он наполнил ваш, а потом и свой стакан 
      тягучей жидкостью, от которой несло чем-то древесным.
      \t- Пожалуйста, угощайтесь, - предложил Маккалистер.
      """,
    'steps': {
      '1': {
        'text': '\t1. Далее',
        'next_step': 'end'
      }
    },
    'inventory': {
      'Пробка от гуанавы': 1
    },
  },
  'take_probe': {
    'text': """
      \tПробка была очень красивой - из мягкой породы красного дерева, 
      инкрустированная изящным узором из золотистого пластика. Очень 
      хороший сувенир! К сожалению, Маккалистер заметил вашу маленькую 
      клептоманическую акцию и сделал вам суровую отповедь:
      \t- А вот так не поступайте в деревне мензолов ни в коем случае! 
      Воровство - это самое страшное преступление в среде мензолов. 
      За него вас могут даже убить, если поймают. И, главное, вы навсегда 
      потеряете уважение мензолов. Запомните: даже если мензол выбросил 
      какую-то вещь, она все равно принадлежит ему! И вы не можете ею 
      завладеть, просто подняв ее с земли. Вы все равно должны будете 
      эту вещь купить. Впрочем, есть одно исключение: если мензол 
      выбросил вещь на деревенскую свалку, то это значит, что она ему не 
      нужна. Любой может взять ее оттуда бесплатно, хотя это и считается 
      дурным тоном... Если уж вам так понравилась эта пробка, то можете 
      оставить ее у себя. Кстати, мензол на моем месте никогда бы не 
      сделал вам подарка. Вы в любом случае должны были бы купить у него 
      пробку или дать ему что-нибудь взамен...
      \tНаконец Маккалистер махнул рукой и наполнил ваш, а потом и свой 
      стакан тягучей жидкостью, от которой несло чем-то древесным. 
      \t- Пожалуйста, угощайтесь, - предложил он.
    """,
    'steps': {
      '1': {
        'text': "\t1. Далее",
        'next_step': 'end',
      },
    },
    'inventory': {
      'Пробка от гуанавы': -1
    }
  },
}


class Raw_Scene(object):
  def __init__(self):
    self.scene = {}
    self.name = ''
    self.text = ''
    self.steps = {}
    self.inventory = {}
  
  def put_name(self):
    name = input("Название сцены? >")

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
        line = "\n    " + word + ' '
    
    formatted_str += line + '\n'

    return formatted_str

  def check_usr_input(self, u_input):
    print("*" * 105)
    print(u_input)
    print("*" * 105)

    is_correct_input = input("Эти данные верны? (y/n)\n")

    if is_correct_input == 'y':
      return True
    else:
      print("ВВЕДИТЕ КОРРЕКТНЫЕ ДАННЫЕ.")
      print("*" * 105)
      return False
    
  def put_text(self):
    user_input = input("Текст сцены? \n(вместо 'enter'и создания абзаца, пишите *n*) >")
    
    formatted_input = self.format_usr_text(user_input, 70)
    
    if self.check_usr_input(formatted_input):
      self.text = formatted_input
    else:
      self.put_text()

  def put_steps(self, step_num = 1):
    input_step_text = input(f"Введите текст для шага № {step_num} >")
    input_next_step = input("Введите название сцены, куда шаг ведет >")

    if input_step_text == '' or input_next_step == '':
      print("ВВЕДИТЕ КОРРЕКТНЫЕ ДАННЫЕ.")
      self.put_steps(step_num)

    else:

      if self.check_usr_input(f"{input_step_text}:\n{input_next_step}"):
        self.steps[str(step_num)] = {}
        step = self.steps[str(step_num)]
        step['text'] = f"\t{step_num}. {input_step_text}."
        step['next_step'] = input_next_step

        is_next_step = input("Есть ли еще шаг? (y/n) >")
        
        if is_next_step == 'y':
          step_num += 1
          self.put_steps(step_num)

      else:
        self.put_steps(step_num)
    
  def put_inventory(self):
    is_inventory = input("Есть ли(еще) инвентарь, который добавляется в этой сцене? (y/n) >")

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
    
    elif is_inventory == '':
      self.put_inventory()

  def change_data(self):
    must_be_changed = input("Что вы хотите изменить? Введите через пробел (name/text/inventory/steps) \nЕсли хотите поменять все, нажмите enter:\n")
    
    if not must_be_changed:
      self.make()
    else:
      must_be_changed = must_be_changed.split()
      
      for func in must_be_changed:
        try:
          fn = getattr(self, f"put_{func}")
          fn()
        except:
          print("*" * 105)
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
        
  def show(self):
    print("*" * 105)
    print("\t" + self.name)
    print(self.text)

    for item in self.inventory:
      print("\t", item, f"[{self.inventory[item]}]")
    
    print("\n")

    for step in self.steps:
      print(self.steps[step]['text'], f"[{self.steps[step]['next_step']}]")

new_scene = Raw_Scene()
# new_scene.put_name()
# new_scene.put_text()
# new_scene.put_steps()
# new_scene.put_inventory()
new_scene.make()
# getattr(new_scene, 'put_name')()


