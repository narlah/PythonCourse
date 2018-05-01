# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
# months = 12
# monthly_interest_rate = annualInterestRate / float(months)
# total_paid = 0
#
#
# for i in range(1, 13):
#     print "Month: " + str(i)
#     minimum_monthly_payment = monthlyPaymentRate * balance
#     unpaid_balance = balance - minimum_monthly_payment
#     balance = unpaid_balance +  unpaid_balance * monthly_interest_rate
#     print "Minimum monthly payment: " + str(round(minimum_monthly_payment,2))
#     print "Remaining balance: " + str(round(balance,2))
#     total_paid += minimum_monthly_payment
#
# print "Total paid: " + str(round(total_paid,2))
# print "Remaining balance: " + str(round(balance,2))


# import math
#
# balance = 229; annualInterestRate = 0.2
# months = 12
# monthly_interest_rate = annualInterestRate / months
#
# # Monthly interest rate = (Annual interest rate) / 12.0
# # Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#
# calculatedC = (balance / months) * (annualInterestRate / (1 - math.pow(math.e, -annualInterestRate)))
#
# print "have to pay : " + str(balance)
# print "calculated to pay: " + str( calculatedC * months)
# print "when rounded down you will be payng : " + str (round(calculatedC / 10) * 10 * 12)
#
# testBalance = balance
# testC = round(calculatedC / 10) * 10
# for i in range(1, 13):
#     testBalance -= testC
#     testBalance +=  testBalance*(annualInterestRate/12)
# print "is it bigger "  + str(testBalance)
# if testBalance > 0:
#     print math.ceil(calculatedC/10)*10
# else:
#     print round(calculatedC / 10) * 10

import math

balance = 320000
annualInterestRate = 0.2
months = 12
monthly_interest_rate = annualInterestRate / months


def test(testBalance, testC):
    for i in range(1, months + 1):
        testBalance -= testC
        testBalance += testBalance * (annualInterestRate / 12)
    if round(testBalance, 4) == -0.0001:
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
print('Lowest Payment: ' + str(round(pos, 2)))
