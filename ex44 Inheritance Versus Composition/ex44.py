class Parent(object):
  def implicit(self):
    print("PARENT implicit()")
  
class Child(Parent):
  pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print("=" * 20)

class Parent1(object):
  def override(self):
    print("PARENT override()")

class Child1(Parent1):
  def override(self):
    print("CHILD override()")

dad = Parent1()
son = Child1()

dad.override()
son.override()
print("=" * 20)

class Parent2(object):
  def altered(self):
    print("PARENT altered()")

class Child2(Parent2):
  def altered(self):
    print("CHILD, BEFORE PARENT altered()")
    super(Child2, self).altered()
    print("CHILD AFTER PARENT altered()")

dad = Parent2()
son = Child2()

dad.altered()
son.altered()

print("=" * 20)

class Parent3(object):
  def override(self):
    print("PARENT override()")
  
  def implicit(self):
    print("PARENT implicit()")
  
  def altered(self):
    print("PARENT altered()")

class Child3(Parent3):
  def override(self):
    print("CHILD override()")
  
  def altered(self):
    print("CHILD, BEFORE PARENT altered()")
    super(Child3, self).altered()
    print("CHILD, AFTER PARENT altered()")

dad = Parent3()
son = Child3()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()