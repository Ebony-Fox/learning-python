Strings are used when you want to "export" or display something to someone from your code. It a piece of text that can be readable using the print() function. In this exercise, I will be writing more code around strings and text and how to format that text.

```python
# Creates the variable "types_of_people" assigned with the value 10
types_of_people = 10

# Creates the variable "x" assigning it a formatted string with the variable "types_of_people" embedded in the string
x = f"There are {types_of_people} types of people."


# creates the variable "binary" with a string value
binary = "binary"

# creates the variable "do_not" with a string value
do_not = "don't"

# creates the variable "y" with a formatted string and the "binary" and "do_not" values embedded in the string
y = f"Those who know {binary} and those who {do_not}."


# prints out the x variable
print(x)

# prints out the y variable
print(y)


# prints out a formatted string with the "x" variable embedded
print(f"I said: {x}")

# prints out a formatted string with the "y" value embedded and wrapped in a string
print(f"I also said: '{y}'")


# creates variale "hilarious" and assigns it a Boolean value
hilarious = False

# creates the variable "joke_evaluation" with the string value and an empty format parenthes
joke_evaluation = "Isn't that joke so funny?! {}"


# prints variable "joke_evaluation" with the .format syntax to add the variable hilarious to the string
print(joke_evaluation.format(hilarious))


# creates the variable "w" with a string
w = "This is the left side of..."

# creates  the variable "e" with a string
e = "a string with a right side"


# prints the variables "w" and "e" with concatention
print(w + e)
```

Study Drills

1. Go through this program and write a comment above each line explaining it.
   -Commented Above

2. Find all the places where a string is put inside a string. There are four places.
   Lines 6, 11, 12 - Yes, there is only 4 places

3. Are you sure there are only four places? How do you know? Maybe I like lying.
   Bro, you're not!

4. Explain why adding the two strings w and e with + makes a longer string.
   The plus symbol is the concatenation where two strings can be attached by using the "+ symbol"

Break It
You are now at a point where you can try to break your code to see what happens. Think of this as a game to devise the most clever way to break the code. You can also find the simplest way to break it. Once you break the code, you then need to fix it. If you have a friend, then the two of you can try to break each other’s code and fix it. Give your friend your ex6.py file so they can break something. Then you try to find their error and fix it. Have fun with this, and remember that if you wrote this code once you can do it again. If you take your damage too far, you can always type it in again for extra practice.
