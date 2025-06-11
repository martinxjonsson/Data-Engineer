import pandas as pd
import numpy as np
import json
import argparse

from faker import Faker

fake = Faker()
Faker.seed(42)
np.random.seed(42)

# 1. User Data
num_users = 100
user_ids = np.arange(1, num_users + 1)
user_data = []

for user_id in user_ids:
    name = fake.name()
    email = fake.email()
    signup_date = fake.date_between(start_date='-2y', end_date='today')
    user_data.append([user_id, name, email, signup_date])

users_df = pd.DataFrame(user_data, columns=['user_id', 'name', 'email', 'signup_date'])


# Products
product_catalogue = [
    ["Laptop", "Electronics", 999.99],
    ["Headphones", "Electronics", 199.99],
    ["Coffee Maker", "Home Appliances", 89.99],
    ["Office Chair", "Furniture", 149.99],
    ["Running Shoes", "Sportswear", 120.00],
    ["Smartphone", "Electronics", 799.99],
    ["Yoga Mat", "Fitness", 29.99],
    ["LED Monitor", "Electronics", 249.99],
    ["Blender", "Home Appliances", 59.99],
    ["Desk Lamp", "Furniture", 39.99]
]

product_data = []
for i, (name, category, price) in enumerate(product_catalogue, start=1):
    product_data.append([i, name, category, price])

products_df = pd.DataFrame(product_data, columns=['product_id', 'product_name', 'category', 'price'])


# Transactions
num_transactions = 500
transaction_data = []

for transaction_id in range(1, num_transactions + 1):
    user_id = np.random.choice(user_ids)
    product_id = np.random.choice(products_df['product_id'])
    quantity = np.random.randint(1, 5)
    transaction_date = fake.date_between(start_date='-1y', end_date='today')
    transaction_data.append([transaction_id, user_id, product_id, quantity, transaction_date])

transactions_df = pd.DataFrame(transaction_data, columns=['transaction_id', 'user_id', 'product_id', 'quantity', 'transaction_date'])

# Merge: users + transactions + products
full_data = pd.merge(transactions_df, users_df, on='user_id', how='left')
full_data = pd.merge(full_data, products_df, on='product_id', how='left')

# Räkna ut total kostnad per transaktion
full_data['total_cost'] = full_data['price'] * full_data['quantity']

# Bästsäljare
product_sales = full_data.groupby(['product_id', 'product_name']) \
                         .agg(total_quantity=('quantity', 'sum'),
                              average_price=('price', 'mean')) \
                         .reset_index()
top_5_products = product_sales.sort_values(by='total_quantity', ascending=False).head(5)

# Bästsäljande kategori
category_sales = full_data.groupby('category') \
                          .agg(total_quantity=('quantity', 'sum')) \
                          .reset_index()
most_popular_category = category_sales.sort_values(by='total_quantity', ascending=False).head(1)


# Gruppera per användare för att se total spending
user_spending = full_data.groupby(['user_id', 'name'])['total_cost'].sum().reset_index()


df = pd.read_json("full_data.json", orient="records")
print(df.tail())