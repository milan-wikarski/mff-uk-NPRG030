def last(arr):
    if (len(arr) > 0):
        return arr[len(arr) - 1]

    return None


def arrCopy(arr, append=None):
    res = []

    for el in arr:
        res.append(el)

    if (append is not None):
        res.append(append)

    return res


def split(num, opts, parts=[]):
    if (num == 0):
        print(" ".join(map(str, parts)))

    else:
        for opt in opts:
            if (num >= opt and (last(parts) is None or last(parts) >= opt)):
                split(num - opt, opts, arrCopy(parts, opt))


kinds = input()
opts = []

for opt in (input()).split(" "):
    opts.append(int(opt))

num = int(input())

split(num, opts)
