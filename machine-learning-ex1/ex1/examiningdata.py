import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
path = os.getcwd() + '\ex1data1.txt'  
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])  
data.head() #this is to show the few rows
data.describe() #this is for describing data with some numerical computations
data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))  
#computing the cost
def computecost(X,y,theta):
    cost = np.power(((X*theta.T)-y),2)
    return np.sum(cost)/(2*len(X))

data.insert(0, 'ones' ,1)#inserting 1 in the firstcolumn
cols = data.shape[1]#returns the column dimension
X = data.iloc[:,0:cols-1]
y = data.iloc[:,cols-1:cols]

X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))
print(computecost(X,y,theta))


