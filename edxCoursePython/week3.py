def gcdRecur(a, b):
    if b == 0:
        return a
    return gcdRecur (b,a%b)

print gcdRecur(0,0)

# def gcdIter(a, b):
#     divisor = a if a <= b else b
#     for k in range(divisor, -1, -1):
#         if (a % k == 0) & (b % k == 0):
#             return k
#         else:
#             k -= 1
#     return 1
#
#
# print gcdIter(21, 4)
# def recurPowerNew(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return base
#     if exp % 2 ==0:
#         return recurPowerNew(base* base, exp /2)
#     else :
#         return base * recurPowerNew(base, exp - 1)
#
#
# print recurPowerNew(-5, 3)
