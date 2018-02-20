# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import mpld3

# creating a dataframe from the csv file 
df=pd.read_csv('final.csv')
df = df.rename(columns={'Unnamed: 0':'Year'})
X=np.array(df[['Year','Barley_area']]).reshape(-1,2)
Y=np.array(df['Barley']).reshape(-1,1)


clf=LinearRegression()
clf.fit(X,Y)
w_pre=clf.predict(np.array([[2011,397589],[2012,180987],[2013,236891],
                            [2014,126811],[2015,363871],[2016,265861],
                            [2017,277992]]).reshape(-1,2))

w_pre.reshape(1,-1)

#creating a plot

years=np.arange(2011,2018).reshape(-1,1)
barley_obj,barley_plt = plt.subplots()
barley_plt.plot(df['Year'],df['Barley'],label="Old Stats")
barley_plt.plot(years,w_pre,label="predicted stats")
barley_plt.set_xlabel('Years')
barley_plt.set_ylabel('Barley')
barley_plt.set_title('Barley Yield')
barley_plt.legend()
plt.ticklabel_format(useOffset=False, style='plain',axis='both')
# plt.show()
#writing it to the file
x = mpld3.fig_to_html(barley_obj)
file1 = open('Barley.txt','w+')
file1.write(x)
file1.close()
