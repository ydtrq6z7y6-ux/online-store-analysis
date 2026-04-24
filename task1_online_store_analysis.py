import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# učitaj CSV
df = pd.read_csv("online_store_data.csv")

# 1. Ukupan broj proizvoda
print("Ukupan broj proizvoda:", df.shape[0])


# 2. Najprodavaniji proizvod
najprodavaniji = df.sort_values(by="quantity_sold", ascending=False).head(1)

print("\nNajprodavaniji proizvod:")
print(najprodavaniji[["product_name", "quantity_sold"]])


# 3. Top 5 najprodavanijih mobilnih telefona
smartphones = df[df["category"] == "Smartphones"]

top5 = smartphones.sort_values(by="quantity_sold", ascending=False).head(5)

print("\nTop 5 najprodavanijih mobilnih telefona:")
print(top5[["product_name", "quantity_sold"]])


# 4. Najskuplji i najjeftiniji laptop
laptops = df[df["category"] == "Laptops"]

# makni prazne i loše vrijednosti
laptops = laptops.dropna(subset=["price"])
laptops = laptops[laptops["price"] > 0]

najskuplji = laptops["price"].max()
najjeftiniji = laptops["price"].min()

print("\nNajskuplji laptop:", najskuplji)
print("Najjeftiniji laptop:", najjeftiniji)
print("\nPregled podataka:")
print(df.head())