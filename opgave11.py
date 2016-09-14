import pandas as pd
import numpy as np

data = pd.pandas.read_csv("data.csv")

df = pd.DataFrame(data.row.str.split("",1).tolist(),columns=['flips','row'])

print(df)






