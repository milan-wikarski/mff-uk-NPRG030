def arrSwap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

    return arr


def arrBubbleSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                arrSwap(arr, j, j + 1)

    return arr


arr = []
num = None

while (1):
    num = int(input())

    if (num == -1):
        break

    arr.append(num)

print("\n".join(map(str, arrBubbleSort(arr))))
