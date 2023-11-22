def nonrepeatingelement(nums):
    # Create a dictionary to store the frequency of each element
    frequency = {}

    # Iterate the list and count the frequency of each element
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the first non-repeating element
    for num in nums:
        if frequency[num] == 1:
            return num

    # Return None if there is no non-repeating element
    return None

# Example
numbers = [3, 3, 2, 4, 2, 6, 3, 7]
result = nonrepeatingelement(numbers)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There is no non-repeating element in the list.")