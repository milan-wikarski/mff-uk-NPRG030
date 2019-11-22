def fill(value, length):
  res = []

  for i in range(length):
    res.append(value)

  return res


def ifelse(condition, t, f):
  if (condition):
    return t

  return f


def arr_copy(arr):
  res = []

  for item in arr:
    res.append(item)

  return res


def arr_replace(arr, index, value):
  arr[index] = value

  return arr


def arr_append(arr, value):
  arr.append(value)

  return arr


def chess(width, height, x, y):
  MOVES = [[2, 1], [2, -1], [-2, 1], [-2, -1],
           [1, 2], [1, -2], [-1, 2], [-1, -2]]

  result = [False]
  size = width * height

  def run(x, y, moves, fields, result):
    if (result[0]):
      return

    fields[x + y * width] = 1
    moves += 1

    if (moves == size):
      result[0] = True
      return

    for move in MOVES:
      new_x = x + move[0]
      new_y = y + move[1]

      if (not (new_x >= width or new_x < 0 or new_y >= height or new_y < 0 or fields[new_x + new_y * width] == 1)):
        run(new_x, new_y, moves,
            fields[:], result)

  run(x, y, 0, fill(0, size), result)

  return ifelse(result[0], "ANO", "NE")


# Input
args = list(map(int, input().split(" ")))
print(chess(args[0], args[1], args[2] - 1, args[3] - 1))

# print(chess(10, 3, 0, 0))
