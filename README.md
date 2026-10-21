# Pertemuan 10 - String dan Pengolah Teks

Nama: Alya Mutiara Marine
NIM: 2225250224
Kelas: 3A

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan
Jalankan file program menggunakan perintah **Python Launcher (`py`)** melalui terminal karena adanya masalah pembacaan *path* *default* Windows:

```bash
py tugas/normalisasi_data_mahasiswa.py
```

## Algoritma
Proses normalisasi data mahasiswa dilakukan melalui langkah-langkah berikut:
1. **Pembersihan Nama**: String nama masukan dihapus spasi kosong di awal dan akhirnya menggunakan method `.strip()`, kemudian diubah formatnya menjadi kapital di setiap awal kata (*Title Case*) menggunakan method `.title()`.
2. **Pembuatan Inisial**: String nama bersih dipecah berdasarkan spasi menjadi *list* kata terpisah memakai `.split()`. Setelah itu, karakter pertama (indeks ke-0) dari masing-masing kata diambil, dikumpulkan, lalu digabung kembali menggunakan `"".join()`.
3. **Normalisasi Kode Kelas**: String kode kelas diubah menjadi huruf kapital secara menyeluruh via `.upper()`, lalu dipecah spasi tengahnya dan dirangkai kembali secara rapi dengan pembatas tanda hubung `-` menggunakan `"-".join()`.

## Test Case

| Nama File Uji | Data Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| `01_dasar_string.py` | `"Algoritma"` | Cetak string asli, panjang teks = 9, huruf besar, huruf kecil | Algoritma, 9, ALGORITMA, algoritma | **LULUS** |
| `02_indeks_slicing.py` | `"Pemrograman"` | Akses indeks awal/akhir, potong string depan/belakang, balik string | P, n, Pemr, ograman, namargormeP | **LULUS** |
| `03_method_string.py` | `"   fATHIYYAH mUTHMAINNAH  "` | Teks bersih tanpa spasi luar, format title case, format kapital | fATHIYYAH mUTHMAINNAH, Fathiyyah Muthmainnah, FATHIYYAH MUTHMAINNAH | **LULUS** |
| `04_bersihkan_teks.py` | `"   belajar     python..."` | Menghapus spasi luar dan mereduksi spasi ganda di tengah kalimat | Belajar python untuk pendidikan | **LULUS** |
| `05_split_join.py` | `"data teks perlu dibersihkan"` | Memecah teks menjadi list kata dan menyambungnya kembali dengan strip `-` | `['data', 'teks', 'perlu', 'dibersihkan']`, data-teks-perlu-dibersihkan | **LULUS** |
| `06_pencarian_kata.py` | Teks & Pencarian kata `"python"` | Cek keberadaan kata (`True`), hitung jumlah kemunculan (`2`), cari indeks pertama (`0`) | True, 2, 0 | **LULUS** |
| `normalisasi_data_mahasiswa.py` | Data: Alya Mutiara Marine & PMAT-A-2026 | Nama: Alya Mutiara Marine, Kelas: PMAT-A-2026, Jumlah kata: 3, Inisial: AMM | Nama bersih: Alya Mutiara Marine, Kode kelas: PMAT-A-2026, Jumlah kata: 3, Inisial: AMM | **LULUS** |

## Refleksi
* **Masalah teks yang ditemukan**: Terjadi masalah spasi berantakan yang berlebih di awal maupun di akhir string input, serta format penulisan huruf kapital yang tidak konsisten pada nama dan kode kelas (seperti huruf kecil semua atau spasi terpisah tengah jalan). Selain itu, di terminal sempat terjadi kesalahan pencarian file akibat salah mengetik nama file `split_join.py` yang seharusnya `05_split_join.py`.
* **Cara memperbaikinya**: Masalah spasi dan kapitalisasi teks diselesaikan secara otomatis menggunakan rangkaian fungsi bawaan Python seperti `.strip()`, `.title()`, `.upper()`, serta manipulasi `.split()` dan `.join()`. Untuk kesalahan eksekusi file di terminal diperbaiki dengan memastikan ketikan jalur file sudah tepat (`py latihan/05_split_join.py`).