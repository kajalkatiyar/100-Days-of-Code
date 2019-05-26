#Read toothpaste sales data of each month and show it using a scatter plot
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
su=df['toothpaste'].tolist()
mn=df['month_number'].tolist()
plt.scatter(mn,su,label='Tooth paste sale data')
plt.legend(loc='upper left')
plt.xlabel('Month Number')
plt.ylabel('Units sold')
plt.xticks(mn)
plt.grid(True,linestyle='--',linewidth=1)
plt.show()