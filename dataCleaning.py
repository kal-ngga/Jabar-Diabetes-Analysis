import pandas as pd

df = pd.read_csv('dataset/Dataset TA1.csv')

# 1. iformasi dan kondisi awal data
print(f"Total baris awal: {df.shape[0]}")
print(f"informasi data & kolom:")
print(df.info())
print("-" *40)
print("\njumlah data yang null:")
print(df.isnull().sum())
print()
print("=" *40)

df_clean = df.dropna()
print(f"Total baris setelah cleaning: {df_clean.shape[0]}")
print(f"informasi data & kolom:")
print(df_clean.info())
print()
print("=" *40)

numeric = ['Age', 'Hemoglobin', 'Hematokrit', 'Lekosit', 'Eritrosit', 'Trombosit', 'HbA1c', 'RBG']
print(f"Total baris setelah drop null: {df_clean.shape[0]}")

Q1 = df_clean.groupby('Diagnose')[numeric].transform(lambda x: x.quantile(0.25))
Q3 = df_clean.groupby('Diagnose')[numeric].transform(lambda x: x.quantile(0.75))

IQR = Q3 - Q1
bawah = Q1 - 1.5 * IQR
atas = Q3 + 1.5 * IQR

outlier = (df_clean[numeric] >= bawah) & (df_clean[numeric] <= atas)
baris_clean = outlier.all(axis=1)

df_clean = df_clean[baris_clean]
print(f"Total baris setelah drip outlier: {df_clean.shape[0]}")
df_clean.to_csv("dataset/Dataset_Clean.csv", index=False)