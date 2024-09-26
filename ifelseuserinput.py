
#get input from user
hours_worked = int(input("enter the number of hours worked "))

#define the hourly rate and calculate the payment 
hourly_rate = 10 #$10 per hour
if hours_worked <= 0:
    payment_amount = 0
elif hours_worked <= 40:
    payment_amount = hours_worked * hourly_rate
else:
    #for hours worked above 40, apply 1.5 times the hourly rate for overtime
    overtime_hours = hours_worked - 40
    payment_amount = 40 * hourly_rate + overtime_hours * hourly_rate * 1.5
    



#display the payment amount to user 
print("the amount is $", payment_amount)




