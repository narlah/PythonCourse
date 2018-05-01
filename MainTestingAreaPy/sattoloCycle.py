from random import randrange


# def sattoloCycle(items):
#     for i in range(len(items) - 1, 0, -1):
#         j = randrange(i)  # 0 <= j <= i-1
#         items[j], items[i] = items[i], items[j]
#
#  # Tests
# for _ in range(10):
#     lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     sattoloCycle(lst)
#     print(lst)
def sattolo_cycle(items):
    for i in range(len(items) - 1, 1, -1):
        j = randrange(i - 1)  # 0 < j <= i-1
        # print(str(i) + " " + str(j) + " ----> " +str(items))
        items[j], items[i] = items[i], items[j]
    return items


# Tests
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for _ in range(10):
    lst = sattolo_cycle(lst)
    print(lst)
