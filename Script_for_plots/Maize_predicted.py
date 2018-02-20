import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import mpld3

# creating a dataframe from the csv file 
df=pd.read_csv('final.csv')
df = df.rename(columns={'Unnamed: 0':'Year'})
X=np.array(df[['Year','Maize_area']]).reshape(-1,2)

Y=np.array(df['Maize']).reshape(-1,1)

clf=LinearRegression()
clf.fit(X,Y)
w_pre=clf.predict(np.array([[2011,1035899],[2012,1080987],
                            [2013,1067891],[2014,1095999],
                            [2015,1163871],[2016,1065861],
                            [2017,1177992]]).reshape(-1,2))

#creating a plot
years=np.arange(2011,2018).reshape(-1,1)
maize_obj,maize_plt = plt.subplots()
maize_plt.plot(df['Year'],df['Maize'],label="Old Stats")
maize_plt.plot(years,w_pre,label="Predicted Stats")
maize_plt.set_xlabel('Years')
maize_plt.set_ylabel('Maize')
maize_plt.set_title('Maize_Yield')
maize_plt.legend()
plt.ticklabel_format(useOffset=False, style='plain',axis='both')
# plt.show()
#writing it to the file
x = mpld3.fig_to_html(maize_obj)
file1 = open('Maize.txt','w+')
file1.write(x)
file1.close()
