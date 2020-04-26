# %%
import pandas as pd 
from matplotlib import pyplot as plt 

covid = 'covid-19.csv'

df = pd.read_csv(covid)
pk = df[df.Country == "Pakistan"] #blue line
china = df[df.Country == "China"] #orange line

plt.plot(pk.Date, pk.Confirmed)
plt.plot(china.Date, china.Confirmed)
plt.xticks(['2020-01-22','2020-02-22','2020-03-22','2020-04-28'], ['January', 'February', 'March', 'April'], rotation=20)
plt.xlabel('Timeline')
plt.ylabel('Number of Confirmed Cases')
plt.legend(['Pakistan', 'China'])
plt.show()
# %%
