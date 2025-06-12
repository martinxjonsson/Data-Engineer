import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

# Remove whitespaces
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(r'[^\w]', '_', regex=True)
df.loc[df['Age'] < 18, 'Sex'] = 'child'

# Create a new DataFrame
df_relatives = df.loc[(df['Siblings_Spouses_Aboard'] > 0) | (df['Parents_Children_Aboard'] > 0), ['Pclass', 'Name', 'Age', 'Fare']].copy()
average_fare_relatives = df_relatives['Fare'].mean()
print(f"Average fare paid by people with relatives: {average_fare_relatives}")
print("DataFrame with people who had relatives:")
print(df_relatives)

# Execution 1
print("Titanic CSV:")
print(df)

# Groups
avg_fare_per_sex = df.groupby('Sex')[['Fare']].mean().reset_index()
avg_fare_sex_pclass = df.groupby(['Sex', 'Pclass'])[['Fare']].mean().reset_index()
avg_fare_per_survived = df.groupby('Survived')[['Fare']].mean().reset_index()

# Execution 2
print("Titanic Avg:")
print(avg_fare_per_sex)
print(avg_fare_per_survived)
print(avg_fare_sex_pclass)

# Groups 2
male_df = df[df['Sex'] == 'male']
female_df = df[df['Sex'] == 'female']
child_df = df[df['Sex'] == 'child']

# Execution 3
print("Genders:")
print(male_df)
print(female_df)
print(child_df)
