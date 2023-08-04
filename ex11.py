# Prints string asking age with the end paramater argument to create a new line
print("How old are you?", end=' ')
# Creates new age variable with input function to gather answer from previous question asked to user
age = input()
# Prints sencond string questions using end parameter again
print("How tall are you?", end=' ')
# Creates variable height with input function
height = input()
# Prints thrid string question with end parameter
print("How much do you weigh?", end=' ')
# Creates variable weight with input function
weight = input()

# Prints formatted string with all variables in string to create sentence from user prompts
print(f"So, you're {age} old, {height}, tall and {weight} heavy.")
