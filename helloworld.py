#import numpy as np
import pandas as pd
import os
cwd = os.getcwd()
print(cwd) #/app

df = pd.read_csv("./src/data/testi.csv")
print("Hello world!")
print(df.columns)
print(df["title"].tolist())
df.to_csv("./data/output.csv")

print(os.path.exists("./data/output.csv"))

print(os.path.exists("/app/data/output.csv"))

print('done8')
