from quest_space import fl

class Game(object):
  def __init__(self):
    self.scenes = fl.read()
    print(self.scenes)


game = Game()