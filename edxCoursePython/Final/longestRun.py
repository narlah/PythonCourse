import sys


def longestRun(L):
    longest = 0
    current_longest = 0
    current_val = -sys.maxint - 1
    for i in range(len(L)):
        if L[i] >= current_val:
            current_longest += 1
        else:
            if current_longest > longest:
                longest = current_longest
            current_longest = 1
        current_val = L[i]
    return longest if current_longest < longest else current_longest


print longestRun(L=[-1, -2, -3, -4, -5, -6, -7, 2, 3])
