for i in range(100000, 999999):
    if i % 3 == 0:
        s = list(str(i))
        z = list(s[-1])
        z.extend(s[:-1])
        l1 = int(''.join(map(str, s)))
        l2 = int(''.join(map(str, z)))
        if l1 == l2 * 3:
            print("FOUND " + str(l1) + " " + str(l2))