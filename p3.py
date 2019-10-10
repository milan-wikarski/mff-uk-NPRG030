res = None

while (1):
  num = int(input())
  if (num == -1):
    break;
  if (res is None):
    res = num
  else:
    res = max(res, num)

print(res)
