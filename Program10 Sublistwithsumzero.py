def sublistwithzerosum(nums):
    prefix_sum_set = set()
    prefix_sum = 0

    for num in nums:
        prefix_sum += num

        # If the current prefix sum is zero or seen, a sub-list with zero sum exists
        if prefix_sum == 0 or prefix_sum in prefix_sum_set:
            return True

        # Add the current prefix sum to the set
        prefix_sum_set.add(prefix_sum)

    # No sub list with zero sum found
    return False

# Example usage:
numbers = [4, 2, -3, 1, 6]

if sublistwithzerosum(numbers):
    print("There is a sub-list with zero sum.")
else:
    print("There is no sub-list with zero sum.")