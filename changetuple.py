x = ("grapes","mango","cherry") #this is tuple
y = list(x) #converting tuple into list
y[1] = "banana" #changing the position the value at 1
x = tuple(y) #converting list back into tuple
print(x)