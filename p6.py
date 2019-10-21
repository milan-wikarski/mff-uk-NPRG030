res = []

num = int(input())
base = int(input())

while (num > 0):
    res.append(str(num % base))
    num = num // base

print("".join(reversed(res)))
