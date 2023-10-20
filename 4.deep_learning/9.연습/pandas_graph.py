import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(20, 6), columns=["A", "B", "C", "D", "E", "F"])
print(df)
df.plot()
plt.show()