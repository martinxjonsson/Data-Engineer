import pandas as pd

e_com = pd.read_csv("ecommerce_sales.csv")

# Remove any NaN
e_com = e_com.dropna()

# Organize 
e_com = e_com.sort_values(by='product_category')
e_com = e_com.sort_values(by='quantity', ascending=False)

total_spend = e_com.groupby(['unit_price', 'quantity'])['Spent'].()

# Specify Categories
selected_data = e_com[['product_category', 'quantity', 'unit_price', 'order_date', 'country']]

print(e_com)
print(selected_data)
print(total_spend)