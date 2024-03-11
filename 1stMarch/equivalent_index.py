"""
Given a list of integers, find the index at which the sum of the left half of the list is equal to the right half.

If there is no index where this condition is satisfied return -1.
"""

nums = [1, 7, 3, 5, 6]

for i in range(1, len(nums)-1):
    left_sum = sum(nums[:i])
    right_sum = sum(nums[i+1:])
    if left_sum == right_sum:
        print(i)
print (-1)
    
    
