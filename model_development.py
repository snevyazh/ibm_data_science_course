import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression

path='http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'

# request.urlretrieve(path, "/Users/imac/Downloads/auto.csv")

df = pd.read_csv(path)
print(df.head())


lm = LinearRegression()
print(lm)

X = df[['highway-mpg']]
Y = df['price']

