def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError as e:
        return 0
