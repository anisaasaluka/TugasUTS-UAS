# WearEase Clothing - Optimalisasi Produksi Outfit

## Data Produksi

| Sumber Daya | Hoodie (x₁) | T-shirt (x₂) | Ketersediaan (per hari) |
|--------------|--------------|--------------|--------------------------|
| Kain (meter) | 3.0 | 1.5 | 300 |
| Tenaga kerja (jam) | 2.0 | 1.0 | 160 |
| Jam mesin (jam) | 1.5 | 0.5 | 100 |
| **Laba per unit (Rp)** | **80.000** | **50.000** | — |


1. **Kain (Bahan Baku)**  
   Setiap Hoodie membutuhkan **3 meter kain**, dan setiap T-shirt membutuhkan **1,5 meter kain**.  
   Total kain yang tersedia adalah **300 meter per hari**, sesuai dengan stok bahan baku untuk produksi harian.
2. **Tenaga Kerja**  
   Pembuatan Hoodie memerlukan **2 jam kerja per unit**, sedangkan T-shirt **1 jam per unit**.  
   WearEase Clothing memiliki sekitar **20 karyawan** dengan jam kerja rata-rata **8 jam per hari**,  
   sehingga total kapasitas tenaga kerja mencapai **160 jam per hari**.
3. **Jam Mesin**  
   Proses jahit dan finishing menggunakan beberapa mesin jahit.  
   Terdapat **10 mesin** yang beroperasi rata-rata **10 jam per hari**,  
   sehingga total kapasitas penggunaan mesin adalah **100 jam per hari**.  
   Setiap Hoodie membutuhkan **1,5 jam mesin**, dan T-shirt **0,5 jam mesin**.
4. **Permintaan Pasar**  
   Berdasarkan estimasi permintaan harian:  
   - Hoodie maksimal **80 unit per hari**  
   - T-shirt maksimal **150 unit per hari**
     
---

### Variabel Keputusan
- **x₁** = jumlah unit Hoodie yang diproduksi per hari  
- **x₂** = jumlah unit T-shirt yang diproduksi per hari
  
---

## Interpretasi Hasil
Dari hasil **Excel Solver**, diperoleh kombinasi optimal sebagai berikut:

| Variabel | Nilai Optimal | Interpretasi |
|-----------|----------------|--------------|
| x₁ (Hoodie) | 40 | Produksi Hoodie sebanyak 40 unit/hari |
| x₂ (T-shirt) | 80 | Produksi T-shirt sebanyak 80 unit/hari |
| **Z (Laba Maksimum)** | **Rp 7.200.000** | Laba maksimum per hari |

> Semua kendala terpenuhi: tenaga (160) dan mesin (100) terpakai penuh → ini menunjukkan kedua sumber daya tersebut merupakan binding constraints (mengikat).
> Kain terpakai 240 dari 300 → masih ada sisa 60 meter kain (slack = 60). Artinya kain bukan bottleneck pada solusi ini.
> WearEase Clothing dapat memperoleh laba maksimum sebesar **Rp 7.200.000 per hari**  
> dengan kombinasi produksi **40 Hoodie dan 80 T-shirt** tanpa melampaui batas sumber daya.

---
