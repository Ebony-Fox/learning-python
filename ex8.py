# creating a formatter variable with for placeholders for later values to input
formatter = "{} {} {} {}"

# Uses the format() method on the formatter variable to print numbers 1,2,3,4
print(formatter.format(1, 2, 3, 4))
# Uses the format method to print string variables one, two, three, four
print(formatter, format("one", "two", "three", "four"))
# Use the format method to print Boolean values
print(formatter.format(True, False, True, False))
# Uses the format method to print the formatter variable itself, printing the "{}" place holder four times
print(formatter.format(formatter, formatter, formatter, formatter))
# Uses the format method to print the multi-line arguments in the placeholder values
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
