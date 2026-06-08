1. Baris 1: Membuat class InventarisToko sebagai cetak biru untuk membungkus semua fungsi logika toko.
2. Baris 2: Fungsi constructor untuk inisialisasi awal saat objek toko dibuat.
3. Baris 3: Menyiapkan dictionary kosong bernama data_barang. Di sinilah konsep Hash Map bekerja menggunakan pasangan Key dan Value.
4. Baris 5: Membuat fungsi tambah_barang yang menerima parameter ID, nama, dan stok awal.
5. Baris 6: Memeriksa kondisi jika ID barang sudah ada di dalam hash map untuk menghindari data ganda.
6. Baris 7: Jika ID sudah ada, sistem menampilkan pesan bahwa barang sudah terdaftar.
7. Baris 8: Kondisi jika ID belum ada di dalam sistem.
8. Baris 9-12: Menyimpan data baru ke dalam hash map dengan ID barang sebagai Key, serta Nama dan Stok sebagai Value-nya.
9. Baris 13: Menampilkan pesan sukses bahwa barang berhasil didaftarkan.
10. Baris 15: Membuat fungsi cari_barang berdasarkan ID yang dicari.
11. Baris 16: Mengambil data dari hash map secara instan menggunakan perintah .get().
12. Baris 17: Memeriksa kondisi jika data barang ditemukan (tidak kosong).
13. Baris 18-19: Menampilkan detail data barang yang ditemukan ke layar dan mengembalikan nilai data tersebut.
14. Baris 20-22: Kondisi jika tidak ditemukan, sistem menampilkan pesan error dan mengembalikan nilai None.
15. Baris 24: Membuat fungsi update_stok untuk mengubah jumlah stok barang yang sudah ada.
16. Baris 25: Memeriksa kondisi jika ID barang yang ingin diubah terdaftar di dalam hash map.
17. Baris 26-27: Mengambil angka stok lama, lalu menimpanya dengan angka stok yang baru.
18. Baris 28: Menampilkan pesan konfirmasi perubahan angka stok di layar.
19. Baris 29-30: Kondisi jika ID tidak ada, sistem menampilkan pesan bahwa update gagal.
20. Baris 32: Membuat fungsi hapus_barang untuk mendepak barang dari sistem.
21. Baris 33: Memeriksa kondisi jika ID barang yang akan dihapus tersedia di dalam hash map.
22. Baris 34-35: Menghapus data barang dari hash map menggunakan perintah .pop() dan menampilkan nama barang yang dihapus.
23. Baris 36-37: Kondisi jika ID tidak ada, sistem menampilkan pesan bahwa proses hapus gagal.
24. Baris 39: Membuat fungsi tampilkan_semua untuk melihat seluruh isi inventaris.
25. Baris 40: Mencetak garis pembatas dan judul tabel di layar terminal.
26. Baris 41-42: Memeriksa kondisi jika hash map masih kosong, maka sistem menampilkan pesan bahwa toko kosong.
27. Baris 43-44: Melakukan perulangan untuk membongkar dan mencetak semua pasangan ID, Nama, dan Stok dari hash map.
28. Baris 45: Mencetak garis penutup tabel.
29. Baris 47: Membuat objek toko bernama toko_elektronik berbasis dari kelas InventarisToko.
30. Baris 49: Membuat fungsi utama bernama main untuk mengatur jalannya menu aplikasi.
31. Baris 50-56: Mencetak daftar teks menu pilihan 1 sampai 6 ke layar terminal.
32. Baris 57: Menyiapkan variabel pilih_menu untuk membaca input angka yang diketik oleh pengguna.
33. Baris 59: Memulai perulangan menu selama pilihan yang dimasukkan bukan angka "6".
34. Baris 60-64: Kondisi jika input adalah "1", sistem meminta input ID, Nama, dan Stok baru dari pengguna.
35. Baris 65: Memanggil fungsi tambah_barang untuk dimasukkan ke hash map, lalu mengulang fungsi main() dan menghentikan loop saat ini.
36. Baris 66-68: Kondisi jika input adalah "2", sistem meminta input ID barang yang ingin dicari.
37. Baris 69: Memanggil fungsi cari_barang, lalu mengulang fungsi main() dan menghentikan loop saat ini.
38. Baris 71-73: Kondisi jika input adalah "3", sistem meminta input ID dan angka stok baru yang diinginkan.
39. Baris 74: Memanggil fungsi update_stok, lalu mengulang fungsi main() dan menghentikan loop saat ini.
40. Baris 77-79: Kondisi jika input adalah "4", sistem meminta input ID barang yang akan dieksekusi.
41. Baris 80: Memanggil fungsi hapus_barang, lalu mengulang fungsi main() dan menghentikan loop saat ini.
42. Baris 82-83: Kondisi jika input adalah "5", sistem langsung memanggil fungsi tampilkan_semua.
43. Baris 84: Mengulang fungsi main() dan menghentikan loop saat ini.
44. Baris 86-87: Kondisi jika input adalah "6", perulangan langsung dihentikan dan aplikasi ditutup.
45. Baris 88-91: Kondisi terakhir jika input selain angka 1-6, sistem menampilkan pesan "input salah!", lalu memanggil kembali fungsi main().
46. Baris 92: Memanggil fungsi main() di baris paling luar sebagai tombol utama untuk menyalakan program pertama kali.
