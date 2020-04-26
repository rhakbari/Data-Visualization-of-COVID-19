# %%
#Data visualization of COVID-19 in Pakistan
#Made by rhakbari 

import pandas as pd 
from matplotlib import pyplot as plt 

covid = 'covid19-pk.csv'

df = pd.read_csv(covid)
Sindh = df[df.Sindh == "Sindh"] #Blue line
Punjab = df[df.Punjab == "Punjab"]#Orange line
Bal = df[df.Balochistan == "Balochistan"] #Green line
AJK = df[df.AJK == "AJK"] #Red line
KPK = df[df.KPK == "KPK"] #purple line
ICT = df[df.ICT == "ICT"] #brown line
GB = df[df.GB == "GB"] #pink line 
plt.plot(df.Date,df.Sindh)
plt.plot(df.Date,df.Punjab)
plt.plot(df.Date,df.Balochistan)
plt.plot(df.Date,df.AJK)
plt.plot(df.Date,df.KPK)
plt.plot(df.Date,df.ICT)
plt.plot(df.Date,df.GB)
plt.xticks(['Mar 31, 2020','Apr 5, 2020', 'Apr 10, 2020' ,'Apr 15, 2020','Apr 20, 2020', 'Apr 26, 2020'], ['Mar 31, 2020','Apr 5, 2020', 'Apr 10, 2020' ,'Apr 15, 2020','Apr 20, 2020', 'Apr 26, 2020'], rotation='vertical')
plt.xlabel('Timeline')
plt.ylabel('Number of Confirmed Cases')
plt.legend(['Sindh', 'Punjab', 'Balochistan','AJK','KPK', 'ICT', 'GB'])
plt.show()
# %%
