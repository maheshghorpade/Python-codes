#getting units from user
units_consumed = int(input("enter the number of units used by consumer "))

#defining unit rate  
unit_rate = 5 #rs 5 per hour
industry_rate = 10
if units_consumed <= 100:
    electricity_bill = 0
elif units_consumed <= 200:
    electricity_bill = units_consumed * unit_rate
else:
    
    units_consumed > 200
    electricity_bill = units_consumed * industry_rate

print("elctricity bill of consumer will be rupees ",  electricity_bill )
print("save electricity save earth")
    