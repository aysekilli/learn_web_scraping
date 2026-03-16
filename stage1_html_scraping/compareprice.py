
import pandas as pd

df = pd.read_csv('books.csv')

df['price_float'] = df['price'].str.replace('£', '', regex = False).astype(float)
# Remove the price sign and convert to float.

print("\n------ Cheapest 20 books: ------")
print(df.nsmallest(20, 'price_float')[['name', 'price_float']].to_string(index=False))


print("\n------ Most expensive 20 books: ------")
print(df.nlargest(20, 'price_float')[['name', 'price_float']].to_string(index=False))

print("\n------ ALL STATISTICS: ------")
print(f"Average price: £{df['price_float'].mean():.2f}") # neden 2f mesela 3f değil?
#çünkü 2f bize virgülden sonra 2 basamak gösterir, bu da para birimleri için standarttır. 3f kullanırsak virgülden sonra 3 basamak gösterir ki bu genellikle gereksizdir ve fiyatların okunmasını zorlaştırabilir. miş
print(f"Cheapest book: {df.nsmallest(1, 'price_float')['name'].values[0]} at £{df['price_float'].min():.2f}")
print(f"Most expensive book: {df.nlargest(1, 'price_float')['name'].values[0]} at £{df['price_float'].max():.2f}")
print(f"Total number of books: {len(df):,}") #len() ile toplam kitap sayısını alıyoruz, : , ise binlik ayracı ekler.

print("\n------AVERAGE PRICE FOR STAR RATINGS ------")

star_number = ["One", "Two", "Three", "Four", "Five"]
#df.groupby('stars')['price_float']ü #bu kod bize he star ratiing [One, Two, Three, Four, Five] için price_float verir.
#star_analysis = df.groupby('stars')['price_float'].mean() : her grubun ortalamasını al
#.reindex(star_number) : star_number listesine göre sıralama yap demek ()
#.round(2) : 2 ondalık basamağa yuvarla demek

star_analysis = df.groupby('stars')['price_float'].mean().reindex(star_number).round(2)

print(star_analysis)

#:method chaining
