import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b

print(f'c 는 넘파이로 만든 배열 {c} 입니다.')


d = np.arange(1, 101)
e = np.average(d)
print(d)
print(e)

f = np.random.random(10)
g = np.random.random(10)
h = np.random.random(10)
print(f)

plt.plot(f, g, h)
plt.pcolor()
plt.title('hello world')
plt.ylabel('y value')
plt.xlabel('x value')
plt.legend(['test1'], loc = 'upper left')
plt.show()
