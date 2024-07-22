cars = 100  # Number of cars available
space_in_a_car = 4  # Number of passengers that can fit in each car
drivers = 30  # Number of drivers available
passengers = 90  # Number of passengers needing a ride
# Cars that won't be driven because there aren't enough drivers
cars_not_driven = cars - drivers
# All drivers will drive a car, so this equals the number of drivers
cars_driven = drivers
# Total number of people that can be transported
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / \
    cars_driven  # Average number of passengers per car

print("There are", cars, "cars available.")  # Display the total number of cars
# Display the number of drivers
print("There are only", drivers, "drivers available.")
# Display the number of cars not driven
print("There will be", cars_not_driven, "empty cars today.")
# Display the total transport capacity
print("We can transport", carpool_capacity, "people today.")
# Display the number of passengers
print("We have", passengers, "to carpool today.")
# Display the average number of passengers per car
print("We need to put about", average_passengers_per_car, "in each car.")
