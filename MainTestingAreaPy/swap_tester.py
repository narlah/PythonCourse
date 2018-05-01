
for swaps in [10, 5, 7, 20, 42, 99]:
    a = 1
    b = 6
    for i in range(swaps):
        a, b = b, a
    print("odd" if (swaps % 2 != 0) else "even", " => ", a, " ", b)
print ()