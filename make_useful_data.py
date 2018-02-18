import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

df=pd.read_csv("apy.csv");
df=df[['District_Name','Crop_Year','Crop','Production','Area']][164440:176954]
# all_crops=set()
# for crop in df['Crop']:
#     all_crops.add(crop)
Req_crops=['Bajra','Barley','Jowar','Maize','Wheat']
i=0
drop_indexes=[]
for crop in df['Crop']:
    if crop not in Req_crops:
        drop_indexes.append(i)
    i+=1
df.drop(df.index[drop_indexes], inplace=True)
df=df.reset_index()
df.drop('index',1,inplace=True)
df.fillna(0,inplace=True)
print(df)
index=np.arange(1997,2011)
Req_crops=Req_crops+['Bajra_area','Barley_area','Jowar_area','Maize_area','Wheat_area']
crops_df=pd.DataFrame(index=index,columns=Req_crops)
crops_df.fillna(0,inplace=True)
# crops_df['Bajra'][1997]=1
# print(crops_df.loc[[1997]])
i=0

for i in range(0,2199):
    a = int(df.iloc[[i]]['Crop_Year'])
    b = df.iloc[[i]]['Crop']
    c= b + '_area'
    crops_df.set_value(a, b, float(crops_df.loc[a, b]) + df.iloc[i]['Production'])
    crops_df.set_value(a, c, float(crops_df.loc[a, c]) + df.iloc[i]['Area'])

print(crops_df)
# crops_df.to_csv('final.csv')
# plt.plot(crops_df['Bajra'])
# plt.show()

