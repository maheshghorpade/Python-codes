def print_even_numbers():
    # Taking user input
    numbers = input("Enter numbers separated by spaces: ")
    
    # Splitting the input into a list of strings and converting them to integers
    num_list = [int(num) for num in numbers.split()]
    
    # Printing even numbers
    print("Even numbers are:")
    for num in num_list:
        if num % 2 == 0:
            print(num)

# Call the function
print_even_numbers()