def find_minimumelement(sorted_list):
    # Check if list is not empty
    if not sorted_list:
        return None

    # The minimum element is the first element in the sorted list
    return sorted_list[0]

# Example
sorted_numbers = [-1, 2, 3, 4, 5, 6, 7, 8]
min_element = find_minimumelement(sorted_numbers)

if min_element is not None:
    print(f"The minimum element is: {min_element}")
else:
    print("The list is empty.")