Tugas Akhir Percobaan 3 : Searching

Judul Proyek : Sistem pencarian dan tambah no hp

Proyek ini merupakan sebuah sistem yang berfungsi untuk mencari dan menambahkan nomor telepon yang disimpan di dalam dictionary. sistem ini mengimplementasikan algoritma sequential search karena sistem ini tidak perlu mengurutkan data terleih dahulu selama proses berlangsung. pertama-tama sistem akan meminta input nama nomor hp yang ingin dicari, input ini yang akan digunakan sebagai key untuk mencari nomor telepon di dalam dictionary, jika nama ada dalam dictionary maka sistem akan menampilkan informasi kontak dari nama tersebut, jika tidak maka sistem akan memberitahu bahwa nama tidak terdaftar. setelah itu sistem ini akan menanyakan apakah user akan menambah nomor baru atau tidak, jika ya maka sistem akan meminta input nama dan nomor hp yang kemudian akan disimpan ke dictionary sebagai data baru, jika tidak maka program akan selesai.

Source Code : 

<img width="1448" height="2154" alt="code_3" src="https://github.com/user-attachments/assets/bcba1dc1-e80e-4b96-a9b2-587257c8d734" />

Penjelasan :

Line 1 - 5 : fungsi sequential search

1. deklarasi fungsi sequential search untuk mencari nomor telepon dengan mengambil parameter buku_telepon dan nama_target
2. kondisi loop for kontak di variabel buku_telepon
3. mengambil kondisi jika input nama_target ada di dictionary dengan key 'nama'
4. mengembalikan nomor hp
5. mengembalikan none jika kondisi tidak terpenuhi

line 7 - 12 : dictionary untuk menyimpan daftar kontak hp

7. deklarasi variabel buku_telepon
8. data dalam dictionary
9. data dalam dictionary
10. data dalam dictionary
11. data dalam dictionary
12. tutup kurung

Line 14 - 27 : Fungsi cek kontak dan tambah kontak

14. deklarasi fungsi tambah_kontak dengan mengambil parameter buku_telepon, nama_baru, nomor_baru
15. deklarasi variabel untuk_cek dengan mengambil input dari variabel nama_baru
16. memgambil loop for kontak di buku_telepon
17. mengambil kondisi jika vairabel unutk_cek sudah ada di kontak
18. menampilkan "Gagal! Nama '{nama_baru}' sudah ada di buku telepon." ke terminal
19. mengembalikan false
21. deklarasi variabel kontak_baru
22. isi dictionary
23. isi dictionary
25. memasukkan data pada kontak_baru ke buku_telepon
26. menampilkan "Berhasil! Kontak '{nama_baru}' telah ditambahkan." ke teminal
27. kembalikan true

Line 29 - 35 : Mencari nomor di dictionary

29. deklarasi variabel nama_dicari untuk meminta input nama yang ingin dicari
30. deklarasi variabel hasil yang mengambil fungsi cari_nomor_telepon
32. mengambil kondisi jika hasil
33. tampilkan nomor telepon yang dicari
34. kondisi else
35. menampilkan pemberitahuan nomor telepon yang dicari tidak tersedia

line 37 - 49 : Menambah nomor baru

37. deklarasi vairabel Masukkan_nomor_baru untuk meminta input string
39. kondisi jika input adalah "y"
40. minta input nama
41. minta input nomor
43. panggil fungsi tambah_kontak
45. tampilkan "daftar kontak sekarang" ke terminal
46. kondisi for k di buku_telepon
47. tampilkan nama dan nomor
48. kondisi jika input adalah "n"
49. tampilkan "Selesai."

Output : 

<img width="324" height="226" alt="ss3" src="https://github.com/user-attachments/assets/b8d92d3c-593a-47cc-be8f-27827dead127" />

Youtube :

https://youtu.be/PN5bor3IdNU
