def isprime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def getprimes(numbers):
    prime_numbers = []
    prime_count = 0

    for number in numbers:
        if isprime(number):
            prime_count += 1
            prime_numbers.append(number)

    return prime_count, prime_numbers

# Example usage:
original_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_count, prime_numbers = getprimes(original_list)

print("Original List:", original_list)
print("Prime Count:", prime_count)
print("Prime Numbers:", prime_numbers)