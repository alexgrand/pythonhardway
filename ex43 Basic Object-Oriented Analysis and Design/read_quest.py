from os import listdir
import json

def input_question(question):
  question = f_string(question)
  answer = input(question)

  return answer

def f_string(string):
  string = f"|{string}|"
  string = f"\n{'-' * len(string)}\n{string}\n{'-' * len(string)}\n"
  
  return string


class File(object):
  def __init__(self):
    self.file = ''
    self.name = ''
    self.dict = ''

    self.choose_quest()
  
  def get_quests(self):
    available_quests = listdir('quests/')
    all_quests = []

    for quest in available_quests:
      quest = quest.replace('.json', '')
      all_quests.append(quest)
    
    return all_quests

  def jsonify(self):
    if self.file:
      self.dict = json.loads(self.file)
    
    return self.dict

  def open(self):
    try:
      file = open(f"quests/{self.name}.json", 'r')
      file = file.read()
      self.file = file
      return file
    except:
      return False

  def choose_quest(self):
    print(f_string("Доступные квесты: "))
    print(self.get_quests())

    self.name = input_question("Выберете квест, который хотите пройти.")

    if self.open():
      self.jsonify()
    else:
      print(f"Квеста '{self.name}' не существует! Введите правильное название квеста.")
      self.choose_quest()

  def get(self):
    return self.dict



quest = File()
