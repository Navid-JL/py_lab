import numpy as np

A = np.array([[8, 3], [4, 2]])

B = np.array([9, 7])

C = np.linalg.solve(A, B)

print(C)
