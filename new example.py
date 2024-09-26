# Get input from the user
hours_worked = int(input("Enter the number of hours worked: "))

# Define the hourly rate and calculate the payment amount
hourly_rate = 10  # $10 per hour
if hours_worked <= 0:
    payment_amount = 0
elif hours_worked <= 40:
    payment_amount = hours_worked * hourly_rate
else:
    # For hours worked above 40, apply 1.5 times the hourly rate for overtime
    overtime_hours = hours_worked - 40
    payment_amount = 40 * hourly_rate + overtime_hours * hourly_rate * 1.5

# Display the payment amount to the user
print("The payment amount is $", payment_amount)