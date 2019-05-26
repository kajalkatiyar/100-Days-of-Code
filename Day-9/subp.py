#Read Bathing soap facewash of all months and display it using the Subplot
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
mn=df["month_number"].tolist()
bs=df["bathingsoap"].tolist()
fw=df["facewash"].tolist()

f,arr=plt.subplots(2,sharex=True)
arr[0].plot(mn,bs,label='bathing soap sales data',color='k',marker='o')
arr[0].set_title('Sales data of bathing soap')
arr[1].plot(mn,fw,label='face wash sales data',color='r',marker='o')
arr[1].set_title('Sales data of facewash')
plt.xticks(mn)
plt.xlabel('Month Number')
plt.ylabel('Sales unit in number')
plt.show()