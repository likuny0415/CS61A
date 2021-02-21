def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if s1 and s2:
        if s1[0] > s2[0]:
            s1, s2 = s2, s1
        return [s1[0]] + merge(s1[1:], s2)
    return s1 + s2
