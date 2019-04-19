from quest_space import fl
from sys import exit
from utils import *

class Game(object):
  def __init__(self):
    self.scenes = fl.read()
    self.u_name = input("Ваше имя? ")
    self.scene = {}
    self.current_scene = 'begining'
    self.pre_scene = self.current_scene
    self.next_scene = ''
    self.text = ''
    self.inventory = {}
    self.steps = {}
    self.status = {}
  
  def start(self):
    self.enter()
    self.exit()
    return
  
  def enter(self):
    if self.next_scene == 'end':
      self.exit()

    self.get_data()
    self.print()

    u_input = input("> ")

    if not self.steps.__contains__(u_input) and u_input != 'exit':
      print(f_string("Введите верный шаг или exit!"))
      self.pre_scene = self.current_scene
      self.enter()
      return

    elif u_input == 'exit':
      self.exit()
      return

    self.next(u_input)
    self.enter()

  def get_data(self):
    if self.current_scene != self.pre_scene or self.current_scene == 'begining':
      self.get_scene()
      self.get_text()
      self.get_inventory()
      self.get_steps()
      self.get_status()

    return self.scene

  def get_scene(self):
    self.scene = self.scenes.get().get(self.current_scene)
    return self.scene

  def get_text(self):
    self.text = self.scene.get('text')
    return self.text

  def get_inventory(self):
    inventory = self.scene.get('inventory')
    items = inventory.keys()

    for item in items:
      if not self.inventory.__contains__(item):
        self.inventory[item] = inventory[item]
      else:
        self.inventory[item] += inventory[item]
    
    return self.inventory
  
  def get_steps(self):
    self.steps = self.scene.get('steps')
    return self.steps

  def get_status(self):
    status = self.scene.get('status')
    properties = status.keys()

    for name in properties:
      self.status[name] = status[name]

  def print(self):
    self.print_text()
    self.print_status()
    self.print_inventory()
    self.print_steps()

    return

  def print_text(self):
    self.text = self.text.format(self.u_name)

    print(self.text)
  
  def print_status(self):
    if len(self.status) > 0:
      for status in self.status:
        print(f"\t{self.status[status]}")

  def print_inventory(self):
    if len(self.inventory) > 0:
      print("\t\tУ вас есть:")

      for item in self.inventory:
        print(f"\t{item}: {self.inventory[item]}")
    
      print("\n")
  
  def print_steps(self):
    for step in self.steps:
      print(self.steps[step].get('text'))

  def next(self, u_choice):
    self.pre_scene = self.current_scene
    self.next_scene = self.steps.get(u_choice).get('next_step')
    self.current_scene = self.next_scene
    return

  def exit(self):
    exit(1)
    return




game = Game()
game.start()