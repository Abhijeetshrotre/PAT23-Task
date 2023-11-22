def ishappynumber(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

def counthappynumbers(numbers):
    happy_count = 0

    for number in numbers:
        if ishappynumber(number):
            happy_count += 1

    return happy_count

# Example
original_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = counthappynumbers(original_list)

print("Original List:", original_list)
print("Happy Count:", happy_count)