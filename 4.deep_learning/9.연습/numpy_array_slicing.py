import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 8])
print(a)
print(a[1:3])
print(a[-1])
print(a[-2])
print(a[5])
print(a[6])

a[0:2] = 9
print(a)

print('## b is below ##')
b = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])
print(b[:, -1])
print(b[:, [-1]])
print(b[:, 0:-1])
print(b[-1])
print(b[-1, :])
print(b[-1, ...])
print(b[0:2, :])

