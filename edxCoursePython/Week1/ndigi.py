def ndigits(x):
    '''
    This function should return the number of digits in the integer x.
    :param x: parameter - positive or negative integer number
    :return: number of digits that the parameter has
    '''
    if abs(x) < 10:
        return 1
    return 1 + ndigits(x / 10)
