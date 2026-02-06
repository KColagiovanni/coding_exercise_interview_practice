# Given a list of numbers, find the second largest number.
# O(n) time, O(1) space

numbers = [10, 5, 8, 20]

def second_largest(nums):
    if len(nums) < 2:
        return None

    largest = second = float('-inf')

    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n

    return second if second != float('-inf') else None

print(second_largest(numbers))