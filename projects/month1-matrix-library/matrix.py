class: Matrix

def __init__(self, data):
  # data is a list of lists
  # e.g. Matrix([[1, 2], [3, 4]])
  self.data = data

def __str__(self):
  return '\n'.join([str(row) for row in self.data])
