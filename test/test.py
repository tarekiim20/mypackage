from mypackage import myModule

def test_top_n():
    """make sure top_n function works correctly
    """
    assert myModule.top_n([2,5,6,4,5], 2) == [6, 5], 'incorrect'