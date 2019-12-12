def index_of(haystack, needle):
  for i in range(len(haystack)):
    if (needle == haystack[i]):
      return i

  return -1


def chess(board):
  move = 0

  tower = index_of(board, "v")
  target = index_of(board, "c")

  board[tower] = "."

  reachable = {tower}

  while (move < 32):
    reachable_this_move = set()

    for state in reachable:
      col = state % 8
      row = state // 8

      if (state == target):
        return move

      # Up
      for x in range(1, row + 1):
        pos = state - x * 8

        if (board[pos] == "x"):
          break

        reachable_this_move.add(pos)

      # Down
      for x in range(1, 8 - row):
        pos = state + x * 8

        if (board[pos] == "x"):
          break

        reachable_this_move.add(pos)

      # Left
      for x in range(1, col + 1):
        pos = state - x

        if (board[pos] == "x"):
          break

        reachable_this_move.add(pos)

      # Right
      for x in range(1, 8 - col):
        pos = state + x

        if (board[pos] == "x"):
          break

        reachable_this_move.add(pos)

    for state in reachable_this_move:
      reachable.add(state)

    move += 1

  return -1


position = ""
for _ in range(8):
  position += input()

position = list(position)

# position = [
#     ".", ".", ".", ".", ".", ".", ".", ".",
#     ".", ".", ".", "x", "x", ".", ".", ".",
#     ".", ".", "v", "x", ".", "x", ".", ".",
#     ".", ".", ".", "x", "c", "x", ".", ".",
#     ".", ".", ".", "x", ".", ".", "x", "x",
#     ".", ".", ".", "x", "x", "x", "x", ".",
#     ".", ".", "x", ".", ".", ".", ".", ".",
#     ".", ".", ".", ".", "x", ".", "x", "."
# ]

# print(position)

moves = chess(position)
print(moves)


# ........
# ...xx...
# ..vx....
# ...xc...
# ...x....
# ...xx...
# ........
# ....x.x.
