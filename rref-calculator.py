def displayMatrix(matrix):
  for row in matrix:
    print('[', end='')
    for cell in row:
      print(str(cell).rjust(5), end=' ')
    print(']')
  print()






def leadingOne(matrix, i):
  # divide every cell in that row by the number in the spot going to be the
  # leading one
  matrix[i] = [cell / matrix[i][i] for cell in matrix[i]]

def pivot(matrix, i):
  # zero out all cells above and below the pivot cell
  # will be done after getting a leading one, so
  # find the scale factor = -1 * cell we want to zero, then add 
  # scale factor * leading one row cell to each zero row cell
  for r, row in enumerate(matrix):
    if r != i:
      scale = -1 * row[i]
      matrix[r] = [curr + scale * other for curr, other in zip(matrix[r], matrix[i])]



def rref(matrix):
  for i in range(len(matrix)):
    leadingOne(matrix, i)
    pivot(matrix, i)
  return matrix




m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

m2 = [[1, 2, 1],
      [-2, -3, 1],
      [3, 5, 0]]

m3 = [[-1, 1, -4, 2],
      [0, 2, 5, -6],
      [2, 3, 1, -2]]

# displayMatrix(m3)
displayMatrix(rref(m3))
