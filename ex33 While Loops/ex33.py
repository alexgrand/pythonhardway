numbers = []

# while i < 6:
#   print(f"At the top i is {i}")
#   numbers.append(i)

#   i += 1
#   print("Numbers now: ", numbers)
#   print(f"At the bottom i is {i}")

def whileLoop(var, step):
  # i = 0
  # while i < var:
  #   print(f"At the top i is {i}")
  #   numbers.append(i)

  #   i += step
  #   print("Numbers now: ", numbers)
  #   print(f"At the bottom i is {i}")

  for i in range(0, var):
    if step == 0: step = 1
    if i < var and i % step == 0:
      print(f"At the top i is {i}")
      numbers.append(i)
      print("Numbers now: ", numbers)
      i += step
      print(f"At the bottom i is {i}")


print("The numbers: ")

whileLoop(7, 2)

for num in numbers:
  print(num)
