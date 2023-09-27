# Penyelesaian Traveling Salesman Problem (TSP) dengan Python

Kode ini adalah implementasi sederhana untuk menyelesaikan Traveling Salesman Problem (TSP) menggunakan pendekatan brute-force dengan menghitung semua kemungkinan permutasi rute yang mungkin. Berikut adalah penjelasan singkat tentang bagaimana kode ini berfungsi:

1. `calculate_total_distance(path, graph)`: Fungsi ini menghitung total jarak dari suatu rute berdasarkan grafik jarak yang diberikan. Ini melakukan iterasi melalui setiap pasangan simpul yang dihubungkan dalam rute dan menjumlahkan jarak antara mereka.

2. `solve_tsp(graph)`: Fungsi ini adalah algoritma utama untuk menyelesaikan TSP. Ini memulai dari simpul awal (dalam hal ini simpul 0), dan kemudian mencoba semua kemungkinan permutasi rute yang mungkin menggunakan modul `itertools`. Algoritma ini selalu mencari rute dengan jarak terpendek. 

3. `graph`: Ini adalah matriks yang mewakili jarak antara setiap pasangan simpul dalam grafik. Anda dapat mengganti grafik ini dengan grafik TSP yang berbeda.

## Menjalankan Kode

Anda dapat menjalankan kode ini dengan menggunakan interpreter Python. Pastikan Anda memiliki Python terinstal di komputer Anda.

1. Salin kode di atas dan simpan dalam sebuah file dengan ekstensi `.py`.

2. Jalankan file tersebut dengan perintah berikut melalui terminal:

   ```bash
   python nama_file.py
   ```

   Gantilah `nama_file.py` dengan nama file tempat Anda menyimpan kode ini.

## Hasil

Setelah kode dijalankan, hasil solusi TSP akan dicetak di layar, termasuk rute terbaik dan jarak terpendeknya.

**Catatan**: Metode ini akan menjadi tidak efisien untuk grafik yang sangat besar karena mencoba semua kemungkinan permutasi. Untuk masalah TSP yang lebih besar, akan lebih baik menggunakan algoritma heuristik seperti Algoritma Nearest Neighbor atau Algoritma 2-Opt untuk mendapatkan solusi yang lebih cepat meskipun tidak selalu optimal.

Selamat mencoba menyelesaikan Traveling Salesman Problem dengan kode ini!
