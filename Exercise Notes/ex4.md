In this exercise, I learned about variable and how to create & name variables. Below is the following code with comments above on what the code does.

```python
# creates the variable name "cars" with the value of 100
cars = 100

# creates the variable name "space_in_a_car" with of the value 4.0
space_in_a_car = 4.0

# creates variable name "drivers" with value of 30
drivers = 30

# creates variable name "passengers" with value 90
passengers = 90

# creates variable "cars_not_driven" that is the result of the "cars" variable - the "drivers" variable
cars_not_driven = cars - drivers

# creates varible name "cars_driven" that is equal to the "drivers" variable
cars_driven = drivers

# creates variable name "carpool_capacity" that is the vaue of "cars_driven" times "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car

# creates variable name "average_passengers_per_car" that equals "passengers" divided by cars_driven
average_passengers_per_car = passengers / cars_driven



# prints string with "cars" varaible that prints out a number
print("There are", cars, "cars available.")

# prints strings with "drivers" variable that prints the variable number
print("There are only", drivers, "drivers avalible.")


print("There will be", cars_not_driven, "empty cars today.")

print("We can transport", carpool_capacity, "people today.")

print("We have", passengers, "to carpool today.")

print("We need to put about", average_passengers_per_car, "in each car.")
```

## Study Drills

Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

Explain this error in your own words. Make sure you use line numbers and explain why.

## Here are more study drills

1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
   The 4.0 is not nesscarry you still get the correct answer, it's just the number is no longer a float number
2. Remember that 4.0 is a floating point number. It’s just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.

3. Write comments above each of the variable assignments.
   Done! See Above

4. Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
   The "=" symbol is the assignment operator that assigns values to variables

5. Remember that \_ is an underscore character.
   Got it!

6. Try running python3.6 from the Terminal as a calculator like you did before, and use variable names to do your calculations. Popular variable names include i, x, and j.
