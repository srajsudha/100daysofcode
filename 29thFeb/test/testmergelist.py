from merge_sorted_list import merge_list

def test_merge_list():
    assert [1,1,2,2,3,4] == merge_list([1,2,3],[1,2,4])