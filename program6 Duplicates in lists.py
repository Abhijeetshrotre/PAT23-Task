def find_duplicates(list1, list2, list3):
    # Convert the lists to sets for finding common elements
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    # Find common elements across  three sets
    common_elements = set1.intersection(set2, set3)

    # Convert the common elements to a list
    common_elements_list = list(common_elements)

    return common_elements_list

# Example
list1 = [2, 6, 3, 4, 5, 4, 8]
list2 = [4, 5, 6, 7, 8, 8, 9]
list3 = [6, 7, 8, 9, 10]

duplicates = find_duplicates(list1, list2, list3)

if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")