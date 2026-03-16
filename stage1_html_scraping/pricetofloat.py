import pandas as pd

df = pd.read_csv('books.csv')

print(df.head(10))
print(df.dtypes) # Check the data types of the columns

df['price_float'] = df['price'].str.replace('£', '', regex = False).astype(float)
# Remove the price sign and convert to float.

print(df[[ 'name','price', 'price_float']].head(10))
print(df.dtypes) # Check the data types again to confirm the change

