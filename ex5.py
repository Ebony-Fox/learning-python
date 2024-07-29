name = 'Jarrel T.'
age = 35  # not a lie
height = 74  # inches
height_converted = height * 2.54  # centimeters
weight = 180  # lbs
weight_converted = weight * 0.453592  # kilograms
eyes = 'brown'
teeth = 'white'
hair = 'black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eys and {hair} hair.")
# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
