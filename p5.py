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


i = 2
res = []

num = int(input())
orgNum = num

while (num > 1):
    if (isPrime(i) and num % i == 0):
        num = num // i
        res.append(str(i))
        i = 1

    i += 1

print(str(orgNum) + "=" + "*".join(res))
