import pytest
from functools import reduce
from task.app import MergeGenerator

def test_empty_list():
    mg = MergeGenerator()
    assert mg.gen_main() == []

def test_one_empty_list():
    mg = MergeGenerator(
        [1, 5, 9], 
        [2, 5],
        [],
        [1, 6, 10, 11],
        [8, 7, 4, 15]
    )

    assert mg.gen_main() == [1, 1, 2, 4, 5, 5, 6, 7, 8, 9, 10, 11, 15]

def test_merge_generator():

    mg1 =  MergeGenerator(
        [1, 5, 9], 
        [2, 5], 
        [1, 6, 10, 11],
        [8, 7, 4, 15]
    )

    assert mg1.gen_main() == [1, 1, 2, 4, 5, 5, 6, 7, 8, 9, 10, 11, 15]

def test_list_with_string_data():
    # When trying to concatenate a list of strings
    # to a list of integers
    mg2 =  MergeGenerator(
        "[1, 5, 9]", 
        [2, 5], 
        [1, 6, 10, 11],
        [8, 7, 4, 15]
    )
    with pytest.raises(TypeError):
        assert mg2.gen_main()

def test_size_of_input_output():
    nums = [
        [1, 5, 9], 
        [2, 5], 
        [1, 6, 10, 11],
        [8, 7, 4, 15]
        ]
    mg1 =  MergeGenerator(
        [1, 5, 9], 
        [2, 5], 
        [1, 6, 10, 11],
        [8, 7, 4, 15]
    )
    assert reduce(lambda count, l: count + len(l), nums, 0) == len(mg1.gen_main())