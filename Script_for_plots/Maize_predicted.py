import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# creating a dataframe from the csv file 
df=pd.read_csv('/home/cyberworm/Desktop/final.csv')

X=np.array(df[['year','Maize_area']]).reshape(-1,2)

Y=np.array(df['Maize']).reshape(-1,1)

clf=LinearRegression()
clf.fit(X,Y)
w_pre=clf.predict(np.array([[2011,995899],[2012,1080987],
                            [2013,1067891],[2014,1095999],
                            [2015,1163871],[2016,1065861],
                            [2017,1177992]]).reshape(-1,2))

#creating a plot
maize_obj,maize_plt = plt.subplots()
maize_plt.plot(df['year'],df['Maize'],label="Old Stats")
maize_plt.plot(years,w_pre,label="Predicted Stats")
maize_plt.set_xlabel('Years')
maize_plt.set_ylabel('Maize')
maize_plt.set_title('Maize_Yield')
maize_plt.legend()
plt.ticklabel_format(useOffset=False, style='plain',axis='both')

#writing it to the file
x = mpld3.fig_to_html(maize_obj)
file1 = open('/home/cyberworm/Desktop/Script_for_plots/Maize.txt','w+')
file1.write(x)
file1.close()
