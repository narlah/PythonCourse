def dict_invert(d=None):
    if d is None:
        d = {}
    result = {}
    for key in d:
        val = d[key]
        if result.has_key(val):
            result[val] = result[val] + [key]
        else:
            result[val] = [key]
    for k in result:
        l = result[k]
        list.sort(l)
        result[k] = l
    return result


print dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
print dict_invert({4: True, 2: True, 0: True})
print dict_invert({8: 6, 2: 6, 4: 6, 6: 6})
