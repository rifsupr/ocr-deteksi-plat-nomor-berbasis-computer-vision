# Methodology
# Implementasi OCR untuk Deteksi Nomor Plat Kendaraan Berbasis Computer Vision Menggunakan YOLOv8 dan EasyOCR

---

# 1. Metode Pengembangan

Project ini dikembangkan menggunakan pendekatan implementasi sederhana Computer Vision dengan menggabungkan teknologi Object Detection dan Optical Character Recognition (OCR).

Metode utama yang digunakan yaitu:
- YOLOv8 untuk mendeteksi area plat nomor kendaraan
- EasyOCR untuk membaca teks pada plat nomor
- OpenCV untuk preprocessing gambar

Sistem dirancang agar mampu mendeteksi plat kendaraan dari gambar dan menampilkan hasil pembacaan teks secara otomatis.

---

# 2. Alur Sistem

Berikut alur kerja sistem secara umum:

```text
Input Gambar
      ↓
Deteksi Plat Nomor
      ↓
Crop Area Plat
      ↓
Preprocessing Gambar
      ↓
OCR dengan EasyOCR
      ↓
Menampilkan Hasil OCR
```

---

# 3. Input Sistem

Input utama sistem berupa gambar kendaraan.

Gambar dapat berupa:
- Mobil,
- Motor,
- atau kendaraan lain yang memiliki plat nomor yang terlihat jelas.

Format gambar yang digunakan:
- JPG
- JPEG
- PNG

---

# 4. Deteksi Plat Nomor Menggunakan YOLOv8

Tahap pertama sistem adalah mendeteksi lokasi plat nomor kendaraan menggunakan YOLOv8.

YOLOv8 digunakan karena:
- Memiliki performa deteksi yang cepat,
- Akurasi cukup baik,
- dan mudah digunakan untuk implementasi Computer Vision.

Pada tahap ini sistem akan:
- Membaca gambar,
- Mendeteksi area plat,
- dan menghasilkan bounding box pada plat kendaraan.

Output dari tahap ini berupa koordinat area plat nomor.

---

# 5. Crop Area Plat

Setelah plat nomor berhasil dideteksi, sistem akan melakukan crop pada area plat berdasarkan koordinat bounding box.

Tujuan proses crop:
- Mengambil fokus area plat,
- Mengurangi noise dari gambar lain,
- dan meningkatkan akurasi OCR.

Hasil crop kemudian digunakan pada tahap preprocessing.

---

# 6. Preprocessing Gambar Menggunakan OpenCV

Sebelum dilakukan OCR, gambar plat akan diproses terlebih dahulu menggunakan OpenCV.

Tahapan preprocessing yang digunakan:
- Mengubah gambar menjadi grayscale,
- Resize gambar,
- Thresholding,
- dan pengurangan noise sederhana.

Tujuan preprocessing:
- Memperjelas karakter pada plat,
- Meningkatkan kontras teks,
- dan membantu proses OCR agar lebih akurat.

---

# 7. OCR Menggunakan EasyOCR

Setelah preprocessing selesai, sistem menggunakan EasyOCR untuk membaca teks pada plat kendaraan.

EasyOCR bekerja dengan:
- Mengenali pola karakter,
- Mengekstraksi teks dari gambar,
- dan menghasilkan output berupa nomor plat kendaraan.

Contoh hasil OCR:

```text
B 1234 XYZ
```

---

# 8. Integrasi Sistem

Semua tahapan digabungkan menjadi satu pipeline sistem.

Pipeline sistem:

```text
Input Gambar
      ↓
YOLOv8 Detection
      ↓
Crop Plat
      ↓
Preprocessing
      ↓
EasyOCR
      ↓
Hasil OCR
```

Output akhir sistem berupa:
- Gambar hasil deteksi,
- Area plat,
- dan teks nomor kendaraan.

---

# 9. Interface Sistem

Project ini menggunakan Streamlit sebagai interface aplikasi.

Fitur utama interface:
- Upload gambar,
- Menampilkan gambar hasil deteksi,
- Menampilkan hasil OCR,
- dan menampilkan bounding box pada plat nomor.

Streamlit dipilih karena:
- Ringan,
- Mudah digunakan,
- dan cocok untuk demo project AI sederhana.

---

# 10. Struktur Implementasi

Struktur implementasi project:

```text
alpr-ocr-project/
│
├── app/
├── docs/
├── images/
├── outputs/
├── models/
├── detect.py
├── ocr.py
└── requirements.txt
```

Keterangan:
- detect.py digunakan untuk deteksi plat nomor
- ocr.py digunakan untuk proses OCR
- app.py digunakan untuk interface Streamlit

---

# 11. Pengujian Sistem

Pengujian dilakukan menggunakan beberapa gambar kendaraan dengan kondisi berbeda.

Skenario pengujian:
- Gambar normal,
- Pencahayaan rendah,
- Gambar blur,
- dan sudut plat berbeda.

Tujuan pengujian:
- Mengetahui kemampuan deteksi sistem,
- dan mengevaluasi hasil OCR.

---

# 12. Hasil yang Diharapkan

Sistem diharapkan mampu:
- Mendeteksi area plat kendaraan,
- Membaca teks plat,
- dan menampilkan hasil OCR dengan baik.

Selain itu project ini diharapkan dapat menjadi implementasi sederhana Computer Vision yang dapat digunakan sebagai portfolio pembelajaran AI dan OCR.