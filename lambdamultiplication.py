# user-input
num = [int(input("Enter a number: "))]

# let's create our lambda function for the table
table = list(map(lambda x, y: x * y, list(range(1, 11)), num * 10))

print(table)