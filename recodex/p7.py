def isPrime(num):
    if (num <= 1):
        return False

    i = 2
    iMax = num ** 0.5

    while (i <= iMax):
        if (num % i == 0):
            return False

        i += 1

    return True


print("ano" if isPrime(int(input())) else "ne")
