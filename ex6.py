types_of_people = 10  # Number of types of people
# Formatted string with types of people variable
x = f"There are {types_of_people} types of people."

binary = "binary"  # binary as a string
do_not = "don't"  # do not short-hand
# Formatted string with binary and do_not variables
y = f"Those who know {binary} and those who {do_not}."

print(x)  # Display "x" variable with formatted string
print(y)  # Display "y" variable with formatted string

print(f"I said: {x}")  # Display formatted string of a formatted string
# Display formatted string containing formatted string
print(f"I also said: '{y}")

hilarious = False  # Variable with False boolean
# String variable with empty value
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))  # Display

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)
