#Editing problem - what is the minimum number of steps we can take to get two strings to equal each other with delete / insert / mismatch 
def alignment_problem(masterString, editedString):
  #master string has the number of columns
  #edited string has the number of rows 

  i = len(masterString)+1
  j = len(editedString)+1
  rows, cols = (j,i) 

  matrix = [[0 for i in range(cols)] for j in range(rows)]
  
  for e in range(0,i,1):
    matrix[0][e] = e
  
  for a in range(0,j,1):
    matrix[a][0] = a

  for y in range(1, j):
    for u in range(1,i):
      insertion = matrix[y][u-1] +1
      deletion = matrix[y-1][u]+1
      match = matrix[y-1][u-1]
      mismatch = matrix[y-1][u-1]+1
      if masterString[u-1] == editedString[y-1]:
        matrix[y][u] = min(insertion,deletion,match)
      else:
        matrix[y][u] = min(insertion,deletion,mismatch)

  print_matrix(matrix)

  return matrix[j-1][i-1]

def print_matrix(matrix):
  print("LEVENSHTEIN DISTANCE MATRIX:")
  for i in range(len(matrix)):
    for e in range(len(matrix[0])):
      print(str(matrix[i][e]),end=" ")
    print("\n",end="")
  print("\n")

print("ANSWER: " + str(alignment_problem("sitting","kitten")))
