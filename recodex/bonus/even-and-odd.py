# first = True
# odd = []
# nums = list(map(int, input().split()))

# for i in range(len(nums) - 1):
#   num = nums[i]
#   if (num % 2 == 0):
#     odd.append(str(num))
#   else:
#     if (not first):
#       print(" ", end="")
#     else:
#       first = False
      
#     print(num, end="")

# print(" " + " ".join(odd))

res = [[], []]
arr = list(map(int, input().split()))
arr = arr[:-1]
# print(arr)
for element in arr:
    if (element % 2 == 0):
        res[0].append(element)
    else:
        res[1].append(element)


def flattenList(arr, res=[]):
    for element in arr:
        if (type(element) is list):
            flattenList(element, res)

        else:
            res.append(element)

    return res


result = flattenList(res)
res_string = ""
for element in result:
    res_string += str(element) + " "

print(res_string.strip())