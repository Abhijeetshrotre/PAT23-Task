def sum_firstandlastdigit(number):
    # Convert the number to a string to easily access digits
    number_str = str(number)

    # Extract  first and last digit
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])

    #  sum of the first and last digit
    digit_sum = first_digit + last_digit

    return digit_sum


# Example
try:
    # user input as integer
    user_input = int(input("Enter an integer: "))

    #  display the sum
    result = sum_firstandlastdigit(user_input)
    print(f"Sum of the first and last digit: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")