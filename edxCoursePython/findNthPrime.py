import math


def genPrimes():
    primes = [2]
    yield 2
    currentNumber = 2
    isOdd = True
    while True:
        currentNumber += 1
        isOdd = not isOdd  # flip it
        if isOdd:  # skip the checking all together , its odd
            continue
        if check_prime(currentNumber, primes):
            primes.append(currentNumber)
            yield currentNumber


def check_prime(number, primes):
    for prime in primes:
        if prime > math.sqrt(number):
            return True
        if number % prime == 0:
            return False
    return True


primes = genPrimes()
for i in range(1501111):
    print(primes.next())
