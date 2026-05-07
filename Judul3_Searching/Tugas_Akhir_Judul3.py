def cari_nomor_telepon(buku_telepon, nama_target):
    for kontak in buku_telepon:
        if kontak['nama'] == nama_target:
            return kontak['nomor']
    return None

buku_telepon = [
    {"nama": "Andi", "nomor": "0812-3456-7890"},
    {"nama": "Budi", "nomor": "0857-1122-3344"},
    {"nama": "Citra", "nomor": "0821-9988-7766"},
    {"nama": "Dewi", "nomor": "0813-4455-6677"}
]

def tambah_kontak(buku_telepon, nama_baru, nomor_baru):
    untuk_cek = nama_baru
    for kontak in buku_telepon:
        if kontak['nama'] == untuk_cek:
            print(f"Gagal! Nama '{nama_baru}' sudah ada di buku telepon.")
            return False 

    kontak_baru = {
        "nama": nama_baru,
        "nomor": nomor_baru
    }
    buku_telepon.append(kontak_baru)
    print(f"Berhasil! Kontak '{nama_baru}' telah ditambahkan.")
    return True

nama_dicari = input("Masukkan nama yang ingin dicari: ")
hasil = cari_nomor_telepon(buku_telepon, nama_dicari)

if hasil:
    print(f"Nomor telepon {nama_dicari} adalah: {hasil}")
else:
    print(f"Maaf, kontak dengan nama '{nama_dicari}' tidak ditemukan.")

Masukkan_nomor_baru = input("Ingin masukkan nomor baru? (y/n) : ")

if Masukkan_nomor_baru == "y": 
    nama = input("Masukkan nama kontak baru: ")
    nomor = input("Masukkan nomor telepon: ")

    tambah_kontak(buku_telepon, nama, nomor)

    print("\nDaftar Kontak Sekarang:")
    for k in buku_telepon:
        print(f"- {k['nama']}: {k['nomor']}")
elif Masukkan_nomor_baru == "n" :
    print("Selesai.")