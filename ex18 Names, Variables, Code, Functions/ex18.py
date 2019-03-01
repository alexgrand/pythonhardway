def print_two(*args):
  print(f"arg1: {args[0]}, arg2: {args[1]}")

def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
  print(f"arg1: {arg1}")

def print_none():
  print("I got nothing.")

print_two("Alex", "Grand")
print_two_again("Grand", "Alex")
print_one("First!")
print_none()