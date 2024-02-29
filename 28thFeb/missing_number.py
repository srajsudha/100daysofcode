"""
You have an array of integers, nums of length n spanning 0 to n with one missing. Write a function missing_number that returns the missing number in the array.

Note: Complexity of 
�
(
�
)
O(n) required.

Example:

Input:

nums = [0,1,2,4,5] 
missing_number(nums) -> 3
"""

nums = [12,14,17,19] 
nums.sort()
print(nums)

num_set = set()
numbers = []
for i in range (nums[0],nums[-1]):
    if i not in nums:
        numbers.append(i)

print(numbers)