car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

#x = car.keys()
y = car.keys()

#print(x) #before the change

car["color"] = "white"
car["fuel"] = "diesel"
#print(x) #after the change
print(y)

