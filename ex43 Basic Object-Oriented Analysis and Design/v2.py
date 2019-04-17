from quest_space import fl
from sys import exit

class Game(object):
  def __init__(self):
    self.scenes = fl.read()
    self.u_name = input("Ваше имя? ")
    self.scene = ''
    self.current_scene = 'give_probe'
    self.next_scene = ''
  
  def start(self):

    while self.next_scene != 'end':
      self.enter()
  
  def enter(self):
    self.scene = self.scenes.get().get(self.current_scene)

    self.print_text()
    self.print_inventory()
    print(self.scene.get('steps'))

    self.exit()

  def print_text(self):
    text = self.scene.get('text')
    text = text.format(self.u_name)

    print(text)

  def print_inventory(self):
    inventory = self.scene.get('inventory')

    print("У вас есть:")
    
    for item in inventory:
      print(f"\t{item}")

  def exit(self):
    exit(1)
    return




game = Game()
game.start()