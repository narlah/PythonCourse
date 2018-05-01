def hanoi(n, source, help, target):
    source = [4, 3, 2, 1]
    helper = []
    target = []
    hanoi(len(source), source, helper, target)


hanoi(3, 1, 0, 3)
