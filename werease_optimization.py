from pulp import LpMaximize, LpProblem, LpVariable, value

# 🧵 WearEase Clothing - Optimalisasi Produksi Outfit
model = LpProblem("Optimasi_Produksi_WearEase", LpMaximize)

# Variabel Keputusan
x1 = LpVariable("Hoodie", lowBound=0, upBound=80, cat="Continuous")
x2 = LpVariable("Tshirt", lowBound=0, upBound=150, cat="Continuous")

# Fungsi Tujuan
model += 80000 * x1 + 50000 * x2, "Total_Laba"

# Kendala
model += 3 * x1 + 1.5 * x2 <= 300, "Ketersediaan_Kain"
model += 2 * x1 + 1 * x2 <= 160, "Kapasitas_TenagaKerja"
model += 1.5 * x1 + 0.5 * x2 <= 100, "Kapasitas_Mesin"

# Jalankan optimasi
model.solve()

# Hasil
print("=== HASIL OPTIMALISASI PRODUKSI ===")
print(f"Hoodie (x1)   = {x1.varValue:.0f} unit/hari")
print(f"T-shirt (x2)  = {x2.varValue:.0f} unit/hari")
print(f"Laba maksimum = Rp {value(model.objective):,.0f} per hari")

kain_terpakai = 3 * x1.varValue + 1.5 * x2.varValue
tenaga_terpakai = 2 * x1.varValue + 1 * x2.varValue
mesin_terpakai = 1.5 * x1.varValue + 0.5 * x2.varValue

print("\n=== PEMAKAIAN SUMBER DAYA ===")
print(f"Kain terpakai        : {kain_terpakai} / 300 (sisa {300 - kain_terpakai})")
print(f"Tenaga kerja terpakai: {tenaga_terpakai} / 160 (sisa {160 - tenaga_terpakai})")
print(f"Jam mesin terpakai   : {mesin_terpakai} / 100 (sisa {100 - mesin_terpakai})")

print("\n=== INTERPRETASI ===")
if abs(tenaga_terpakai - 160) < 1e-6:
    print("→ Tenaga kerja adalah *binding constraint* (terpakai penuh).")
if abs(mesin_terpakai - 100) < 1e-6:
    print("→ Jam mesin adalah *binding constraint* (terpakai penuh).")
if kain_terpakai < 300:
    print("→ Kain tidak terpakai penuh (bukan pembatas utama).")
