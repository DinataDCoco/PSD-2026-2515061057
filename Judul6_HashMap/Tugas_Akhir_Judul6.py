class InventarisToko:
    def __init__(self):
        self.data_barang = {}

    def tambah_barang(self, id_barang, nama_barang, stok_awal):
        if id_barang in self.data_barang:
            print(f"Barang dengan ID {id_barang} sudah ada!")
        else:
            self.data_barang[id_barang] = {
                "nama": nama_barang,
                "stok": stok_awal
            }
            print(f"{nama_barang} berhasil didaftarkan dengan {stok_awal} pcs.")

    def cari_barang(self, id_barang):
        barang = self.data_barang.get(id_barang)
        if barang:
            print(f"ID: {id_barang} | Nama: {barang['nama']} | Stok: {barang['stok']} pcs")
            return barang
        else:
            print(f"Barang dengan ID {id_barang} tidak ditemukan.")
            return None

    def update_stok(self, id_barang, jumlah_baru):
        if id_barang in self.data_barang:
            stok_lama = self.data_barang[id_barang]["stok"]
            self.data_barang[id_barang]["stok"] = jumlah_baru
            print(f"Stok {self.data_barang[id_barang]['nama']} diubah: {stok_lama} -> {jumlah_baru} pcs.")
        else:
            print(f"Gagal update, ID {id_barang} tidak terdaftar.")

    def hapus_barang(self, id_barang):
        if id_barang in self.data_barang:
            barang_dihapus = self.data_barang.pop(id_barang)
            print(f"{barang_dihapus['nama']} telah dihapus dari sistem.")
        else:
            print(f"Gagal menghapus, ID {id_barang} tidak ditemukan.")

    def tampilkan_semua(self):
        print("=== DAFTAR INVENTARIS TOKO ===")
        if not self.data_barang:
            print("Toko masih kosong melompong.")
        for id_barang, info in self.data_barang.items():
            print(f"- [{id_barang}] {info['nama']} (Stok: {info['stok']})")
        print("==============================\n")

toko_elektronik = InventarisToko()

def main():
    print("\nMenu Inventaris Toko")
    print("\n1.Tambah Barang")
    print("2.Cari Barang")
    print("3.Update Stok")
    print("4.Hapus barang")
    print("5.Tampilkan Semua")
    print("6.Keluar")
    pilih_menu = input("\nPilih menu: ")

    while pilih_menu != "6":
        if pilih_menu == "1":
            input_kode = input("Masukkan kode barang: ")
            input_nama = input("Masukkan nama barang: ")
            input_stok = int(input("Masukkan stok barang: "))
            toko_elektronik.tambah_barang(input_kode, input_nama, input_stok)
            main()
            break
        elif pilih_menu == "2":
            input_kode = input("Masukkan kode barang: ")
            toko_elektronik.cari_barang(input_kode)
            main()
            break
        elif pilih_menu == "3":
            input_kode = input("Masukkan kode barang: ")
            input_stok = input("Masukkan stok barang: ")
            toko_elektronik.update_stok(input_kode,input_stok)
            main()
            break
        elif pilih_menu == "4":
            input_kode = input("Masukkan kode barang: ")
            toko_elektronik.hapus_barang(input_kode)
            main()
            break
        elif pilih_menu == "5":
            toko_elektronik.tampilkan_semua()
            main()
            break
        elif pilih_menu == "6":
            break
        else:
            print("input salah!")
            main()
            break
main()