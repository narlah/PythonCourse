import math
balance = 320000
annualInterestRate = 0.2
months = 12
monthly_interest_rate = annualInterestRate / months


def test(testBalance, testC):
    for i in range(1, months + 1):
        testBalance -= testC
        testBalance += testBalance * (annualInterestRate / 12)
    if round(testBalance, 3) < 0.001 and round(testBalance, 3) > -0.001:
        return 0
    elif testBalance < 0:
        return -1
    elif testBalance > 0:
        return +1


# calculatedC = (balance / months) * (annualInterestRate / (1 - math.pow(math.e, -annualInterestRate)))
coef = math.pow(math.e, -1 * months * math.log(1 + monthly_interest_rate, math.e))
good_starting_point = (balance * monthly_interest_rate) / (1 - coef)

k = test(balance, good_starting_point)
lower = good_starting_point - good_starting_point * 1 / 50
upper = good_starting_point
pos = 0
while k != 0:
    pos = (upper + lower) / 2
    k = test(balance, pos)
    if k < 0:
        upper = pos
    elif k > 0:
        lower = pos
print 'Lowest Payment: ' + str(round(pos, 2))
