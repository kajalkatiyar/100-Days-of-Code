import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
mn=df["month_number"].tolist()
fc=df["facecream"].tolist()
fw=df["facewash"].tolist()
#plt.bar(mn,fc,label='face cream')
#plt.bar(mn,fw,label='face wash')
plt.bar([a-0.25 for a in mn],fc,width=0.25,label='face cream',align='edge')
plt.bar([a-0.25 for a in mn],fw,width=-0.25,label='face wash',align='edge')
plt.legend(loc='upper left')
plt.xlabel("Month Number")
plt.xticks(mn)
plt.ylabel("Sold units")
plt.grid(True,linestyle='--',linewidth=1)
plt.show()