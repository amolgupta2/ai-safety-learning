class: Matrix

  def __init__(self, data):
    # data is a list of lists
    # e.g. Matrix([[1, 2], [3, 4]])
    self.data = data
  
  def __str__(self):
    temp  = "" # Initializing String Var to return
    for i in range(len(self.data)): # Cycling through each list within the list
      for j in range(len(self.data[i])): # Cycling throug each index in the list
       temp = temp + str(self.data[i][j]) + " " # Concatenating each int in the Matrix
      temp = temp + "\n" # Printing a new line to represent a new row for the new list
    return temp # Return the string
  
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
  
  def transpose(self):
    result = [0] * len(self.data[0]) # Initializing the new array with the amount of rows = the amount of columns of the inputted Matrix
    for i in range(len(result)): # Cycling through the columns of the old matrix
      temp = [] # temporary array to contain data which will refresh as a new array every loop
      for j in range(len(self.data)): # Cycling through the rows of the matrix
        temp.append(self.data[j][i]) # Selecting the first index from each row, then 2nd index from each row, and ...
      result[i] = temp # Takes the array containing the column values and adds it as a list of lists
    return Matrix(result) # Return the Transposed Matrix
  
  def shape(self):
    # Resulting message displaying the proper shape of the matrix by using len(self.data) as rows and len(self.data[0]) as columns
    return (len(self.data), len(self.data[0]))
