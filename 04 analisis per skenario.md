# Analisis Per Skenario – WearEase Clothing

Dokumen ini berisi analisis dari empat skenario perubahan kapasitas produksi
yang telah dihitung pada branch `feature/analysis-exploratif`.

---

## Baseline (Data Asli)
- Hoodie: 5 unit  
- T-shirt: 150 unit  
- **Total Profit: Rp 8.500.000**

Baseline dibatasi oleh tenaga kerja (160 jam) dan jam mesin (100 jam).

## penjelasan baseline

Meskipun tabel data awal tidak menyebutkan angka tersebut, nilai ini muncul dari **solusi optimal LP** berdasarkan batas sumber daya.
## ➤ Pemakaian Sumber Daya oleh 150 T-shirt

| Sumber Daya | Tersedia | Dipakai T-shirt (150 unit) | Sisa |
|------------|----------|-----------------------------|------|
| Tenaga kerja | 160 jam | 150 jam | **10 jam** |
| Jam mesin | 100 jam | 75 jam | **25 jam** |
| Kain | 300 m | 225 m | **75 m** |

T-shirt memenuhi **permintaan maksimum (150 unit)** tanpa melanggar batas sumber daya, sehingga model memprioritaskannya.

## ➤ Mengapa Hoodie hanya dapat 5 unit?

Sisa kapasitas setelah produksi T-shirt:

- **Tenaga kerja:** 10 jam  
- **Mesin:** 25 jam  
- **Kain:** 75 meter  

Kebutuhan untuk 1 Hoodie:

- 2 jam tenaga kerja  
- 1.5 jam mesin  
- 3 meter kain  

### Perhitungan kapasitas maksimum Hoodie dari tiap sumber daya:

- Berdasarkan tenaga kerja:  
  10 jam ÷ 2 jam per Hoodie = **5 Hoodie**

- Berdasarkan mesin:  
  25 jam ÷ 1.5 jam per Hoodie ≈ **16 Hoodie**

- Berdasarkan kain:  
  75 meter ÷ 3 meter per Hoodie = **25 Hoodie**

### Sumber daya yang paling membatasi:
➡ **Tenaga kerja**, sehingga hanya **5 Hoodie** yang bisa diproduksi.

---

## Skenario 1 — Tenaga Kerja +5 Orang
**Perubahan:** 160 → 200 jam tenaga kerja  
### *Hasil*
- Produksi Hoodie bertambah.
- Produksi T-shirt tetap pada kapasitas maksimal (150 unit).
- Profit meningkat dibanding baseline.

### *Dampak*
- Bottleneck tenaga kerja di baseline menjadi longgar.  
- Kapasitas produksi meningkat tanpa menambah mesin.  
- Perusahaan dapat memenuhi demand Hoodie lebih baik.  
- Laba naik signifikan karena Hoodie memiliki profit per unit lebih tinggi.

Kendala tenaga kerja menjadi lebih longgar sehingga produksi lebih optimal.

---

## Skenario 2 — Jam Mesin 10 jam → 12 jam per hari
**Perubahan:** 100 → 120 jam mesin  
### *Hasil*
- Produksi Hoodie naik.  
- T-shirt tetap stabil.  
- Profit lebih besar dari baseline.

### *Dampak*
- Kendala mesin tidak lagi membatasi produksi.  
- Hoodie dapat diproduksi lebih banyak karena menggunakan 1.5 jam mesin.  
- Kenaikan produksi Hoodie langsung meningkatkan profit.  
- Peningkatan kapasitas mesin memberikan efek paling besar setelah tenaga kerja.

---

## Skenario 3 — Permintaan Hoodie naik 80 → 100 unit
### *Perubahan*
- Permintaan pasar Hoodie meningkat (batas produksi bertambah).
  
### *Hasil*
- Solusi LP mengizinkan produksi Hoodie lebih banyak (jika sumber daya mendukung).  
- Profit naik karena produksi Hoodie bertambah.

### *Dampak*
- Model tidak lagi dibatasi oleh demand rendah Hoodie.  
- Produksi Hoodie menjadi lebih fleksibel mengikuti kapasitas mesin & tenaga kerja.  
- Memberikan potensi peningkatan profit tanpa menambah biaya operasional.  
- Perusahaan bisa merespon peluang pasar lebih cepat.

---

## Skenario 4 — Profit T-shirt turun 50.000 → 33.000
### *Perubahan*
- Laba per unit T-shirt turun signifikan.
  
### *Hasil*
- Total profit menurun.  
- Model memprioritaskan Hoodie (karena profit per unit lebih tinggi).  
- Rasio produksi berubah: Hoodie naik, T-shirt sedikit berkurang (jika sumber daya ketat).

### *Dampak*
- Perubahan harga jual langsung menurunkan profit harian.  
- Kinerja keuangan menjadi lebih bergantung pada produksi Hoodie.  
- Risiko: jika profit T-shirt menurun di pasar nyata, perusahaan harus adaptasi untuk menjaga margin.

---
