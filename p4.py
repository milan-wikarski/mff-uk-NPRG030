import copy

maximal = []
current = []

numBefore = None
num = None

count = 0

while (1):
  count += 1

  numBefore = num
  num = int(input())

  if (numBefore is None):
    continue

  if (numBefore < num):
    if (len(current) == 0):
      current.append(str(numBefore))

    current.append(str(num))

  if (numBefore >= num or num == -1 or count >= 10000):
    if (len(current) > len(maximal)):
      maximal = copy.deepcopy(current)

    current = []

  if (num == -1 or count >= 10000):
    break

print("\n".join(maximal))
