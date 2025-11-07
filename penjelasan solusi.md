# WearEase Clothing - Optimalisasi Produksi Outfit

## Data Produksi

| Sumber Daya | Hoodie (x₁) | T-shirt (x₂) | Ketersediaan (per hari) |
|--------------|--------------|--------------|--------------------------|
| Kain (meter) | 3.0 | 1.5 | 300 |
| Tenaga kerja (jam) | 2.0 | 1.0 | 160 |
| Jam mesin (jam) | 1.5 | 0.5 | 100 |
| **Laba per unit (Rp)** | **80.000** | **50.000** | — |

---
1. **Kain**  
   Setiap Hoodie membutuhkan **3 meter kain**, dan setiap T-shirt membutuhkan **1,5 meter kain**.  
   Total kain yang tersedia adalah **300 meter per hari**, sesuai dengan stok bahan baku untuk produksi harian.

2. **Tenaga Kerja**  
   Pembuatan Hoodie memerlukan **2 jam kerja per unit**, sedangkan T-shirt **1 jam per unit**.  
   WearEase Clothing memiliki sekitar **20 karyawan** dengan jam kerja rata-rata **8 jam per hari**,  
   sehingga total kapasitas tenaga kerja mencapai **160 jam per hari**. (total operator-hours = 20 × 8 = 160).  

3. **Jam Mesin**  
   Proses jahit dan finishing menggunakan beberapa mesin jahit.  
   Terdapat **10 mesin** dengan total kapasitas penggunaan **100 jam per hari** (sesuai data tugas).  
   Angka ini dicapai melalui pengoperasian mesin secara bergantian dengan pengaturan **shift/overlap**,
   - **Grup A (10 operator)** bekerja pukul **08.00 – 16.00**,  
   - **Grup B (10 operator)** bekerja pukul **10.00 – 18.00**.
     
   Total jam operasi mesin = 10 mesin × 10 jam = **100 jam/hari**,  
   Setiap Hoodie membutuhkan **1,5 jam mesin**, dan setiap T-shirt **0,5 jam mesin**.
   
5. **Permintaan Pasar**  
   Berdasarkan estimasi permintaan harian:  
   - Hoodie maksimal **80 unit per hari**  
   - T-shirt maksimal **150 unit per hari**

---

## Interpretasi Hasil (uji pertama)

Dari hasil **Excel Solver**

Jika :
x₁ (Hoodie) : 40
x₂ (T-shirt) : 80

**Perhitungan sumber daya yang digunakan:**
  - Kain: (3 × 40) + (1.5 × 80) = **240 meter**  
  - Tenaga kerja: (2 × 40) + (1 × 80) = **160 jam**  
  - Mesin: (1.5 × 40) + (0.5 × 80) = **100 jam**
    
Semua kendala terpenuhi:  
- **Tenaga kerja (160)** dan **mesin (100)** terpakai penuh → menunjukkan bahwa keduanya merupakan **binding constraints** (mengikat).  
- **Kain** terpakai 240 dari 300 → masih ada sisa 60 meter kain (slack = 60).  
- Artinya, kain bukan faktor pembatas utama (*bottleneck*) pada solusi ini.  

Dengan kombinasi ini, WearEase Clothing dapat memperoleh laba maksimum sebesar **Rp 7.200.000 per hari**  
tanpa melampaui batas sumber daya yang tersedia.

---

## Interpretasi Hasil (uji kedua)

Jika :
x₁ (Hoodie) : 50
x₂ (T-shirt) : 90

**Perhitungan sumber daya yang digunakan:**
  - Kain: (3 × 50) + (1.5 × 90) = **285 meter**  
  - Tenaga kerja: (2 × 50) + (1 × 90) = **190 jam**  
  - Mesin: (1.5 × 50) + (0.5 × 90) = **120 jam**

Walaupun laba meningkat secara matematis, kombinasi ini **tidak feasible**  
karena **melampaui kapasitas tenaga kerja (160 jam)** dan **jam mesin (100 jam)** yang tersedia.

---

### Kesimpulan

Berdasarkan dua skenario pengujian, **Uji Pertama** merupakan kombinasi produksi yang paling efisien dan realistis untuk kondisi sumber daya harian WearEase Clothing. Sementara **Uji Kedua** menunjukkan potensi peningkatan laba, namun hanya bisa diterapkan apabila kapasitas tenaga kerja dan jam operasi mesin ditingkatkan. Oleh karena itu, kombinasi **40 Hoodie dan 80 T-shirt** dipilih sebagai **solusi optimal** dengan laba maksimum **Rp 7.200.000 per hari**.

--

### Catatan
- Feasible : kondisi solusi yang memenuhi semua kendala atau batas sumber daya.
- Binding constraint : kendala yang terpakai penuh dan membatasi hasil optimal.
- Bottleneck : sumber daya paling kritis yang membatasi peningkatan produksi.
- Slack : sisa kapasitas atau ruang kosong dari sumber daya yang belum terpakai.
