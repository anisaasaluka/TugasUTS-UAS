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

3x₁ + 1.5x₂ ≤ 300      (batas kain) 2x₁ + 1x₂ ≤ 160        (batas tenaga kerja) 1.5x₁ + 0.5x₂ ≤ 100    (batas jam mesin) 0 ≤ x₁ ≤ 80 0 ≤ x₂ ≤ 150

Model akan diselesaikan menggunakan **metode Linear Programming (Simplex)**
