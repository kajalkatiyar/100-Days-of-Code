import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\kajal\Desktop\company_sales_data.csv")
mn=df["month_number"].tolist()
labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
data=[df['facecream'].sum(),df['facewash'].sum(),df['toothpaste'].sum(),df['bathingsoap'].sum(),df['shampoo'].sum(),df['moisturizer'].sum()]
plt.pie(data,labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.show()
#autopct = % on pie chart