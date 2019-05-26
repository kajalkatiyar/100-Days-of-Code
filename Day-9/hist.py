import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
pl=df["total_profit"].tolist()
range=[150000,175000,200000,225000,250000,300000,350000]
plt.hist(pl,range)
plt.xlabel("profit range in dollars")
plt.ylabel("Actual profit in dollars")
plt.xticks(range)
plt.show()