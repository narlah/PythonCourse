import sys
import unittest


def findDuplicates(arr):
    print(arr)
    # STEP 1: GET INSIDE A CYCLE
    # start at position n-1 and walk n steps to find a position guaranteed to be in a cycle
    n = len(arr)
    pos = n
    for i in range(n * 2):
        pos = arr[pos - 1]
        #print(pos)

    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    pointOfOrigin = pos
    pos = arr[pos - 1]
    lengthOfCycle = 1
    while pos != pointOfOrigin:
        pos = arr[pos - 1]
        lengthOfCycle += 1
        #print(pos)
    #print("leght ->" + str(lengthOfCycle))
    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # start two pointers
    #   (1) at position n-1
    #   (2) ahead of position n-1 as many steps as the cycle's length
    posForward = n
    for i in range(lengthOfCycle):
        #print(arr[posForward - 1])
        posForward = arr[posForward - 1]
    pos = n
    while pos != posForward:
        posForward = arr[posForward - 1]
        pos = arr[pos - 1]

    #print("result : " + str(pos) + " " + str(arr[pos]))
    return pos


def find_duplicate(list):
    """find a duplicate of 1..n in a list n+1 elements long"""
    n = len(list)
    if n <= 1:
        raise Exception("not enough")
    i = n
    j = n
    while True:
        # print("looking for cycle: i %s j %s" % (i, j))
        i = list[i - 1]  # tortoise
        j = list[j - 1]  # hare
        j = list[j - 1]  # hare
        if i == j:
            print("cycle found at %s" % i)
            break

    # we found a cycle
    # now restart j
    # and loop until j meets i again
    # and that's the start of the cycle (or the dup)

    j = n
    while True:
        # print("looking for dup: i %s j %s" % (i, j))
        i = list[i - 1]
        j = list[j - 1]
        if i == j:
            print("dup found at %s" % i)
            break

    print("dup is %s" % i)
    return i


class FindDuplicateTest(unittest.TestCase):
    arr2 = [2, 3, 4, 5, 6, 7, 2, 1]  # lengthOfCycle = 4
    arr4 = [1, 8, 6, 5, 2, 3, 9, 4, 7, 4]
    arr5 = [5, 2, 3, 5, 4, 6, 7, 1]

    def test_case1(self):
        answer = findDuplicates([2, 3, 4, 5, 6, 7, 2, 1])
        self.assertEqual(answer, 2)

    def test_case2(self):
        answer = find_duplicate([2, 3, 4, 5, 6, 7, 2, 1])
        self.assertEqual(answer, 2)

    def test_case3(self):
        answer = findDuplicates([1, 8, 6, 5, 2, 3, 9, 4, 7, 4])
        self.assertEqual(answer, 4)

    def test_case4(self):
        # danger! Maybe looped
        answer = find_duplicate([1, 8, 6, 5, 2, 3, 9, 4, 7, 4])
        self.assertEqual(answer, 4)

    def test_case5(self):
        answer = findDuplicates([5, 2, 3, 5, 4, 6, 7, 1])
        self.assertEqual(answer, 5)

    def test_case6(self):
        with self.assertRaises(Exception):
            find_duplicate([1])


suite = unittest.TestLoader().loadTestsFromTestCase(FindDuplicateTest)
unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
