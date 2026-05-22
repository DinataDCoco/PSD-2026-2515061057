Tugas Akhir Percobaan 5 : Binary Search Tree

Judul Proyek : Sistem Inventaris Toko

Proyek ini merupakan sistem sederhana yang menerapkan binary search tree untuk melakukan penyimpanan produk ke dalam gudang dimana user bisa melakukan penambahan data, melihat daftar produk, dan mencari produk spesifik di dalam gudang. sistem ini menggunakan id produk sebagai data yang akan disimpan di node BST, id produk ini berfungsi sebagai kunci untuk mengurutkan, menampilkan, serta mencari produk yang ada di dalam gudang.

source code : 

<img width="2140" height="4168" alt="ss5-1" src="https://github.com/user-attachments/assets/6d71b696-6ee8-4edc-a545-b84b62e8a213" />

Penjelasan : 

Baris 1: Membuat class ProdukNode.
Baris 2: Fungsi inisialisasi.
Baris 3 - 6: Menyimpan 4 data yang diterima.
Baris 7 - 8: Membuat node kiri dan kanan.
Baris 10: Membuat class InventarisTokoBST.
Baris 11 - 12: Saat pertama kali dimulai, root diatur sebagai None.
Baris 14: Membuat fungsi tambah_produk yang menerima parameter detail produk untuk dimasukkan ke dalam tree.
Baris 15: membuat variabel baru yang memanggil class ProdukNode.
Baris 16-19: Mengecek kondisi Jika root masih kosong , maka produk baru akan menjadi Root, lalu fungsi dihentikan.
Baris 21: membuat variabel pointer yang posisi awalnya dimulai dari root.
Baris 22: Menagmbil kondisi selama True.
Baris 23-25: Memeriksa kondisi jika id produk yang ditambahkan sama dengan pointer maka proses dibatalkan.
Baris 26: Memeriksa kondisi lain jika id produk yang ditambahkan lebih kecil dari pointer
Baris 27-30: jika node kiri kosong maka id produk di simpan disini, kemudian hentikan loop.
Baris 31: jika node sudah terisi maka pointer turun ke bawah node tersebut.
Baris 32: kondisi lain jika id produk lebih besar.
Baris 33-36: jika node kiri kosong maka id produk di simpan disini, kemudian hentikan loop.
Baris 37: jika node sudah terisi maka pointer turun ke bawah node tersebut.
Baris 39-40: membuat fungsi mencari produk dengan pointer dimulai dari root.
Baris 41: mengambil kondisi selama pointer tidak kosong
Baris 42-43: kondisi jika id produk sama dengan pointer maka kembalian pointer.
Baris 44-45: mengambl kondisi jika id produk lebih kecil dari pointer maka pointer ke child kiri.
baris 46-47: mengambil kondisi jika id produk lebih besar dari pointer maka pointer ke child kanan.
baris 48: kondisi lain jika tidak ada yang memenuhi syarat sebelumnya maka kembalikan none.
baris 50: membuat fungsi untuk menampilkan data produk secara urut.
baris 51: mengambil kondisi jika node tidak kosong.
baris 52: fungsi memanggil dirinya sendiri untuk mencari id terkecil.
baris 53: print data produk 
baris 54: fungsi memeriksa node kanan
baris 56-57: membuat variabel toko yang memanggil fungsi InventarisTokoBST dan membuat variabel pilih sebagai input yang menentukan menu mana yang akan diakses user.
baris 59: mengambil kondisi selama input tidak sama dengan "4".
baris 60-65: menampilkan menu inventaris toko yang berjumlah 4 menu kemudian meminta input dari user untuk memeilih menu.
baris 57-72: mengambil kondisi jika input "1" maka sistem akan meminta input data produk dari user
baris 74: memanggil fungsi tambah_produk untuk menambahkan data yang diinputkan user ke tree.
baris 76-81: mengambil kondisi jika input "2" maka sistem akan mengecek terlebih dahulu jika root kosong maka akan menampilkan pesan gagal, namun jika ada maka akan memanggil fungsi tampilkan_stok_urut
Baris 83-84: mengambil kondisi jika input "3" kemudian menampilkan keterangan menu pencarian produk
baris 85-86: mengambil kondisi jika root kosong maka tampilkan pesan gagal
baris 87-89: mengambil kondisi jika root terisi maka siste makan meminta input id yang ingin dicari kemudian memanggil fungsi cari_produk.
baris 90-94: jika barang ditemukan maka akan menampilkan data barang tersebut
baris 95-96: mengambil kondisi jika produk tidak ada maka menampilkan pesan produk tidak ditemukan
baris 98-99: mengambil kondisi jiak pilihan "4" maka tampilkan pesan aplikasi ditutup
baris 101-102: mengambil kondisi lain jika input selain itu maka menampilkan pesan menu tidak tersedia.

Output: 

<img width="488" height="572" alt="output5 1" src="https://github.com/user-attachments/assets/8c312903-8243-4e25-b585-1685ab3197a6" />
<img width="288" height="229" alt="output5 2" src="https://github.com/user-attachments/assets/f5d75146-2ce0-4c4a-8e35-6163677c3363" />

Youtube:

