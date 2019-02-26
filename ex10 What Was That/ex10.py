tabbyCat = '\tI\'m tabbed in.'
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."

fatCat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(tabbyCat)
print(persianCat)
print(backslashCat)
print(fatCat)

# try formatting and escaping with variables
tab = '\t'
newline = '\n'

fatCat2 = '''
I'll do a list 2:
''' + f'{tab}* Cat food' + '''
{}* Fishies
{}* Catnip {}* Grass
'''

print(fatCat2.format(tab, tab, newline + tab)
)