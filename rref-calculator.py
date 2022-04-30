from random import randint

def displayMatrix(matrix):
  for row in matrix:
    print('[', end='')
    for cell in row:
      print('{0:>7.2f}'.format(cell + 0), end=' ')
    print(']')
  print()

def randomMatrix(rows, cols):
  m = []
  for i in range(rows):
    row = []
    for i in range(cols):
      row.append(randint(0, 10))
    m.append(row)
  return m

# divide every cell in that row by the number in the spot going to be the
# leading one
def leadingOne(matrix, i):
  if matrix[i][i] == 0:
    return
  matrix[i] = [cell / matrix[i][i] for cell in matrix[i]]

# zero out all cells above and below the pivot cell
# will be done after getting a leading one, so
# find the scale factor = -1 * cell we want to zero, then add 
# scale factor * leading one row cell to each zero row cell
def pivot(matrix, i):
    for r, row in enumerate(matrix):
    if r != i:
      scale = -1 * row[i]
      matrix[r] = [curr + scale * other for curr, other in zip(matrix[r], matrix[i])]

def rref(matrix):
  for i in range(len(matrix)):
    leadingOne(matrix, i)
    pivot(matrix, i)
  return matrix

# m1 = [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]

# m2 = [[1, 2, 1],
#       [-2, -3, 1],
#       [3, 5, 0]]

# m3 = [[-1, 1, -4, 2],
#       [0, 2, 5, -6],
#       [2, 3, 1, -2]]

# m4 = [[1, -1, -1, 2, 0],
#       [0, 1, 4, 3, 10],
#       [0, 0, 1, 1, 2,]]

m = randomMatrix(5, 8)

print('Original matrix:')
displayMatrix(m)
print('RREF form:')
displayMatrix(rref(m))
