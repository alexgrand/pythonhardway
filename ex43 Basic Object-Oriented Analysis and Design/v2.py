from quest_space import fl
from sys import exit
from utils import *

class Game(object):
  def __init__(self):
    self.scenes = fl.read()
    self.u_name = input("Ваше имя? ")
    self.scene = {}
    self.current_scene = 'begining'
    self.next_scene = ''
    self.inventory = {}
    self.steps = {}
  
  def start(self):

    while self.next_scene != 'end':
      self.enter()
  
  def enter(self):
    self.get_data()

    self.print_text()
    self.print_inventory()
    self.print_steps()

    self.exit()

  def get_data(self):
    self.get_scene()
    self.get_inventory()
    self.get_steps()

  def get_scene(self):
    self.scene = self.scenes.get().get(self.current_scene)
    return self.scene

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

  def print_text(self):
    text = self.scene.get('text')
    text = text.format(self.u_name)

    print(text)
  
  def print_inventory(self):
    self.get_inventory()

    if len(self.inventory) > 0:
      print("\t\tУ вас есть:")

      for item in self.inventory:
        print(f"\t{item}: {self.inventory[item]}")
    
      print("\n")
  
  def print_steps(self):
    for step in self.steps:
      print(self.steps[step].get('text'))

  def exit(self):
    exit(1)
    return




game = Game()
game.start()