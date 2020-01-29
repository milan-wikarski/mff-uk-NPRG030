POSSIBLE_MOVES = ["<", ">", "^", "v", "-", "0"]


def run():
  width = int(input())
  height = int(input())
  x = int(input())
  y = int(input())
  history = set()

  pos = [x, y]
  history.add(y * width + x)
  direction = None
  count = 0

  move = input()

  while (move in POSSIBLE_MOVES):
    if (move == "<"):
      direction = (-1, 0)
    elif (move == ">"):
      direction = (1, 0)
    elif (move == "^"):
      direction = (0, -1)
    elif (move == "v"):
      direction = (0, 1)
    elif (move == "0"):
      return "{} OK".format(count)

    pos[0] += direction[0]
    pos[1] += direction[1]

    pos_flat = pos[0] + pos[1] * width

    count += 1

    if (pos_flat in history or pos[0] < 0 or pos[0] >= width or pos[1] < 0 or pos[1] >= height):
      return "{} KO".format(count)

    history.add(pos_flat)

    move = input()


print(run())
