#taking bike pric 
bike_price = int(input("eneter the bike price here"))

tax_rate1 = 0.15
tax_rate2 = 0.10
tax_rate3 = 0.05

if bike_price > 100000:
    tax = bike_price * tax_rate1
elif bike_price > 50000:
    tax = bike_price * tax_rate2
else:
    tax = bike_price * tax_rate3

print("road tax you need to pay is rupees",tax)