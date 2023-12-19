# Memuat library yang diperlukan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Memuat data bike sharing day_df dan hour_df
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

# Membuat sidebar dengan judul dan deskripsi
st.sidebar.title("Dashboard Analisis Data Bike Sharing")
st.sidebar.write("Eksplor data bike sharing (penyewaan sepeda) tahun 2011 dan 2012 yang datanya diperoleh dari Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto, Portugal.")

# Menampilkan info dataset
st.write("### Sekilas Data Bike Sharing 2011 dan 2012")
st.write("#### Data Bike Sharing Per Hari")
st.write(day_df.head())
st.write("#### Data Bike Sharing Per Jam")
st.write(hour_df.head())

# Menampilkan ringkasan informasi statistik
st.write("### Ringkasan Informasi Statistik")
st.write("#### Informasi Statistik Tabel Data Per Hari")
st.write(day_df.describe())
st.write("Pada data di atas, dapat diperoleh informasi bahwa dataset mulai direkam pada 1 Januari 2011 sampai dengan 31 Desember 2012 (dua tahun). Selama dua tahun, rata-rata nilai season (musim) adalah 2,49 yang berarti rata-rata penyewaan sepeda dilakukan di antara musim panas (yang ditandai dengan angka 2) dan musim gugur (yang ditandai dengan angka 3). Dalam dua tahun, dengan nilai rata-rata 0,5 pada kolom yr (tahun) penyewaan sepeda pada tahun 2011 dan 2012 mempunyai jumlah yang hampir sama. Lalu, pada kolom holiday (hari libur) dan workingday (hari kerja) terdapat nilai rata-rata masing-masing 0,02 dan 0,6 yang berarti terdapat lebih banyak penyewaan sepeda pada hari kerja dibandingkan dengan hari libur. Pada kolom weekday, terdapat nilai rata-rata 2,99 yang mengindikasikan bahwa setiap harinya (selain akhir pekan) jumlah penyewaan sepeda kurang lebih sama. Kemudian, dapat diketahui juga bahwa rata-rata jumlah pengguna per hari adalah sebanyak 4504 pengguna yang terdiri dari 848 pengguna kasual dan 3656 pengguna terdaftar.")
st.write("#### Informasi Statistik Tabel Data Per Jam")
st.write(hour_df.describe())
st.write("Pada tabel hour_df, data direkam dan disimpan per jam. Dapat diketahui juga bahwa rata-rata jumlah pengguna per jam adalah sebanyak 189 pengguna yang terdiri dari 35 pengguna kasual dan 153 pengguna terdaftar.")

# Membuat visualisasi tren penyewaan sepeda pada 2011 dan 2012
st.write("### Visualisasi Tren Penyewaan Sepeda Tahun 2011 dan 2012")

st.write("#### Tren Penyewaan Sepeda Tahun 2011")
bike_sharing_2011 = day_df[day_df['yr'] == 0]
monthly_sharing_2011 = bike_sharing_2011.groupby('mnth')['cnt'].sum()
plt.figure(figsize=(10, 6))
plt.plot(monthly_sharing_2011, marker='o', linestyle='-')
plt.title('Frekuensi Penyewaan Sepeda Tahun 2011')
plt.xlabel('Bulan')
plt.ylabel('Total Jumlah Penyewaan Sepeda')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des'])
plt.grid(True)
st.pyplot(plt)

st.write("#### Tren Penyewaan Sepeda Tahun 2012")
bike_sharing_2012 = day_df[day_df['yr'] == 1]
monthly_sharing_2012 = bike_sharing_2012.groupby('mnth')['cnt'].sum()
plt.figure(figsize=(10, 6))
plt.plot(monthly_sharing_2012, marker='o', linestyle='-')
plt.title('Frekuensi Penyewaan Sepeda Tahun 2012')
plt.xlabel('Bulan')
plt.ylabel('Total Jumlah Penyewaan Sepeda')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des'])
plt.grid(True)
st.pyplot(plt)

st.write("#### Perbandingan Tren Frekuensi Bike Sharing Tahun 2011 dan Tahun 2012")
monthly_sharing = day_df.groupby(['yr', 'mnth'])['cnt'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='mnth', y='cnt', hue='yr', data=monthly_sharing, palette='deep', marker='o')
plt.title('Perbandingan Tren Penyewaan Sepeda (2011 vs. 2012)')
plt.xlabel('Bulan')
plt.ylabel('Total Jumlah Penyewaan Sepeda')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des'])
plt.legend(title='Year', loc='upper left', labels=['2011', '2012'])
st.pyplot(plt)

st.write("##### Kesimpulan Visualisasi 1")
st.write("Setelah menganalisis dataset Bike Sharing, dapat diamati bahwa secara keseluruhan terdapat peningkatan tren penyewaan sepeda yang signifikan di antara tahun 2011 dan 2012. Pada tahun 2011, jumlah penyewaan sepeda tertinggi terjadi pada bulan Mei. Sementara, pada tahun 2012, bulan September adalah bulan dengan jumlah penyewaan sepeda tertinggi.")

# Membuat visualisasi distribusi tipe pengguna yang melakukan sewa sepeda dalam dua tahun
st.write("### Visualisasi Distribusi Tipe Pengguna Bike Sharing Tahun 2011 dan 2012")

st.write("#### Distribusi Tipe Pengguna Bike Sharing Tahun 2011")
monthly_counts_2011 = bike_sharing_2011.groupby('mnth')[['registered', 'casual']].sum().reset_index()
bar_width = 0.4
r1 = np.arange(len(monthly_counts_2011))
r2 = [x + bar_width for x in r1]
plt.figure(figsize=(15, 10))
plt.bar(r1, monthly_counts_2011['registered'], width=bar_width, label='Registered', color='blue', alpha=0.7)
plt.bar(r2, monthly_counts_2011['casual'], width=bar_width, label='Casual', color='orange', alpha=0.7)
plt.xlabel('Bulan', fontsize=14)
plt.ylabel('Jumlah Pengguna', fontsize=14)
plt.title('Distribusi Tipe Pengguna Bike Sharing Tahun 2011', fontsize=18)
plt.xticks([r + bar_width / 2 for r in r1], monthly_counts_2011['mnth'], fontsize=12)
plt.legend()
st.pyplot(plt)

st.write("#### Distribusi Tipe Pengguna Bike Sharing Tahun 2012")
monthly_counts_2012 = bike_sharing_2012.groupby('mnth')[['registered', 'casual']].sum().reset_index()
bar_width = 0.4
r1 = np.arange(len(monthly_counts_2012))
r2 = [x + bar_width for x in r1]
plt.figure(figsize=(15, 10))
plt.bar(r1, monthly_counts_2012['registered'], width=bar_width, label='Registered', color='green', alpha=0.7)
plt.bar(r2, monthly_counts_2012['casual'], width=bar_width, label='Casual', color='red', alpha=0.7)
plt.xlabel('Bulan', fontsize=14)
plt.ylabel('Jumlah Pengguna', fontsize=14)
plt.title('Distribusi Tipe Pengguna Bike Sharing Tahun 2012', fontsize=18)
plt.xticks([r + bar_width / 2 for r in r1], monthly_counts_2011['mnth'], fontsize=12)
plt.legend()
st.pyplot(plt)

st.write("#### Perbandingan Jumlah Tipe Pengguna Terdaftar (Registered) (2011 vs. 2012)")
bar_width = 0.35
r1 = np.arange(len(monthly_counts_2011))
r2 = [x + bar_width for x in r1]
plt.figure(figsize=(15, 10))
plt.bar(r1, monthly_counts_2011['registered'], width=bar_width, label='Registered (2011)', color='blue', alpha=0.7)
plt.bar(r2, monthly_counts_2012['registered'], width=bar_width, label='Registered (2012)', color='green', alpha=0.7)
plt.xlabel('Bulan', fontsize=14)
plt.ylabel('Jumlah Pengguna', fontsize=14)
plt.title('Perbandingan Jumlah Tipe Pengguna Terdaftar (Registered) (2011 vs. 2012)', fontsize=18)
plt.xticks([r + 0.5*bar_width for r in r1], monthly_counts_2011['mnth'], fontsize=12)
plt.legend()
st.pyplot(plt)

st.write("#### Perbandingan Jumlah Tipe Pengguna Kasual (Casual) (2011 vs. 2012)")
bar_width = 0.35
r1 = np.arange(len(monthly_counts_2011))
r2 = [x + bar_width for x in r1]
plt.figure(figsize=(15, 10))
plt.bar(r1, monthly_counts_2011['casual'], width=bar_width, label='Casual (2011)', color='orange', alpha=0.7)
plt.bar(r2, monthly_counts_2012['casual'], width=bar_width, label='Casual (2012)', color='red', alpha=0.7)
plt.xlabel('Bulan', fontsize=14)
plt.ylabel('Jumlah Pengguna', fontsize=14)
plt.title('Perbandingan Jumlah Tipe Pengguna Kasual (Casual) (2011 vs. 2012)', fontsize=18)
plt.xticks([r + 0.5*bar_width for r in r1], monthly_counts_2011['mnth'], fontsize=12)
plt.legend()
st.pyplot(plt)

st.write("##### Kesimpulan Visualisasi 2")
st.write("Dari visualisasi data, dapat terlihat bahwa tipe pengguna bike sharing terbanyak dalam dua tahun adalah pengguna terdaftar (registered). Sehingga, dapat ditarik kesimpulan bahwa pengguna bike sharing terbanyak adalah pengguna yang menggunakan bike sharing bukan hanya sekali waktu.")

# Membuat visualisasi pola penyewaan sepeda berdasarkan hari
st.write("### Visualisasi Pola Penyewaan Sepeda Berdasarkan Hari")
weekday_order = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='weekday', y='cnt', data=day_df, order=range(0, 7), palette='deep', errwidth=0)
plt.xlabel('Hari')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.title('Pola Penyewaan Sepeda Berdasarkan Hari')
ax.set_xticklabels(weekday_order)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
st.pyplot(plt)

st.write("##### Kesimpulan Visualisasi 3")
st.write("Pada grafik batang, dapat terlihat bahwa jumlah penyewaan sepeda terbanyak ada pada hari Sabtu yaitu sebanyak 4690 penyewaan. Namun, secara keseluruhan jumlah penyewaan sepeda dari hari ke hari tidak terdapat perbedaan yang signifikan. Jumlah penyewaan sepeda berkisar antara 4228 hingga 4690 penyewaan per hari.")