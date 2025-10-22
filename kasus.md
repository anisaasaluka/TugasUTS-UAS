# WearEase Clothing - Optimalisasi Produksi Outfit

## Studi Kasus
**WearEase Clothing** adalah usaha konveksi kecil yang memproduksi dua jenis produk utama:
1. **Hoodie**
2. **T-shirt**

Perusahaan menghadapi keterbatasan sumber daya harian seperti bahan kain, tenaga kerja, dan waktu penggunaan mesin.  
Tujuannya adalah menentukan kombinasi jumlah produksi Hoodie dan T-shirt yang menghasilkan **laba maksimum**, tanpa melampaui batas sumber daya yang tersedia.

### Data Produksi
| Sumber Daya | Hoodie (x₁) | T-shirt (x₂) | Ketersediaan |
|--------------|-------------|--------------|---------------|
| Kain (meter) | 3.0 | 1.5 | 300 |
| Tenaga kerja (jam) | 2.0 | 1.0 | 160 |
| Jam mesin (jam) | 1.5 | 0.5 | 100 |
| **Laba per unit (Rp)** | **80.000** | **50.000** | — |

---

## Formulasi Model

### Variabel Keputusan
- x₁ = jumlah unit Hoodie yang diproduksi per hari  
- x₂ = jumlah unit T-shirt yang diproduksi per hari  


### Fungsi Tujuan
Maksimalkan total laba harian:

Max Z = 80.000x₁ + 50.000x₂


### Kendala

3x₁ + 1.5x₂ ≤ 300      (batas penggunaan kain) 2x₁ + 1x₂ ≤ 160        (batas waktu tenaga kerja) 1.5x₁ + 0.5x₂ ≤ 100    (batas jam mesin) 0 ≤ x₁ ≤ 80            (batas permintaan Hoodie) 0 ≤ x₂ ≤ 150           (batas permintaan T-shirt)

#### Penjelasan Kendala:
1. **Kain:** Setiap Hoodie butuh 3 m kain dan T-shirt butuh 1,5 m. Total kain yang tersedia maksimal 300 m/hari.  
2. **Tenaga kerja:** Proses pembuatan Hoodie butuh 2 jam kerja, sedangkan T-shirt 1 jam. Total waktu kerja tersedia 160 jam/hari.  
3. **Jam mesin:** Mesin digunakan 1,5 jam per Hoodie dan 0,5 jam per T-shirt, dengan total waktu maksimal 100 jam/hari.  
4. **Permintaan:** Produksi harian tidak boleh melebihi permintaan pasar — maksimal 80 Hoodie dan 150 T-shirt per hari.

---
Model ini akan diselesaikan menggunakan **metode Linear Programming (Simplex)**  
