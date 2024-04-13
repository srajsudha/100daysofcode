from mutability import duplicate_items, items

def test_duplicate_items():
    item_copy = duplicate_items(items)
    assert item_copy == items

    item_copy[0]['name'] = 'macbook'
    item_copy[1]['id'] = 4
    item_copy[2]['value'] = 30
    

    assert items[0]['name'] =='laptop'