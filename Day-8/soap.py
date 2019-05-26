import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
mn=df["month_number"].tolist()
fc=df["bathingsoap"].tolist()
plt.bar(mn,fc)
plt.xlabel("Month Number")
plt.xticks(mn)
plt.ylabel("Sold units")
plt.grid(True,linestyle='--',linewidth=1)
plt.show()