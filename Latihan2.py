modal_awal = 100_000_000  # 100 juta

# Persentase laba per bulan
laba_per_bulan = [0, 0, 1, 1, 5, 5, 5, 3]  # dalam persen

total_keuntungan = 0

print("="*50)
print("PERHITUNGAN KEUNTUNGAN USAHA")
print("="*50)
print(f"Modal Awal: Rp {modal_awal:,}\n")

for bulan in range(1, 9):
    persentase = laba_per_bulan[bulan-1]
    keuntungan = modal_awal * persentase / 100
    total_keuntungan += keuntungan
    
    print(f"Bulan {bulan}: {persentase}% = Rp {keuntungan:,.0f}")

print("="*50)
print(f"Total Keuntungan (8 bulan): Rp {total_keuntungan:,.0f}")
print("="*50)
