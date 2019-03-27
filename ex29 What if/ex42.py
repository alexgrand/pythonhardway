class Animal(object):
  pass

# Dog is an Animal Class
class Dog(Animal):
  def __init__(self, name):
    # Dog has a name property
    self.name = name

# Cat is-an Animal class
class Cat(Animal):
  def __init__(self, name):
    # Cat has-a name prop
    self.name = name

# Person is-an object
class Person(object):
  def __init__(self, name):
    #Person has-a name
    self.name = name

    ## Person has-a pet of some kind
    self.pet = None

# Employee is-a Person class
class Employee(Person):
  def __init__(self, name, salary):
    # Employee has-a name from Person's class
    super(Employee, self).__init__(name)
    # Employee has-a salary property
    self.salary = salary

# Fish is-an object
class Fish(object):
  pass

# Salmon is-a Fish
class Salmon(Fish):
  pass

# Halibut is-a Fish
class Halibut(Fish):
  pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet that is-a satan
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-a per that is-a rover
frank.pet = rover

# flipper is-a Fish 
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
