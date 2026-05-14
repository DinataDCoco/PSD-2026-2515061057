Tugas Akhir Percobaan 4 : Stack & Queue

Judul Proyek : Sistem Antrian Minimarket

Proyek ini merupakan sebuah sistem sederhana yang berfungsi untuk menambah antrian, melayani antrian, dan melihat jumlah antiran saat ini. Sistem ini mengimplementasikan Queue dan Array dalam algoritma-nya, penggunaan Queue sangat cocok untuk sistem antrian ini karna algoritma dari Queue yang sesuai seperti antrian. sistem akan meminta input berupa angka untuk memilih diantara 4 menu yang tersedia yaitu menu "Tambah Pelanggan" untuk menambah pelanggan, menu "Layani Pelanggan" untuk melayani dan menghapus pelanggan dari antrian, menu "Lihat Antrian" untuk melihat posisi antrian saat ini, dan menu "Keluar" untuk keluar dari sistem. pada menu "Tambah Pelanggan" sistem akan meminta input nama pelanggan berupa string kemudian memasukkannya ke dalam array, pada menu "Layani Pelanggan" sistem akan melakukan pop pada array paling depan atau index ke 0, pada menu "Lihat Antrian" sistem akan menampilkan elemen yang disimpan dalam array saat ini, kemudian pada menu "keluar" sistem akan menyelesaikan loop.

Source Code : 

<img width="732" height="1210" alt="code4" src="https://github.com/user-attachments/assets/5baec25e-017a-4ad8-bcd6-d737e5399941" />

Penjelasan :

Line 1 - 25 merupakan deklarasi class queue 
1. deklarasi class queue
2. deklarasi def __init__ yang mengambil parameter self
3. deklarasi array kosong
5. deklarasi fungsi enqueue dengan parameter self dan item
6. melakukan append ke array
8. deklarasi fungsi dequeue dengan parameter self
9. mengambil kondisi jika array kosong
10. print "Antrian Kosong" ke terminal
11. kembalikan None
12. melakukan pop pada index ke-0
14. deklarasi fungsi is_empty dengan parameter self
15. mengemalikan nilai len array sebagai 0
17. deklarasi fungsi size dengan parameter self
18. kembalikan panjang dari data
20. deklarasi fungsi tampilkan dengan parameter self
21. mengambil kondisi jika array kosong
22. print "Antrian Kosong" ke terminal
23. mengambil kondisi else
24. mengambil loop for i, nama in enumerate(self.data, 1)
25. print parameter i dan nama
27. deklarasi variabek antrian yang mengambil fungsi queue

Line 29 - 56 adalah menu utama
29. deklarasi loop while kondisi True
30. print "===== MENU KASIR ====="
31. print "1. Tambah pelanggan"
32. print "2. Layani pelanggan"
33. print "3. Lihat antrian"
34. print "4. Keluar"
35. deklarasi variabel pilihan yang meminta input string untuk memilih menu
37. mengambil kondisi jika input berupa "1"
38. deklarasi variabel nama untuk meminta input nama berupa string
39. panggil fungsi 1=enqueue
40. print nama dan posisi di array
42. mengambil kondisi lain jika input "2"
43. deklarasi fungsi dilayani yang memanggil  fungsi dequeue
44. mengambil kondisi jika dilayani
45. print dilayani dan sisa antrian saat ini
47. kondisii lain jika input "3"
48. print jumlah antrian saat ini
49. panggil fungsi tampilkan
51. kondisi lain jika input "4"
52. print "Kasir ditutup. Sampai jumpa!"
53. break
55. kondisi terakhir 
56. print "Pilihan tidak valid, coba lagi."

Output : 

<img width="240" height="472" alt="ss hasil 4" src="https://github.com/user-attachments/assets/00bcda31-e103-4cfc-bc07-96c725de64a7" />
<img width="247" height="437" alt="ss hasil 4 2" src="https://github.com/user-attachments/assets/b61ba96b-7d0a-469e-8d2b-32f5b0c5dcec" />

Youtube : 
