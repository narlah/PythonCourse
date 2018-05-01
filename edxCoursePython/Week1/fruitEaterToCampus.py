def nfruits(dictionary, stringPattern):
    """
    :param dictionary: dict with fruit names as capital letters and values explaining how many the user had
        example : {'A': 1, 'B': 2, 'C': 3}
    :param stringPattern: The pattern he used to eat while going to campus
        example :  'ACCA'
    :return: the max quantity that fruit can have when he gets to the campus
        example- the above values would product this result
        in the end of computation dictionary would have this state {'A': 0, 'C': 2, 'B': 5} and value returned is 5
    """
    length = len(stringPattern)
    count = 0
    for eatenFruit in stringPattern:
        count += 1
        if length != count:
            update_dictionary(dictionary, eatenFruit)
        else:
            dictionary[eatenFruit] -= 1
    return determine_max(dictionary)


def update_dictionary(dictionary, except_this_key=""):
    """
    :param dictionary:  dict with fruit names as capital letters and values explaining how many the user had
        example : {'A': 1, 'B': 2, 'C': 3}
    :param except_this_key: all other keys we will update with +1 , this one tho - we will substract 1
    :return: dictionary that has all elements updated by +1 except TheONE(tm) that will be updated with -1
        in this example and with exceptOneKey = "A" , the result would be {'A': 0, 'B': 3, 'C': 4}
    """
    for key in dictionary.iterkeys():
        if key != except_this_key:
            dictionary[key] += 1
        else:
            dictionary[key] -= 1


def determine_max(dictionary):
    """
    :param dictionary: dict with fruit names as capital letters and values explaining how many the user had
        example : {'A': 1, 'B': 2, 'C': 5}
    :return: the max of all quantities in the dict
        example : in this case the result is equal to 5
    """
    max = 0
    for key in dictionary.iterkeys():
        if dictionary[key] > max:
            max = dictionary[key]
    return max


print(nfruits({'A': 1, 'B': 2, 'C': 3}, 'ACCA'))
