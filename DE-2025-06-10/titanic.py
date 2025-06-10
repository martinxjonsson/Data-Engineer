import pandas as pd

df = pd.read_csv('titanic.csv')

# Remove whitespaces
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(r'[^\w]', '_', regex=True)

df.loc[df["Age"] < 18, "sex"] = "child"

print("DataFrame Info:")
print(df)