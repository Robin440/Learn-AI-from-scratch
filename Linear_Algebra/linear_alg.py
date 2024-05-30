import numpy as np

# Define vectors
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# Vector addition
print("u + v =", u + v)

# Scalar multiplication
print("3 * u =", 3 * u)

# Dot product
print("u . v =", np.dot(u, v))

print("--------------------------------------------------------")

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
print("A + B =\n", A + B)

# Scalar multiplication
print("3 * A =\n", 3 * A)

# Matrix multiplication
print("A @ B =\n", A @ B)
