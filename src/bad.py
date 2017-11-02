#-----------------------------------------------------------------
# Annotated example of a bad snippet for printing the contents of a file
#
# no "if __name__..."
# code not in a function
# no license
# "file" is a reversed word in python
# use with open(... instead of f = open(...
# avoid hardcoded paths. use os.path.join and string formatting
file = open('/a/b/c.txt', 'r')

# files are iterable in python
lines = file.readlines()

# in python 2.7 use xrange instead of range
# use enumerate() instead of a counter
c = 0
for i in range(len(lines)):
    # use string formatting and use prefix
    print c, lines[c]
    c = c+1

# file not closed
# no EOF