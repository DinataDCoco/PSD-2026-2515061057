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
