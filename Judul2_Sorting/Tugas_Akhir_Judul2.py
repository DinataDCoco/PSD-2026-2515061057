def bubble_sort(data):
    n = len(data)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

skor_ujian = []

o = int(input("Masukkan jumlah mahasiswa :"))
for i in range (o):
    input_nilai = int(input("Masukkan Nilai Ujian : "))
    app = skor_ujian.append(input_nilai)

print("Skor Sebelum Sorting:", skor_ujian)

skor_terurut = bubble_sort(skor_ujian)

print("Skor Setelah Sorting (Bubble Sort):", skor_terurut)