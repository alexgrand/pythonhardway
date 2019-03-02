def define_Known_Names(word, definition):
  print("{} - {}\n".format(word, definition))

symPrint = '\nprint()'
defPrint = 'prints out str that you put in'
define_Known_Names(symPrint, defPrint)

symF = "f'str {var}'"
defF = "formats string and put variables in {}, where 'var' must contain some string"
define_Known_Names(symF, defF)

symFormat = "'str {}'.format()"
defFormat = 'formats string in {} using args that were given in ()'
define_Known_Names(symFormat, defFormat)

symInput = "input()"
defInput = "takes users input from comand line (that is always string)"
define_Known_Names(symInput, defInput)

symImport = "from [module] import [fn]"
defImport = "imports functions/methods from modules"
define_Known_Names(symImport, defImport)

symARGV = "argv"
defARGV = "container that takes strings from user's input in command line and put it into variables. EX: var1, var2 = argv"
define_Known_Names(symARGV, defARGV)

symInt = "int()"
defInt = "converts different formats into integer"
define_Known_Names(symInt, defInt)

symOpen = "open()"
defOpen = "builtin method that opens file by given path"
define_Known_Names(symOpen, defOpen)

symRead = "[file].read()"
defRead = "reads and returns file's content from FileObject (_io.TextIOWrapper). "
define_Known_Names(symRead, defRead)

symTruncate = "[file].truncate()"
defTruncate = "truncate(self, pos=None, /)Truncate file to size bytes. Must be used with 'w' mode when you open() the file. Was cleaning file in our examples"
define_Known_Names(symTruncate, defTruncate)

symWrite = "[file].write()"
defWrite = """_io.TextIOWrapper.write = write(self, text, /)
    Write string to stream.
    Returns the number of characters written (which is always equal to the length of the string).
"""
define_Known_Names(symWrite, defWrite)

symSeek = "[file].seek(int)"
defSeek = "change the stream position to the given byte offset. 0 - start of stream. 1 - current stream position. 2 - end of stream. Returns the new absolute position."
define_Known_Names(symSeek, defSeek)

symReadline = "[file].readline()"
defReadline = """readline(self, size=-1, /)
      Read until newline or EOF
      Return an empty string if EOF is hit immediately"""
define_Known_Names(symReadline, defReadline)

symClose = "[file].close()"
defClose = """ _io.TextIOWrapper.close = close(self, /)
    Flush and close the IO object.

    This method has no effect if the file is already closed."""
define_Known_Names(symClose, defClose)

symExists = "[os.path].exists('path')"
defExists = "func imported from os.path. checks the path if it exists. Returns False for broken symbolic links"
define_Known_Names(symExists, defExists)

symDef = "def [fn():]"
defDef = " a function definition that defines a user-defined function object."
define_Known_Names(symDef, defDef)