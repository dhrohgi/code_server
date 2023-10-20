import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pandas.csv')
print(df)
df.plot()
plt.show()
