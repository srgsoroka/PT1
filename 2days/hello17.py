def add(x, y):
    """Add x and y
    >>> add(2,3)
    5
    >>> add(-1,1)
    Traceback (most recent call last):
    ...
    ValueError
    """
    if x < 0:
        raise ValueError
    return x + y
###doctest with error
