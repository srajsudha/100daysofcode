from copy import deepcopy
items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    new_list = deepcopy(items)
    # new_list = [item.copy() for item in items]
    return new_list

func_object = duplicate_items(items)
print(func_object)