class: Matrix

def __init__(self, data):
  # data is a list of lists
  # e.g. Matrix([[1, 2], [3, 4]])
  self.data = data

def __str__(self):
  return '\n'.join([str(row) for row in self.data])

def __add__(self, other):
  if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
    result = [0] * len(self.data) # Defining the result array
    for i in range(len(self.data)):
      result[i] = self.data[i].copy()
    for i in range(len(self.data)):
        for j in range(len(self.data[0])):
            result[i][j] = self.data[i][j] + other.data[i][j]
    return Matrix(result)
  else:
    raise ValueError("Matrices must have the same dimensions")

def __mul__(self, other):
  if len(self.data[0]) == len(other.data):
    # Initializing the Result Matrix
    result = [0] * len(self.data)
    result_temp = [0] * len(other.data[0])

    # Adding in the columns for the Result Matrix
    for i in range(len(result)):
      result[i] = result_temp.copy()

    # The Matrix Multiplication  
    for i in range(len(self.data)): # Rows in C
      for j in range(len(other.data[0])): # Columns in C
        for k in range(len(other.data)): # Columns in A and Rows in B
          result[i][j] += other.data[k][j] * self.data[i][k]
    
    return Matrix(result)
  else:
    raise ValueError("First Matrix's columns must match the Second Matrix's rows")
