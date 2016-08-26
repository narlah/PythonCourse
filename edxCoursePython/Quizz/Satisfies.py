def f(s):
    return 'a' in s


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    correction = 0
    for x in range(0, len(L)):
        x -= correction
        if not f(L[x]):
            del L[x]
            correction += 1
    return len(L)


L = ['a', 'b', 'a', 'kopeleee', 'mamata']
#L = ['z', 'k', 'nikol']
print satisfiesF(L)
print L
