Tugas Akhir Percobaan 1

Judul Proyek : Sistem Booking Kursi Bioskop

Proyek ini merupakan sebuah sistem yang digunakan untuk mempermudah pelanggan dalam memesan kursi di bioskop. sistem booking ini menggunakan konsep list 2D pada python dimana kursi dibuat di dalam list 3 X 5, setiap data di dalam list merepresentasikan sebuah kursi di bioskop. di dalam sistem ini terdapat 2 menu yang bisa diakses oleh pelanggan yaitu menu booking kursi dan keluar. ketika pelanggan memilih menu booking kursi maka pertama-tama sistem akan menunjukkan denah kursi bioskop yang ada, kemudian pelanggan diminta untuk memilih kursi mana yang akan di booking dengan meminta input baris dan kolom. setelah pelanggan memilih kursi, sistem akan memberi pesan bahwa kursi berhasil di booking dan kemudian mengembalikan tampilan pilihan menu, jika pelanggan memilih menu keluar maka sistem akan selesai beroprasi.

<img width="408,5" height="567" alt="code" src="https://github.com/user-attachments/assets/603fa905-51d6-4ec5-9cce-4ca9500fd8fd" />

Baris 2 - 6 
Merupakan list 2D berukuran 3 X 5 yang digunakan untuk menyimpan data dan merepresentasikan kursi bioskop

Baris 8 - 22
Merupakan fungsi untuk menampilkan denah kursi bioskop

  8. deklarasi variabel fungsi dan input yang digunakan
  
  9. Menampilkan "=== DENAH KURSI SAAT INI ===" ke terminal
  
  10. Menampilkan "Kolom: 1 2 3 4 5" ke terminal
  
  11. Menampilkan "----------------------" ke terminal 
  
  12. Deklarasi variabel integer a dengan nilai awal 0
  
  13. Mendeklarasikan loop while dengan kondisi selama a <= 2
  
  14. Deklarasi variabel b dengan nilai awal 0
  
  15. Menampilkan setiap data yang disimpan di index ke 0, 1, dan 2 pada list_kursi ke terminal
  
  16. Deklarasi loop while dengan kondisi selama b <= 4
  
  17. Comment
  
  18. Mengubah nilai data pada list yang akan ditampilkan ke terminal, jika data di list adalah 0 maka akan diubah ke ".", jika 1 maka akan diubah menjadi "X", dan selain itu akan diubah menjadi "M".
  
  19. Menampilkan data menjadi 1 baris 
  
  20. Menambah nilai pada variabel b dengan angka 1 untuk setiap perulangan
  
  21. Pindah baris selanjutnya
  
  22. Menambah nilai pada variabel a dengan angka 1 untuk setiap perulangan

Baris 25 - 52
Merupakan loop untuk menampilkan pilihan menu Booking dan Keluar
  
  25. kondisi perulangan selama True
  
  26. Memanggil fungsi tampilkan_denah
  
  27. Menampilkan "Menu" ke terminal
  
  28. Menampilkan "1. Boking kursi" ke terminal
  
  29. Menampilkan "2. Keluar" ke terminal
  
  30. 
  
  31. variabel untuk meminta input angka ke user
  
  32. Mengambil kondisi jika input 1
  
  33. 
  
  34. variabel untuk meminta input dari 1 sampai 3, kemudian dikurang 1 agar sesuai dengan index pada list_kursi
  
  35. variabel untuk meminta input dari 1 sampai 5, kemudian dikurang 1 agar sesuai dengan index pada list_kursi
  
  36. 
  
  37. Nested if : Mengambil kondisi jika 0 <= r <= dan 0 <= c <= 4
  
  38. Nested di dalam nested : Mengambil kondisi jika data pada list_kursi di index r,c adalah 0
  
  39. Mengubah data pada list_kursi di index r,c menjadi 1
  
  40. Menampilkan "Kursi telah dipesan!" ke terminal
  
  41. Nested di dalam nested : Mengambil Kondisi lain jika data pada list_kursi adalah 1
  
  42. Menampilkan "Kursi sudah dipesan orang lain." ke terminal
  
  43. Nested di dalam nested : Mengambil kondisi terakhir jika selain angka 0 dan 1
  
  44. Menampilkan "Kursi sedang dalam perbaikan." ke terminal
  
  45. Nested : Mengambil kondisi terakhir jika angka diluar jangkauan
  
  46. Menampilkan "Posisi kursi tidak valid." ke terminal
  
  47. 
  
  48. Mengambil kondisi lain jika input adalah 2
  
  49. Menampilkan "Terima kasih!" ke terminal
  
  50. Menghentikan loop
  
  51. Mengambil kondisi terakhir jika input selain 1 dan 2
  
  52. Menampilkan "Pilihan tidak valid." ke terminal
