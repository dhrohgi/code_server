import pandas as pd
import matplotlib.pyplot as plt

data = {
    "ID": ["a1", "a2", "a3", "a4", "a5"],
    "X1": [1, 2, 3, 4, 5],
    "X2": [3.0, 4.5, 3.2, 4.0, 3.5]
}

my_data = pd.DataFrame(data, index=["a", "b", "c", "d", "e"])
print(my_data)

print(my_data.columns)
print(my_data["X1"])

my_data.to_csv("456.csv")
