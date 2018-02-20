import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# creating a dataframe from the csv file 
df=pd.read_csv('/home/cyberworm/Desktop/final.csv')

X=np.array(df[['year','Jowar_area']]).reshape(-1,2)

Y=np.array(df['Jowar']).reshape(-1,1)

clf=LinearRegression()
clf.fit(X,Y)
w_pre=clf.predict(np.array([[2011,497589],[2012,698009],
                            [2013,720891],[2014,920511],
                            [2015,840871],[2016,545861],
                            [2017,667992]]).reshape(-1,2))

#creating a plot
jowar_obj,jowar_plt = plt.subplots()
jowar_plt.plot(df['year'],df['Jowar'],label="Old Stats")
jowar_plt.plot(years,w_pre,label="Predicted Stats")
jowar_plt.set_xlabel('Years')
jowar_plt.set_ylabel('Jowar')
jowar_plt.set_title('Jowar Yield')
jowar_plt.legend()
plt.ticklabel_format(useOffset=False, style='plain',axis='both')

#writing it to the file
x = mpld3.fig_to_html(jowar_obj)
file1 = open('/home/cyberworm/Desktop/Script_for_plots/Jowar.txt','w+')
file1.write(x)
file1.close()


#w_pre.reshape(1,-1)
#plt.plot(df['year'],df['Jowar'],label="Old Stats")
#plt.plot(years,w_pre,label="Predicted Stats")
#plt.xlabel('Years')
#plt.ylabel('Jowar')
#plt.title('Jowar Yield')
#plt.legend()
#plt.show()
