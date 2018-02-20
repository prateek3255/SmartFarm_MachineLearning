# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# from sklearn import svm

df=pd.read_csv('final.csv')
# df.set_index('Unnamed: 0',inplace=True)
df = df.rename(columns={'Unnamed: 0':'Year'})
print(df)

years=np.arange(2011,2018).reshape(-1,1)

# fig_wheat, wheat=plt.subplots()
# fig_barley, barley=plt.subplots()
# fig_jowar, jowar=plt.subplots()
# fig_maize, maize=plt.subplots()
# fig_bajra, wheat=plt.subplots()


X=np.array(df[['Year','Wheat_area']]).reshape(-1,2)
print(X)
Y=np.array(df['Wheat']).reshape(-1,1)
clf=LinearRegression()
clf.fit(X,Y)
w_pre=clf.predict(np.array([[2011,2975899],[2012,2980987],[2013,3367891],[2014,3265811],[2015,3163871],[2016,3465861],[2017,3577992]]).reshape(-1,2))
w_pre.reshape(1,-1)
# plt.plot(years,w_pre)
# plt.scatter(df.index.values,df['Wheat'])
# years=years.reshape(1,-1)
plt.plot(df['Year'],df['Wheat'])
plt.plot(years,w_pre)
plt.ticklabel_format(useOffset=False, style='plain',axis='both')
plt.show()

