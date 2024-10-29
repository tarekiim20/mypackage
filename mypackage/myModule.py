def top_n(list, n):
    """Return the top n numbers from a list in desc order.

    Args:
        list (list): list or array-like type
        n (int): the first n numbers of the list
    
    Returns:
        list of n numbers of a list in desc order.
    """
    for i in range(n):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    top_n = list[-n:]
    
    return top_n[::-1]