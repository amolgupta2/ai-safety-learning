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
