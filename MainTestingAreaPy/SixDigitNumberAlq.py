for i in range(100000, 999999):
    if i % 3 == 0:
        i2 = ((i % 10) * 100000) + (i // 10)
        if i == i2 * 3:
            print("FOUND " + str(i) + " " + str(i2))

        # i was young , stupid and tired , ok just two of those :P

        # s = list(str(i))
        # z = list(s[-1])
        # z.extend(s[:-1])
        # l1 = int(''.join(map(str, s)))
        # l2 = int(''.join(map(str, z)))
