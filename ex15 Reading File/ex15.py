#imports argv from system and command line
from sys import argv

#unpacks variables from argv to script and filename var
script, filename = argv

#opens path that was given in command line to argv
txt = open(filename)

print(f"Here's your file {filename}:")
#reads file that is hold in txt variable
print(txt.read())

print("type the filename again:")
fileAgain = input("> ")

txtAgain = open(fileAgain)

print(txtAgain.read())

txt.close()
txtAgain.close()