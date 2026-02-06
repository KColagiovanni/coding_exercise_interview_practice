# Given a list of integers and a target number, return the indices of the two numbers that add up to the target.
# Assume exactly one solution exists.

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    seen = {}

    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i

print(two_sum(nums, target))