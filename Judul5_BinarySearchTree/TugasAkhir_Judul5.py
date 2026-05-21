class ProdukNode:
    def __init__(self, id_produk, nama, stok, harga):
        self.id_produk = id_produk
        self.nama = nama
        self.stok = stok
        self.harga = harga
        self.kiri = None
        self.kanan = None

class InventarisTokoBST:
    def __init__(self):
        self.root = None

    def tambah_produk(self, id_produk, nama, stok, harga):
        baru = ProdukNode(id_produk, nama, stok, harga)
        if self.root is None:
            self.root = baru
            print(f"Sukses: '{nama}' berhasil didaftarkan sebagai produk utama (Root).")
            return

        pointer = self.root
        while True:
            if id_produk == pointer.id_produk:
                print(f"Gagal: ID {id_produk} sudah terdaftar di sistem!")
                return
            elif id_produk < pointer.id_produk:
                if pointer.kiri is None:
                    pointer.kiri = baru
                    print(f"Sukses: '{nama}' ditambahkan di cabang kiri dari ID {pointer.id_produk}.")
                    break
                pointer = pointer.kiri
            else:
                if pointer.kanan is None:
                    pointer.kanan = baru
                    print(f"Sukses: '{nama}' ditambahkan di cabang kanan dari ID {pointer.id_produk}.")
                    break
                pointer = pointer.kanan

    def cari_produk(self, id_produk):
        pointer = self.root
        while pointer is not None:
            if id_produk == pointer.id_produk:
                return pointer
            elif id_produk < pointer.id_produk:
                pointer = pointer.kiri
            else:
                pointer = pointer.kanan
        return None

    def tampilkan_stok_urut(self, node):
        if node is not None:
            self.tampilkan_stok_urut(node.kiri)
            print(f"ID: {node.id_produk:<4} | Nama: {node.nama:<15} | Stok: {node.stok:<5} | Harga: Rp{node.harga:,}")
            self.tampilkan_stok_urut(node.kanan)

toko = InventarisTokoBST()
pilih = ""

while pilih != "4":
    print(f"\n======== MENU INVENTARIS TOKO ========")
    print("1. Masukkan Produk Baru")
    print("2. Lihat Semua Stok (Urut ID)")
    print("3. Cari Produk")
    print("4. Keluar Aplikasi")
    pilih = input("Pilih menu (1-4): ")
    
    if pilih == "1":
        print("\n--- Input Data Produk ---")
        idProduk = int(input("Masukkan ID produk   : "))
        namaProduk = input("Masukkan nama produk : ")
        stokProduk = int(input("Masukkan stok produk : "))
        hargaProduk = int(input("Masukkan harga produk: "))

        toko.tambah_produk(idProduk, namaProduk, stokProduk, hargaProduk)

    elif pilih == "2":
        print("\n--- DAFTAR INVENTARIS BARANG (URUT ID) ---")
        if toko.root is None:
            print("Gagal: Toko masih kosong, belum ada produk.")
        else:
            toko.tampilkan_stok_urut(toko.root)

    elif pilih == "3":
        print("\n--- Pencarian Produk ---")
        if toko.root is None:
            print("Gagal: Toko masih kosong.")
        else:
            cari_id = int(input("Masukkan ID produk yang dicari: "))
            hasil = toko.cari_produk(cari_id)
            if hasil:
                print(f"\n[ PRODUK DITEMUKAN ]")
                print(f"Nama Barang : {hasil.nama}")
                print(f"Sisa Stok   : {hasil.stok} unit")
                print(f"Harga       : Rp{hasil.harga:,}")
            else:
                print(f"Maaf, produk dengan ID {cari_id} tidak ditemukan.")

    elif pilih == "4":
        print("\nAplikasi ditutup. Terima kasih!")

    else:
        print("Pilihan menu tidak valid. Silakan coba lagi.")