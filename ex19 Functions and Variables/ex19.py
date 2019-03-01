def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(">>> cheese_count=", cheese_count)
  print(f"You have {cheese_count} cheeses!")
  print("You have {} boxes of crackers!".format(boxes_of_crackers))
  print("Man that's enough for a party!")
  print("Get a blanket.\n")
  print("<<< exit cheese and crackers")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
print("How much cheese you want to put?")
amount_of_cheese = int(input('? '))
print("How many crackers do you want to put in?")
amount_of_crackers = int(input('? '))

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)