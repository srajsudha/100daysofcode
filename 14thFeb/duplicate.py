"""
The duplicates_only function accepts an iterable and returns a new iterable of all items that are duplicated in the original iterable:

>>> duplicates_only([2, 1, 3, 2, 4, 3, 2])
[2, 3]
"""

lst = [2, 1, 3, 2, 4, 3, 2]
unique_item = []
non_unique_item = set()

for i in lst:
    if i not in unique_item and i not in non_unique_item:
        unique_item.append(i)
    elif i in unique_item:
        unique_item.remove(i)
        non_unique_item.add(i)
        

# for i in lst:
#     if i not in unique_item:
#         unique_item.append(i)
#     else:
#         non_unique_item.append(i)
#         unique_item.remove(i)

print(unique_item)
print(non_unique_item)