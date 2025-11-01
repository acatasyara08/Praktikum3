saldo = 1000000

while True:
    print("\n=== MESIN ATM ===")
    print(f"Saldo Anda: Rp {saldo:,}")
    print("\n1. Tarik Uang")
    print("2. Keluar")
    
    pilihan = input("\nPilih menu (1/2): ")
    
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah penarikan: Rp "))
        
        if jumlah > saldo:
            print("Saldo tidak mencukupi!")
        elif jumlah <= 0:
            print("Jumlah penarikan tidak valid!")
        else:
            saldo -= jumlah
            print(f"Penarikan berhasil! Rp {jumlah:,}")
            print(f"Sisa saldo: Rp {saldo:,}")
            
            if saldo == 0:
                print("\nSaldo Anda habis. Terima kasih!")
                break
    
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM kami!")
        break
    
    else:
        print("Pilihan tidak valid!")
