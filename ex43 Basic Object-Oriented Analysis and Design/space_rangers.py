from sys import exit

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

class Scene(object):
  def __init__(self, name, text, steps, inventory = {}):
    self.name = name
    self.text = text
    self.steps = steps
    self.inventory = inventory

  def print_text(self, *f_args):
    print(self.text.format(*f_args))
  
  def print_steps(self):
    print("\n")
    for step in self.steps:
      print(self.steps[step]['text'])

  def get_next_step(self, usr_input):
    usr_choice = self.steps.get(usr_input)

    if usr_choice:
      return usr_choice.get('next_step')
    else:
      return

class Inventory(object):
  def __init__(self):
    self.inventory = {}

  def put(self, i_name, i_amount = 1):
    if self.get(i_name):
      self.inventory[i_name] += i_amount
    else:
      self.inventory[i_name] = i_amount
  
  def get(self, i_name):
    return self.inventory.get(i_name)
  
  def remove(self, i_name):
    if self.get(i_name):
      self.inventory.__delitem__(i_name)

  def show(self):
    return self.inventory

  def print(self):
    if len(self.inventory) > 0:
      print("\t", "*" * 5, "У вас есть", "*" * 5)
      for item in self.inventory:
        print(f"\t{item}:", self.inventory.get(item))
      

class Map(object):
  def __init__(self, scene_map):
    self.scene_map = scene_map
    self.map = {}
  
  def create_scenes(self):
    for scene_name in self.scene_map:
      scene_obj = self.scene_map.get(scene_name)
      scene_text = scene_obj.get('text')
      scene_items = scene_obj.get('inventory')
      scene_steps = scene_obj.get('steps')

      scene = Scene(scene_name, scene_text, scene_steps, scene_items)
      self.map[scene_name] = scene
    
  def show(self):
    return self.map
  
  def get(self, scene_name):
    return self.map.get(scene_name)


class Game(object):
  def __init__(self, all_scenes):
    self.all_scenes = all_scenes
    self.scene_map = Map(all_scenes)
    self.inventory = Inventory()

  def start(self):
    self.user_name = input("Ваше имя? ")
    self.scene_map.create_scenes()

  def stop(self):
    exit(1)

  def show_scene(self, scene_name):
    scene = self.scene_map.get(scene_name)
    print(scene.name)
    print(scene.text.format(self.user_name))
    print('\tscene_inventory:\n\t', scene.inventory, '\n')
    
    for step in scene.steps:
      print(scene.steps[step]['text'],
        '{next_step =', scene.steps[step]['next_step'], '}'
      )
  
  def check_inventory(self, scene_obj):
    if scene_obj.inventory:
      for i_name in scene_obj.inventory:
        self.inventory.put(i_name, scene_obj.inventory[i_name])

  def play(self, scene_name):
    current_scene = self.scene_map.get(scene_name)
    last_scene = self.scene_map.get('end')
    inventory = self.inventory

    self.check_inventory(current_scene)

    current_scene.print_text(self.user_name)
    inventory.print()
    current_scene.print_steps()
      
    
    usr_input = input("> ")
    next_step = current_scene.get_next_step(usr_input)


    if usr_input == 'exit':
      self.stop()
    elif next_step == 'end':
      self.stop()
    elif next_step:
      scene_name = next_step
    else:
      print("\n\t---Неверный вариант! Напишите exit, если хотите выйти!---")
    
    self.play(scene_name)
        




game = Game(all_scenes)
game.start()
game.play('begining')