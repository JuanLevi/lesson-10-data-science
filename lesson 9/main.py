import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go   
from plotly.subplots import make_subplots



data = pd.read_csv("covid_data.csv")

print(data.info())
print(data.describe())


data["Province_State"].fillna(value='',inplace=True)
print(data.info())




tendata=pd.DataFrame(data.groupby("Country_Region")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
print(tendata.info())

x=tendata.index
print(x)


#y=tendata["Confirmed"]
'''
plt.bar(x,y,color="b")
plt.xlabel("Countries")
plt.ylabel("Cases")
plt.show()
'''


#make plot nicer

figure1=px.scatter(tendata,x,y="Confirmed",size="Confirmed",size_max=120,color=tendata.index,title="Top 10 Countries by Confirmed Cases")
figure1.write_html('niceplot.html',auto_open=True)




#top 10 countries with most deaths

tenxdata=pd.DataFrame(data.groupby("Country_Region")["Deaths"].sum().nlargest(10).sort_values(ascending=False))

x=tenxdata.index

#figure2=px.scatter(tenxdata,x,y="Deaths",size="Deaths",size_max=100,color=tenxdata.index,title="Top 10 Countries by Most Deaths")



figure2=px.bar(tenxdata,x,y="Deaths",height=600,color="Deaths",orientation='v',color_continuous_scale=['deepskyblue','red'],title="Top 10 Countries by Most Deaths")

figure2.write_html('plotdeaths.html',auto_open=True)





