import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import mpld3

df=pd.read_csv('/home/cyberworm/Desktop/final.csv')

df = df.rename(columns={'Unnamed: 0':'Year'})

years=np.arange(2011,2018).reshape(-1,1)


X=np.array(df[['year','Wheat_area']]).reshape(-1,2)

Y=np.array(df['Wheat']).reshape(-1,1)
clf=LinearRegression()
clf.fit(X,Y)
w_pre=clf.predict(np.array([[2011,2975899],[2012,2980987],[2013,3367891],
                            [2014,3265811],[2015,3163871],[2016,3465861],
                            [2017,3577992]]).reshape(-1,2))

#creating a plot
w_pre.reshape(1,-1)
wheat_obj,wheat_plt = plt.subplots()
wheat_plt.plot(df['year'],df['Wheat'],label="Old Stats")
wheat_plt.plot(years,w_pre,label="Predicted Stats")
wheat_plt.set_xlabel('Years')
wheat_plt.set_ylabel('Wheat')
wheat_plt.set_title('Wheat Yield')
plt.ticklabel_format(useOffset=False, style='plain',axis='both')
wheat_plt.legend()

#writing it to the file
x = mpld3.fig_to_html(wheat_obj)
file1 = open('/home/cyberworm/Desktop/Script_for_plots/Wheat.txt','w+')
file1.write(x)
file1.close()
