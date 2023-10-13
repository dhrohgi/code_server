import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.cos(x)
k = np.sin(x)
q = np.tan(x)
plt.plot(x, y, marker='x')
plt.plot(x, k, marker='o')
plt.plot(x, q)
plt.show()
