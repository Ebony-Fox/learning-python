In this exercise I learned about formatting strings, while apply all the other basic principles that I have accumulated so far. I embed variables inside strings by using a special {} sequence and then putting the variable inside the {} characters. After the string needs to have an "f" for “format,” as in f"Hello {somevar}". This little f before the " (double-quote) and the {} characters tell Python 3, “Hey, this string needs to be formatted. Put these variables in there.”

## Study Drills

1. Change all the variables so there is no my\_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.

```python
name = 'Zed A. Shaw'

age = 35 # not a lie

height = 74 # inches

weight = 180 #lbs

eyes = 'Blue'

teeth = 'White'

hair = 'Brown'



print(f"Let's talk about {name}.")

print(f"He's {height} inches tall.")

print(f"He's {weight} pounds heavy.")

print("Actually that's not too heavy.")

print(f"He's got {eyes} eyes and {hair} hair.")

print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right

total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")
```

2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.

```python
convert_centi = height * 2.54
convert_kilo = weight * 0.453592
```
