import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "item_names": ["Umbrella", "Raincoat", "Slippers", "Sweater", "T-Shirt", "Boots", "Jeans", "Gloves", "Sweatshirts", "Hats"],
    "sales": [239, 284, 924, 622, 942, 298, 773, 143, 645, 234],
    "season": ["monsoon", "monsoon", "summer", "winter", "summer", "monsoon", "summer", "winter", "winter", "summer"],
    "item_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "size": ["M", "L", "M", "L", "M", "L", "M", "L", "M", "L"],
    "category": ["accessory", "clothing", "footwear", "clothing", "clothing", "footwear", "clothing", "accessory", "clothing", "accessory"],
    "gender": ["unisex", "unisex", "unisex", "unisex", "unisex", "unisex", "unisex", "unisex", "unisex", "unisex"]
}

df = pd.DataFrame(data)

summer_sales = df[df["season"] == "summer"]
sales_data = summer_sales.groupby("item_names")["sales"].sum().reset_index()

plt.figure(figsize=(13, 5))
sns.barplot(x="item_names", y="sales", data=sales_data, palette="viridis")
plt.title("Highest Sales of Items in Summer Season (Bar Graph)")
plt.xlabel("Items")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 10))
plt.pie(sales_data["sales"], labels=sales_data["item_names"], autopct="%1.2f%%", startangle=140, colors=sns.color_palette("viridis", len(sales_data)))
plt.title("Highest Sales of Items in Summer Season (Pie Chart)")
plt.tight_layout()
plt.show()

sns.pairplot(price_data, hue="item_names")
plt.title("price data distribution(triangle plot)")
plt.show()
