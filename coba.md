# 📌 Baseline (Data Asli)

Hasil optimasi model Linear Programming menghasilkan:

- **Hoodie:** 5 unit  
- **T-shirt:** 150 unit  
- **Total Profit:** Rp 8.500.000

---

## 🔍 Kenapa Hasil Baseline = 5 Hoodie dan 150 T-shirt?

Meskipun tabel data awal tidak menyebutkan angka tersebut, nilai ini muncul dari **solusi optimal LP** berdasarkan batas sumber daya.

### ➤ Pemakaian sumber daya oleh 150 T-shirt

| Sumber Daya | Total | Dipakai T-shirt (150 unit) | Sisa |
|------------|--------|-----------------------------|-------|
| Tenaga kerja | 160 jam | 150 jam | **10 jam** |
| Jam mesin | 100 jam | 75 jam | **25 jam** |
| Kain | 300 m | 225 m | **75 m** |

Produksi T-shirt memenuhi **permintaan maksimum 150 unit**, dan masih berada dalam batas seluruh sumber daya, sehingga LP memprioritaskan produksi ini.

---

## ➤ Mengapa Hoodie hanya bisa 5 unit?

Sisa kapasitas setelah produksi T-shirt:

- **10 jam tenaga kerja**
- **25 jam mesin**
- **75 meter kain**

Kebutuhan 1 Hoodie:

- 2 jam tenaga kerja  
- 1.5 jam mesin  
- 3 meter kain  

Sehingga kapasitas maksimum berdasarkan tenaga kerja adalah:

\[
10 \text{ jam} \div 2 \text{ jam/unit} = 5 \text{ Hoodie}
\]

Tenaga kerja menjadi **batas utama** sehingga model hanya dapat menambah **5 Hoodie**.

---

## 🎯 Kesimpulan Baseline

Model memilih kombinasi optimal:

- **150 T-shirt (maksimal demand)**
- **5 Hoodie (sesuai sisa sumber daya)**

Kombinasi ini memberikan **profit terbesar** pada kondisi awal tanpa melanggar batas tenaga kerja, mesin, maupun kain.

---
