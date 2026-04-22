# 0: Tersedia, 1: Booked, 2: Maintenance
list_kursi = [
    [0, 0, 0, 2, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def tampilkan_denah(data):
    print("=== DENAH KURSI SAAT INI ===")
    print("Kolom: 1 2 3 4 5")
    print("----------------------")
    a = 0
    while a <= 2:
        b = 0
        print(f"Baris {a+1}:", end=" ")
        while b <= 4:
            # [.] = Tersedia, [X] = Booked, [M] = Maintenance
            simbol = "[.]" if data[a][b] == 0 else "[X]" if data[a][b] == 1 else "[M]"
            print(simbol, end=" ")
            b += 1
        print() # Pindah baris
        a += 1

# MENU UTAMA
while True:
    tampilkan_denah(list_kursi)
    print("\nMenu:")
    print("1. Booking Kursi")
    print("2. Keluar")
    
    pilihan = input("\nPilih menu (1/2): ")
    
    if pilihan == "1":
        r = int(input("Pilih Baris (1-3): ")) - 1
        c = int(input("Pilih Kolom (1-5): ")) - 1
        
        if 0 <= r <= 2 and 0 <= c <= 4:
            if list_kursi[r][c] == 0:
                list_kursi[r][c] = 1
                print("Kursi telah dipesan!")
            elif list_kursi[r][c] == 1:
                print("Kursi sudah dipesan orang lain.")
            else:
                print("Kursi sedang dalam perbaikan.")
        else:
            print("Posisi kursi tidak valid.")
            
    elif pilihan == "2":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
