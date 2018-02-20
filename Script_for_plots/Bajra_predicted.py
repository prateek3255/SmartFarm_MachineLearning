import mpld3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# creating a dataframe from the csv file 
df=pd.read_csv('final.csv')
df = df.rename(columns={'Unnamed: 0':'Year'})

X=np.array(df[['Year','Bajra_area']]).reshape(-1,2)

Y=np.array(df['Bajra']).reshape(-1,1)

clf=LinearRegression()
clf.fit(X,Y)
w_pre=clf.predict(np.array([[2011,5975899],[2012,6280987],
                            [2013,5767891],[2014,6995811],
                            [2015,5863171],[2016,5865861],
                            [2017,5977992]]).reshape(-1,2))

#creating a plot
years=np.arange(2011,2018).reshape(-1,1)
bajra_obj,bajra_plt = plt.subplots()
bajra_plt.plot(df['Year'],df['Bajra'],label="Old Stats")
bajra_plt.plot(years,w_pre,label="Predicted Stats")
bajra_plt.set_xlabel('Years')
bajra_plt.set_ylabel('Bajra')
bajra_plt.set_title('Bajra Yield')
bajra_plt.legend()
plt.ticklabel_format(useOffset=False, style='plain',axis='both')
# plt.show()
#writing it to the file
x = mpld3.fig_to_html(bajra_obj)
file1 = open('Bajra.txt','w+')
file1.write(x)
file1.close()

