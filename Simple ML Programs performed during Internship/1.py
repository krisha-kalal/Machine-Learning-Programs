import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {'item_name':['umbrella','raincoat','boots','sweater','gloves'],
        'sales':[150,200,250,100,50],
        'season':['monsoon','monsoon','monsoon','winter','winter']}

df = pd.DataFrame(data)
monsoon_sales = df[df['season']=='monsoon']
sales_data = monsoon_sales.groupby('item_name')['sales'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x='item_name',y='sales',data=sales_data)
plt.title('highest selling item in monsoon(bar graph)')
plt.xlabel('item name')
plt.ylabel('sales')
plt.show()

plt.figure(figsize=(8,8))
plt.pie(sales_data['sales'],labels=sales_data['item_name'],autopct='%1.1f%%',startangle=140)
plt.title('highest selling item in monsoon(pie chart)')
plt.show()

sns.pairplot(sales_data, hue='item_name')
plt.title('sales data distribution(triangle plot)')
plt.show()