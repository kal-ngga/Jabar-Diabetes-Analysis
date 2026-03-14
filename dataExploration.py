import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv('dataset/Dataset_Clean.csv')

# 2. Pengukuran statistik berdasarkan tipe data
categorical = ['Gender', 'Diagnose']
numeric = ['Age', 'Hemoglobin', 'Hematokrit', 'Lekosit', 'Eritrosit', 'Trombosit', 'HbA1c', 'RBG']

print("\n--- FREKUENSI KATEGORIKAL ---")
print(df[categorical].apply(pd.Series.value_counts).fillna(0))

print("--- STATISTIK NUMERIK ---")
print(f"\nJumlah Data (not null) - COUNT:\n {df[numeric].count()}")
print(f"\nRata-rata - MEAN\n {df[numeric].mean()}")
print(f"\nStandar Deviasi - STD DEV:\n {df[numeric].std()}")
print(f"\nNilai Terendah - MIN:\n {df[numeric].min()}")
print(f"\nNilai Tengah - MEDIAN:\n {df[numeric].median()}")
print(f"\nNilai Tertinggi - MAX:\n {df[numeric].max()}")
print("=" *40)

# 3. visualisasi keseluruhan data
# A. Visualisasi Numerik
df[numeric].hist(figsize=(15, 10), bins=20, edgecolor='black', grid=False)
plt.suptitle("Histogram Variabel Numerik", fontsize=16)
plt.tight_layout()
plt.savefig('visualitation/Histogram_Numerik.png')

# B. Visualisasi Kategorikal
df[categorical].apply(pd.Series.value_counts).T.plot(kind='bar', figsize=(10, 5), cmap='coolwarm')
plt.title("Bar Chart: Gender dan Diagnose")
plt.xticks(rotation=0)
plt.savefig('visualitation/BarChart_Kategori.png')

# 4. visualisasi data diagnosis
df_melt = df.melt(id_vars='Diagnose', value_vars=numeric)
sns.catplot(
    data=df_melt, x='Diagnose', y='value',
    col='variable', col_wrap=4,
    kind='box', sharey=False, height=4, aspect=1.2
)
plt.suptitle("Boxplot Numerik Berdasarkan Diagnosis", y=1.02, fontsize=16)
plt.savefig('visualitation/Boxplot_Diagnosis.png')

print("\n--- RATA-RATA BERDASARKAN DIAGNOSE ---")
print(df.groupby('Diagnose')[numeric].mean().T)

# 4. pengujian korelasui Pearson
print("\n--- KORELASI PEARSON ---")
corr_matrix = df[numeric].corr(method='pearson')
print(corr_matrix)

# heatmap korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Pearson Correlation Heatmap")
plt.tight_layout()
plt.savefig('visualitation/Heatmap_Korelasi.png')

# 6. menghitung dan mendeteksi outlier
print("\n--- DETEKSI OUTLIER (Jumlah Outlier per Variabel) ---")
# Menghitung Q1 dan Q3
Q1 = df.groupby('Diagnose')[numeric].transform(lambda x: x.quantile(0.25))
Q3 = df.groupby('Diagnose')[numeric].transform(lambda x: x.quantile(0.75))

# Rumus IQR & Batas
IQR = Q3 - Q1
bawah = Q1 - 1.5 * IQR
atas = Q3 + 1.5 * IQR

outlier = (df[numeric] < bawah) | (df[numeric] > atas)
outlier_counts = outlier.groupby(df['Diagnose']).sum()
print(outlier_counts)