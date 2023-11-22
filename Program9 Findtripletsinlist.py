def findtripletwithsum(nums, target_sum):
    n = len(nums)

    # Sort the list
    nums.sort()

    # Iterate  the list and find triplets
    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target_sum:
                # Triplet found
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    # No triplet found
    return None

# Example
nums = [10, 20, 30, 9]
target_sum = 59

result = findtripletwithsum(nums, target_sum)

if result:
    print(f"Triplet with sum {target_sum} found: {result}")
else:
    print(f"No triplet found with sum {target_sum}")