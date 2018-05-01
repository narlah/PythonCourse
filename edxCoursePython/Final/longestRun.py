import sys


def longest_run(l):
    longest = 0
    current_longest = 0
    current_val = -sys.maxsize - 1
    for i in range(len(l)):
        if l[i] >= current_val:
            current_longest += 1
        else:
            if current_longest > longest:
                longest = current_longest
            current_longest = 1
        current_val = l[i]
    return longest if current_longest < longest else current_longest


print(longest_run([-1, -2, -3, -4, -5, -6, -7, 2, 3]))
