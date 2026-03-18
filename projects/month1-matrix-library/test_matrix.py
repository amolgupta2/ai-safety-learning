from Matrix import Matrix

# Test __add__
a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
print(a + b)  # Expected: [[6, 8], [10, 12]]

a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[1, 1, 1], [1, 1, 1]])
print(a + b)  # Expected: [[2, 3, 4], [5, 6, 7]]

# Test __mul__
a = Matrix([[1, 2], [3, 4]])
b = Matrix([[1, 0], [0, 1]])
print(a * b)  # Expected: [[1, 2], [3, 4]]

a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[7, 8], [9, 10], [11, 12]])
print(a * b)  # Expected: [[58, 64], [139, 154]]
