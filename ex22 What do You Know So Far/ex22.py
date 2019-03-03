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

symStrip = "str.strip(chars)"
defStrip = "return a copy of the string with leading and trailing whitespace remove. If chars is given and not None, remove in chars instead until finding first char that is not in chars."
define_Known_Names(symStrip, defStrip)

symEncode = "str.encode()"
defEncode = "str.encode(encoding='utf-8, errors='strict').\n Encode the string using the codec registered for encoding."
define_Known_Names(symEncode, defEncode)

symDecode = "bytes.decode()"
defDecode = """ecode(self, /, encoding='utf-8', errors='strict')
    Decode the bytes using the codec registered for encoding."""
define_Known_Names(symDecode, defDecode)

symSplit = "str.split()"
defSplit = """split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.

    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit."""
define_Known_Names(symSplit, defSplit)

symSorted = "sorted()"
defSorted = """"sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order."""
define_Known_Names(symSorted, defSorted)

symPop = "arr.pop()"
defPop = "If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised."
define_Known_Names(symPop, defPop)