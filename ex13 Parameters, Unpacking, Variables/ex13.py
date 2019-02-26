from sys import argv
# read the WYSS section for how to run this

#to run it you need to pass arguments, where 1st arg is path to script

# script, first, second, third = argv

# print('The script is called:', script)
# print('Your first variable is:', first)
# print('Your second variable is:', second)
# print('Your third variable is:', third)

script, age, height, weight = argv
name = input('What\'s your name? ')

print('Hello {}'.format(name))
print(f'You are {int(age)} years old.')
print(f'{height} tall')
print('and {}kg heavy.'.format(weight))

print(argv)