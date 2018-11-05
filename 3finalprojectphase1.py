
import pandas as pd
import io
import requests
import numpy as np
url='https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
s=requests.get(url).content
#df=pd.read_csv(io.StringIO(s.decode('utf-8')))
df = pd.read_csv(io.StringIO(s.decode('utf-8')), na_values=['?'])
df.columns=['Scn', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'CLASS']
df.A7 = pd.to_numeric(df.A7, errors='coerce')

df.to_csv("wisconsinbreast.csv")

m,n=df.shape
#print(m,n)
df = df.replace('?', np.nan)
#print(df)
#print(df.mean()) 
print(df.fillna(df.mean()))



