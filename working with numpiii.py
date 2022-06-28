import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 2*np.pi, 100)
# y=np.sin(x)
# plt.plot(x,y)
# # print(x)
# # print(y)

# z=np.array([1,2,4,6,4,4,565])
# print(z)
# c=z.mean()
# print(c)

# u = np.array([1, 0])
# v = np.array([0, 1])
# z = np.add(u, v)
# print(z)

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
A.ndim
A.shape
A.size
A[1, 2]
A[0:2, 2]


X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]])
Z = X + Y
P = 2 * Y
F=X * Y

A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
# multiplication of two matrixes
Z = np.dot(A,B)


C = np.array([[1,1],[2,2],[3,3]])
# Get the transposed of C
C.T

