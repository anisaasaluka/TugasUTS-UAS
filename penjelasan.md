# WearEase Clothing – Analisis Optimasi Produksi

---

## Data Awal

| Sumber Daya | Hoodie (x₁) | T-shirt (x₂) | Ketersediaan |
|:--|:--:|:--:|:--:|
| Kain (meter) | 3 | 1.5 | 300 |
| Tenaga kerja (jam) | 2 | 1 | 160 |
| Jam mesin (jam) | 1.5 | 0.5 | 100 |

| Produk | Laba per Unit | Permintaan Maksimum |
|:--|:--:|:--:|
| Hoodie | Rp 80.000 | 80 unit |
| T-shirt | Rp 50.000 | 150 unit |

---

## Model Matematika

**Fungsi Tujuan (Maksimasi Laba):**

\[
Max\ Z = 80.000x₁ + 50.000x₂
\]

**Kendala:**

\[
\begin{cases}
3x₁ + 1.5x₂ ≤ 300 & \text{(batas penggunaan kain)}\\
2x₁ + 1x₂ ≤ 160 & \text{(batas waktu tenaga kerja)}\\
1.5x₁ + 0.5x₂ ≤ 100 & \text{(batas jam mesin)}\\
0 ≤ x₁ ≤ 80 & \text{(batas permintaan Hoodie)}\\
0 ≤ x₂ ≤ 150 & \text{(batas permintaan T-shirt)}
\end{cases}
\]

---

## Hasil Solver – Skenario 1 (Solusi Optimal)

| Variabel | Nilai |
|:--|:--:|
| x₁ (Hoodie) | 40 |
| x₂ (T-shirt) | 80 |

| Sumber Daya | Pemakaian | Batas | Status |
|:--|:--:|:--:|:--|
| Kain (meter) | 240 | 300 | ✅ Masih cukup |
| Tenaga kerja (jam) | 160 | 160 | ⚙️ Terpakai penuh |
| Jam mesin (jam) | 100 | 100 | ⚙️ Terpakai penuh |

**Total Laba:** Rp **7.200.000**

**Interpretasi:**  
Solusi ini adalah hasil optimal dari *Excel Solver*. Kapasitas tenaga kerja dan mesin terpakai penuh (*binding constraints*), sedangkan stok kain masih tersisa 60 meter (*non-binding*). Kombinasi **40 Hoodie dan 80 T-shirt** menghasilkan laba maksimum Rp 7,2 juta tanpa melampaui batas sumber daya.

---

## Uji Coba Kombinasi Baru – Skenario 2

| Variabel | Nilai |
|:--|:--:|
| x₁ (Hoodie) | 50 |
| x₂ (T-shirt) | 90 |

| Sumber Daya | Pemakaian | Batas | Status |
|:--|:--:|:--:|:--|
| Kain (meter) | 285 | 300 | ✅ Masih cukup |
| Tenaga kerja (jam) | 190 | 160 | ❌ Melebihi batas |
| Jam mesin (jam) | 120 | 100 | ❌ Melebihi batas |

**Total Laba:** Rp **8.500.000**

**Interpretasi:**  
Jika jumlah produksi dinaikkan menjadi 50 Hoodie dan 90 T-shirt, laba memang naik menjadi Rp 8,5 juta. Namun, pemakaian tenaga kerja dan mesin melebihi kapasitas yang tersedia, sehingga kombinasi ini **tidak feasible** untuk dijalankan tanpa penambahan sumber daya.

---

## Saran

- Produksi optimal: **40 Hoodie** dan **80 T-shirt**  
- Laba maksimum: **Rp 7.200.000**  
- Untuk meningkatkan output, perusahaan perlu menambah tenaga kerja dan jam operasi mesin.  
- Model ini dapat dikembangkan lagi untuk analisis biaya minimum atau simulasi penambahan kapasitas di tahap berikutnya (UAS).
