class Neighbours:
  def __init__(self, top=None, right=None, down=None, left=None):
    self.top = top
    self.right = right
    self.down = down
    self.left = left
    
  @property
  def empty(self):
    return (self.top is None and self.right is None and self.down is None and self.left is None) 

class Board:
  def __init__(self):
    self.pieces = dict()
    
  def get_neighbours(self, x, y):  
    res = Neighbours()
    
    if ((x + 1, y) in self.pieces):
      res.down = self.pieces[(x + 1, y)]
      
    if ((x - 1, y) in self.pieces):
      res.top = self.pieces[(x - 1, y)]
      
    if ((x, y + 1) in self.pieces):
      res.right = self.pieces[(x, y + 1)]
      
    if ((x, y - 1) in self.pieces):
      res.left = self.pieces[(x, y - 1)]

    return res
  
  def can_add_piece(self, piece):
    # print(piece)

    if (len(self.pieces) == 0):
      return (piece.x == 0 and piece.y == 0)
    
    if ((piece.x, piece.y) in self.pieces):
      # print("in")
      return False
    
    neighbours = self.get_neighbours(piece.x, piece.y)
    
    
    if (neighbours.empty):
      return False
    
    # Left
    if (neighbours.left is not None):
      if (neighbours.left.right != piece.left):
        return False
    
    # Right
    if (neighbours.right is not None):
      if (neighbours.right.left != piece.right):
        return False
      
    # Top
    if (neighbours.top is not None):
      if (neighbours.top.down != piece.top):
        return False
    
    # Down
    if (neighbours.down is not None):
      if (neighbours.down.top != piece.down):
        return False
    
    return True
    
  def add_piece(self, piece):
    self.pieces[(piece.x, piece.y)] = piece
    
  def __str__(self):
    res = []
    for key in self.pieces:
      res.append(self.pieces[key].__str__())

    return "\n".join(res)

class Piece:
  def __init__(self, spec, x, y):
    self.top = spec[0]
    self.right = spec[1]
    self.down = spec[2]
    self.left = spec[3]

    self.x = x
    self.y = y
    
  def __str__(self):
    return "{}{}{}{} | ({}, {})".format(self.top, self.right, self.down, self.left, self.x, self.y)
    
board = Board()

# pieces = [
#   Piece("MCLC", 0, 0),
#   Piece("LMML", -1, 0),
#   Piece("CLCL", -1, -1),
#   Piece("CCMM", 0, -1),
#   Piece("LCLC", 0, 1),
#   Piece("LLLM", 1, 1),
#   Piece("LLCL", -2, 0),
#   Piece("LLLL", -2, 1)
# ]

pieces = []
while True:
    try:
      line = input()
      if line == '':
          break
    except:
      break
    
    args = line.split(" ")
    pieces.append(Piece(args[0], int(args[1]), int(args[2])))

for piece in pieces:
    if (board.can_add_piece(piece)):
      print("ANO")
      board.add_piece(piece)
    else:
      print("NE")

    

# for piece in test:
  

# board.add_piece(Piece("MCLM", 0, 0))
# board.add_piece(Piece("LMML", -1, 0))

# print(board.can_add_piece(Piece("MMMC", 1, 0)))