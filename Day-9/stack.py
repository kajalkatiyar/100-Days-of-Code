import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
mn=df["month_number"].tolist()

fc=df["facecream"].tolist()
fw=df["facewash"].tolist()
tp=df["toothpaste"].tolist()
bs=df["bathingsoap"].tolist()
sh=df["shampoo"].tolist()
mo=df["moisturizer"].tolist()

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
plt.stackplot(mn,fc,fw,tp,bs,sh,mo,colors=['m','c','r','k','g','y'],labels=labels)
plt.xlabel('Month number')
plt.ylabel('Sales unit in number')
plt.legend(loc='upper left')
plt.title('Products sales data using stack plot ')
plt.show()