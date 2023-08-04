# from Python's default system libary we are importing the 'argv' module
from sys import argv

# read the WYSS section for how to run this
# Unpacks the 'argv' module list into four variables
script, first, second, third = argv

# Prints first variable 'script' with string
print("The script is called:", script)
# Prints second variable 'first' with string
print("Your first variable is:", first)
# Prints thrird variable 'second' with string
print("Your second variabel is:", second)
# Prints four variable 'third' with string
print("Your third variable is:", third)
