#Get Total profit of all months and show line plot with the following Style properties
# Generated line plot must include following Style properties: –
# Line Style dotted and Line color should be red
# Show legend at the lower right location.
# X label name = Month Number
# Y label name = Sold units number
# Add a circle marker.
# Line marker color as read
# Line width should be 3

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
pl=df['total_profit'].tolist()
ml=df['month_number'].tolist()
plt.plot(ml,pl,label='Profit data',color='r',marker='o',markerfacecolor='k',linestyle='--',linewidth=3)
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.legend(loc='lower right')
plt.show()
