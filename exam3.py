import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression

# define file location and read it into dataframe
file_name='http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df=pd.read_csv(file_name)
print(df.head())

# display columns data types
print(df.dtypes)
df.describe()

#delete coulmns "Unnamed: 0","id"
df.drop(columns=["Unnamed: 0","id"], inplace=True)
print(df.head())

# calculate NaN
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())
# replace NaN with the mean value
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)
mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

#Use the method value_counts to count the number of houses with unique floor values, 
# use the method .to_frame() to convert it to a dataframe

num_houses=df['floors'].value_counts().to_frame()
print(num_houses.head())

#Use the function boxplot in the seaborn library to determine 
#whether houses with a waterfront view or without a waterfront view have more price outliers

sns.boxplot(x='waterfront', y='price', data=df)

#Use the function regplot in the seaborn library to determine if 
# the feature sqft_above is negatively or positively correlated with price.

sns.regplot(x='sqft_above', y='price', data=df)
plt.ylim(0,)

#We can use the Pandas method corr() to find the feature other than price that is most correlated with price.
print(df.corr()['price'].sort_values())

#model development
#We can Fit a linear regression model using the longitude feature 'long' and caculate the R^2.
X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)

#Fit a linear regression model to predict the 'price' using the feature 'sqft_living' 
# then calculate the R^2. Take a screenshot of your code and the value of the R^2.
A = df[['sqft_living']]
B = df[['price']]
lm1 = LinearRegression()
lm1.fit(A, B)
lm1.score(A, B)

#Fit a linear regression model to predict the 'price' using the list of features:
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]     
#Then calculate the R^2
x = df[features]
y = df['price']
lm2=LinearRegression()
lm2.fit(x, y)
lm2.score(x, y)

#Create a list of tuples, the first element in the tuple contains the name of the estimator:
Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(x, y)
pipe.score(x, y)

#Model Evaluation and Refinement
#We will split the data into training and testing sets
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

#Create and fit a Ridge regression object using the training data, 
# set the regularization parameter to 0.1, and calculate the R^2 using the test data.
from sklearn.linear_model import Ridge

RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x_train, y_train)
RidgeModel.score(x_train, y_train)

#Perform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object 
# using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided

pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)

RigeModel1=Ridge(alpha=0.1)
RigeModel1.fit(x_train_pr, y_train)
RigeModel1.score(x_test_pr, y_test)

