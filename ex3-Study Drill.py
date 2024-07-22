# The following script will calculate your anual salary based on the your hourly pay.

hourly_rate = 21.00
state_tax = 0.06
federal_tax = 0.05
sick_days = 5

work_week_hours = 40
weeks_work = 52
daily_hours = 8

sick_time = sick_days * daily_hours
total_work_hours = work_week_hours * weeks_work
total_tax = state_tax + federal_tax

adjusted_work_hours = total_work_hours - sick_time

# Calculate the gross yearly salary
gross_salary = hourly_rate * adjusted_work_hours

# Calculate the net yearly salary after taxes
net_salary = gross_salary * (1-total_tax)

print("Gross Yearly Salary: $", gross_salary)
print("Net Yearly Salary after Taxes (and sick days): $", net_salary)
