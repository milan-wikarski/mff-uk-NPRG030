# =======================================================
# ==============   MATRIX REPRESENTATION   ==============
# =======================================================

from random import randrange


class XY:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  @staticmethod
  def rand(xy):
    return XY(randrange(0, xy.x), randrange(0, xy.y))

# Example input
# 9750046190
# 8342685339
# 3334272809
# 4964866423


# Params
rows = 4
cols = 10

# Create a list of random coordinates
coords = list(map(XY.rand, [XY(cols, rows)] * 5))

# Take random col and row
rowToPrint = randrange(0, rows)
colToPrint = randrange(0, cols)


#
# APPROACH ONE
#

print("APPROACH ONE: 2D --> 1D")
print("=============================================")
print("(x, y) --> items[y * cols + x]\n")

# 1.0 Generate items
# Create a list of size rows * cols
# Each item is a random number between 0-10
items = list(map(randrange, [cols] * (rows * cols)))

# 1.1 Print the items
print("Printing full matrix")
for row in range(rows):
  for col in range(cols):
    print(items[row * cols + col], end="")
  print()

print()

# 1.2 Print some values
print("Printing coordinates")
for coord in coords:
  print("({},{}) --> {}".format(coord.x, coord.y,
                                items[coord.y * cols + coord.x]))

print()

# 1.3 Print a row
print("Row {}".format(rowToPrint))
for i in range(rowToPrint * cols, (rowToPrint + 1) * cols):
  print(items[i], end="")

print("\n")

# 1.4 Print a column
print("Column {}".format(colToPrint))
for i in range(colToPrint, len(items), cols):
  print(items[i], end="")

print("\n")

# 1.5 Print the diagonal ([(0, 0), (1, 1), ...])
print("Diagonal")
for i in range(min(rows, cols)):
  print(items[i * cols + i], end="")
print("\n\n")

# 1.6 Input [TODO]

#
# APPROACH TWO
#

print("APPROACH TWO: 2 Dimensional List")
print("=============================================")
print("(x, y) --> items[y][x]\n")

# 2.0 Generate items
# Create a list of lists
# Each inner list with index I is the items of items in I-th row
items2 = []
for row in range(rows):
  items2.append([])
  for col in range(cols):
    items2[row].append(items[row * cols + col])


# 2.1 Print the items
print("Printing full matrix")

for row in range(rows):
  for col in range(cols):
    print(items2[row][col], end="")
  print()

print()

# 2.2 Print some values [TODO]
# 2.3 Print a row [TODO]
# 2.4 Print a column [TODO]
# 2.5 Print the diagonal ([(0, 0), (1, 1), ...]) [TODO]
# 2.6 Input [TODO]

#
# APPROACH THREE
#

print("APPROACH THREE: Dictionary")
print("=============================================")
print("(x, y) --> items[(x, y)]\n")

# 3.0 Generate items
items3 = dict()
for row in range(rows):
  for col in range(cols):
    items3[(col, row)] = items[row * cols + col]

# 3.1 Print the items
print("Printing full matrix")

for row in range(rows):
  for col in range(cols):
    print(items3[(col, row)], end="")
  print()

# 3.2 Print some values [TODO]
# 3.3 Print a row [TODO]
# 3.4 Print a column [TODO]
# 3.5 Print the diagonal ([(0, 0), (1, 1), ...]) [TODO]
# 3.6 Input [TODO]
