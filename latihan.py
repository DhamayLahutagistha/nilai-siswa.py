import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
data = pd.read_csv('nilai_siswa.csv')

# Menampilkan informasi dasar tentang data
data.info()
print(data.head())
print(data.describe())

# Statistik dasar
print("Rata-rata:", data['Nilai'].mean())   # ✅ diperbaiki: data.gr → data
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# Filter data berdasarkan mata pelajaran
Matematika = data[data['Matpel'] == 'Matematika']
print(Matematika)

BahasaInggris = data[data['Matpel'] == 'Bahasa Inggris']   # ✅ diperbaiki: BahsaInggris → BahasaInggris
print(BahasaInggris)

BahasaIndonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print(BahasaIndonesia)

Produktif = data[data['Matpel'] == 'Produktif']
print(Produktif)

Fisika = data[data['Matpel'] == 'Fisika']
print(Fisika)

# Nilai maksimum dan minimum tiap mapel
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']))

# Rata-rata nilai per mapel (dalam grafik batang)
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

# Boxplot untuk sebaran nilai per mapel
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()