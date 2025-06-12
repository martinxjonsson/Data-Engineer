import pandas as pd

df = pd.read_csv("assessment.csv")
df = df.dropna(subset=['Material', 'Price'])


# Alphabetical order
selected_data = df[["Category", "Material"]]
selected_data = selected_data.sort_values(by=['Category', 'Material'], ascending=True)

# Average Price
avg_price_df = df.groupby(['Category', 'Material'])['Price'].mean().reset_index() 
avg_price_df.rename(columns={'Price': 'AveragePrice'}, inplace=True)
avg_price_df = avg_price_df.round(decimals=2)

# Execution
print(selected_data)
print(avg_price_df)
