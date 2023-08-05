# from 'sys' libary import 'argv' module
from sys import argv

# assign two variables to the 'argv' module
script, user_name = argv
# create a prompt variable with the string '> '
prompt = '> '

# Print a formatted string using the two assigned variables
print(f"Hi {user_name}, I'm the {script} script.")
# Prints a string
print("I'd like to ask you a few questions.")
# Prints a formatted string with the 'user_name' variable
print(f"Do you like me {user_name}")
# Creates the variable 'likes' with and input function using the prompt variable as the string
likes = input(prompt)

# Prints the second question using the same formatted string process
print(f"Where do you live {user_name}?")
# Crates 'lives' variable using the input function
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

# Prints formatted multi-line string with all variables created passing user input data
print(f"""
      Alright, so you said {likes} about liking me.
      You live in {lives}. Not sure where that is.
      And you have a {computer} computer. Nice.
      """)
