import pandas as pd
import numpy as np

df = pd.read_csv("ecommerce_sales.csv")

# Add Unknown where Data is missing
df['order_id'] = df['order_id'].fillna(-1)
df['product_id'] = df['product_id'].fillna(-1) 
df['product_category'] = df['product_category'].fillna("Unknown") 
df['quantity'] = df['quantity'].fillna(df['quantity'].mean())
df['unit_price'] = df['unit_price'].fillna(df['unit_price'].mean())
df['customer_id'] = df['customer_id'].fillna(-1)
df['order_date'] = df['order_date'].fillna("1900-01-01")      
df['country'] = df['country'].fillna("Unknown")                 



# Converting dtypes
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['product_id'] = df['product_id'].astype('Int64')
if (df['quantity'] % 1 == 0).all():
    df['quantity'] = df['quantity'].astype('Int64')  # Tillåter NaN
df['customer_id'] = df['customer_id'].astype('Int64')

# Weekdays & Months
df['order_weekday'] = df['order_date'].dt.day_name()
df['order_month'] = df['order_date'].dt.month

# Total sum
df['total_price'] = df['quantity'] * df['unit_price']

# Category
category_summary = df.groupby('product_category').agg(
    total_sales=('total_price', 'sum'),
    average_quantity=('quantity', 'mean')
).reset_index()

# Pivot Table
pivot_sales = pd.pivot_table(
    data=df,
    index='order_month',
    columns='product_category',
    values='total_price',
    aggfunc='sum'        
).fillna(0)

# Normalize unit_price
avg_price = df['unit_price'].mean()
df['unit_price_normalized'] = (df['unit_price'] / avg_price) * 100
df['unit_price_normalized'] = df['unit_price_normalized'].round(1)

print(df)
print(category_summary)
print(pivot_sales)
