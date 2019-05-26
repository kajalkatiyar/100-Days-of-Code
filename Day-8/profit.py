# Read Total profit of all months and show it using a line plot
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
pl=df['total_profit'].tolist()
ml=df['month_number'].tolist()
plt.plot(ml,pl,label='Month-wise profit data of last year ')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.xticks(ml)
plt.show()