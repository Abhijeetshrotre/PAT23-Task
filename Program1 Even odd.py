python_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the original python list
for number in python_list:
    # Check if the number is even or odd
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the result
print("Original Python List:", python_list)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)