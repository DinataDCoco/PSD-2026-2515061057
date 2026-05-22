Tugas Akhir Percobaan 5 : Binary Search Tree

Judul Proyek : Sistem Inventaris Toko

Proyek ini merupakan sistem sederhana yang menerapkan binary search tree untuk melakukan penyimpanan produk ke dalam gudang dimana user bisa melakukan penambahan data, melihat daftar produk, dan mencari produk spesifik di dalam gudang. sistem ini menggunakan id produk sebagai data yang akan disimpan di node BST, id produk ini berfungsi sebagai kunci untuk mengurutkan, menampilkan, serta mencari produk yang ada di dalam gudang.

source code : 

<img width="2140" height="4168" alt="ss5-1" src="https://github.com/user-attachments/assets/6d71b696-6ee8-4edc-a545-b84b62e8a213" />

Penjelasan : 

1. Baris 1: Membuat class ProdukNode.
2. Baris 2: Fungsi inisialisasi.
3. Baris 3 - 6: Menyimpan 4 data yang diterima.
4. Baris 7 - 8: Membuat node kiri dan kanan.
5. Baris 10: Membuat class InventarisTokoBST.
6. Baris 11 - 12: Saat pertama kali dimulai, root diatur sebagai None.
7. Baris 14: Membuat fungsi tambah_produk yang menerima parameter detail produk untuk dimasukkan ke dalam tree.
8. Baris 15: membuat variabel baru yang memanggil class ProdukNode.
9. Baris 16-19: Mengecek kondisi Jika root masih kosong , maka produk baru akan menjadi Root, lalu fungsi dihentikan.
10. Baris 21: membuat variabel pointer yang posisi awalnya dimulai dari root.
11. Baris 22: Menagmbil kondisi selama True.
12. Baris 23-25: Memeriksa kondisi jika id produk yang ditambahkan sama dengan pointer maka proses dibatalkan.
13. Baris 26: Memeriksa kondisi lain jika id produk yang ditambahkan lebih kecil dari pointer
14. Baris 27-30: jika node kiri kosong maka id produk di simpan disini, kemudian hentikan loop.
15. Baris 31: jika node sudah terisi maka pointer turun ke bawah node tersebut.
16. Baris 32: kondisi lain jika id produk lebih besar.
17. Baris 33-36: jika node kiri kosong maka id produk di simpan disini, kemudian hentikan loop.
18. Baris 37: jika node sudah terisi maka pointer turun ke bawah node tersebut.
19. Baris 39-40: membuat fungsi mencari produk dengan pointer dimulai dari root.
20. Baris 41: mengambil kondisi selama pointer tidak kosong
21. Baris 42-43: kondisi jika id produk sama dengan pointer maka kembalian pointer.
22. Baris 44-45: mengambl kondisi jika id produk lebih kecil dari pointer maka pointer ke child kiri.
23. Baris 46-47: mengambil kondisi jika id produk lebih besar dari pointer maka pointer ke child kanan.
24. Baris 48: kondisi lain jika tidak ada yang memenuhi syarat sebelumnya maka kembalikan none.
25. Baris 50: membuat fungsi untuk menampilkan data produk secara urut.
26. Baris 51: mengambil kondisi jika node tidak kosong.
27. Baris 52: fungsi memanggil dirinya sendiri untuk mencari id terkecil.
28. Baris 53: print data produk 
29. Baris 54: fungsi memeriksa node kanan
30. Baris 56-57: membuat variabel toko yang memanggil fungsi InventarisTokoBST dan membuat variabel pilih sebagai input yang menentukan menu mana yang akan diakses user.
31. Baris 59: mengambil kondisi selama input tidak sama dengan "4".
32. Baris 60-65: menampilkan menu inventaris toko yang berjumlah 4 menu kemudian meminta input dari user untuk memeilih menu.
33. Baris 57-72: mengambil kondisi jika input "1" maka sistem akan meminta input data produk dari user
34. Baris 74: memanggil fungsi tambah_produk untuk menambahkan data yang diinputkan user ke tree.
35. Baris 76-81: mengambil kondisi jika input "2" maka sistem akan mengecek terlebih dahulu jika root kosong maka akan menampilkan pesan gagal, namun jika ada maka akan memanggil fungsi tampilkan_stok_urut
36. Baris 83-84: mengambil kondisi jika input "3" kemudian menampilkan keterangan menu pencarian produk
37. Baris 85-86: mengambil kondisi jika root kosong maka tampilkan pesan gagal
38. Baris 87-89: mengambil kondisi jika root terisi maka siste makan meminta input id yang ingin dicari kemudian memanggil fungsi cari_produk.
39. Baris 90-94: jika barang ditemukan maka akan menampilkan data barang tersebut
40. Baris 95-96: mengambil kondisi jika produk tidak ada maka menampilkan pesan produk tidak ditemukan
41. Baris 98-99: mengambil kondisi jiak pilihan "4" maka tampilkan pesan aplikasi ditutup
42. Baris 101-102: mengambil kondisi lain jika input selain itu maka menampilkan pesan menu tidak tersedia.

Output: 

<img width="488" height="572" alt="output5 1" src="https://github.com/user-attachments/assets/8c312903-8243-4e25-b585-1685ab3197a6" />
<img width="288" height="229" alt="output5 2" src="https://github.com/user-attachments/assets/f5d75146-2ce0-4c4a-8e35-6163677c3363" />

Youtube:

