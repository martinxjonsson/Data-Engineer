import pandas as pd

# Data 1
data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Anna', 'Björn', 'Martin', 'David', 'Erik'],
    'Age': [28, 22, 35, 28, 40],
}

df1 = pd.DataFrame(data1)

# Data 2
data2 = {
    'ID': [1, 2, 3, 4, 5],
    'Occupation': ['Business Owner', 'Software Engineer', 'Data Scientist', 'Teacher', 'Artist'],
    'Salary': [50000, 50000, 70000, 55000, 45000],
    'Start Date': ['2020-01-15', '2019-03-22', '2018-07-30', '2021-05-10', '2017-11-05'],
}

df2 = pd.DataFrame(data2)
df2['Start Date'] = pd.to_datetime(df2['Start Date'])

# Merging DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)

# Merging ID's
df_merged = pd.merge(df1, df2, on='ID')

unique_salarys = df_merged['Salary'].unique()

print("Combined Data:")
print(df_merged)

#Save this to a CSV
combined_df.to_csv('demo_users1337.csv', index=False)

