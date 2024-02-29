"""
Given two sorted lists, write a function to merge them into one sorted list.

Bonus: What’s the time complexity?
"""

list1 = [1,2,5]
list2 = [2,4,6]

def merge_list(list1:list, list2:list)->list:
    return sorted(list1+list2)