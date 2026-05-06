# Project Plan
# Implementasi OCR untuk Deteksi Nomor Plat Kendaraan Berbasis Computer Vision Menggunakan YOLOv8 dan EasyOCR

---

# 1. Gambaran Project

Project ini merupakan implementasi Computer Vision untuk mendeteksi dan membaca nomor plat kendaraan menggunakan teknologi Object Detection dan Optical Character Recognition (OCR).

Sistem dikembangkan menggunakan:
- YOLOv8 untuk mendeteksi area plat nomor kendaraan
- OpenCV untuk preprocessing gambar
- EasyOCR untuk membaca teks pada plat kendaraan

Output akhir project berupa aplikasi sederhana berbasis Streamlit yang mampu:
- menerima input gambar kendaraan,
- mendeteksi area plat,
- membaca teks nomor plat,
- dan menampilkan hasil OCR secara otomatis.

---

# 2. Latar Belakang

Computer Vision merupakan salah satu bidang Artificial Intelligence yang memungkinkan komputer memahami informasi visual dari gambar maupun video.

Salah satu implementasi populer dari Computer Vision adalah Automatic License Plate Recognition (ALPR), yaitu sistem yang dapat mendeteksi dan membaca nomor plat kendaraan secara otomatis.

Teknologi ini banyak digunakan pada:
- Sistem parkir otomatis,
- Pembayaran tol otomatis,
- Monitoring lalu lintas,
- Identifikasi kendaraan,
- dan sistem smart city.

Melalui project ini dilakukan implementasi sederhana ALPR menggunakan YOLOv8 dan EasyOCR sebagai bentuk penerapan pembelajaran Computer Vision.

---

# 3. Rumusan Masalah

Permasalahan yang ingin diselesaikan pada project ini yaitu:

1. Bagaimana mendeteksi area plat kendaraan menggunakan Computer Vision?
2. Bagaimana membaca teks plat kendaraan menggunakan OCR?
3. Bagaimana menggabungkan Object Detection dan OCR dalam satu sistem sederhana?

---

# 4. Tujuan Project

## Tujuan Utama

Membangun sistem OCR sederhana untuk mendeteksi dan membaca nomor plat kendaraan menggunakan Computer Vision.

---

## Tujuan Khusus

- Mengimplementasikan YOLOv8 untuk deteksi plat nomor kendaraan
- Menggunakan EasyOCR untuk membaca karakter pada plat
- Melakukan preprocessing gambar menggunakan OpenCV
- Mengembangkan aplikasi sederhana berbasis Streamlit
- Mendokumentasikan project secara terstruktur di GitHub

---

# 5. Ruang Lingkup Project

## Cakupan Project

- Upload gambar kendaraan
- Deteksi area plat nomor
- OCR nomor plat kendaraan
- Menampilkan hasil OCR
- Interface sederhana menggunakan Streamlit

---

# 6. Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Bahasa Pemrograman | Python |
| Object Detection | YOLOv8 |
| OCR | EasyOCR |
| Image Processing | OpenCV |
| Interface | Streamlit |
| Deep Learning Framework | PyTorch |
| Development Tools | VS Code |
| Version Control | GitHub |

---

# 7. Arsitektur Sistem

```text
Input Gambar
      ↓
Deteksi Plat dengan YOLOv8
      ↓
Crop Area Plat
      ↓
Preprocessing Gambar
      ↓
EasyOCR
      ↓
Hasil OCR
```

---

# 8. Tahapan Pengembangan

## Tahap 1 — Persiapan Environment
- Install library dan dependency
- Membuat struktur project
- Membuat repository GitHub

---

## Tahap 2 — Persiapan Model Deteksi
- Menyiapkan model pretrained YOLOv8
- Testing deteksi objek

---

## Tahap 3 — Implementasi OCR
- Crop area plat yang terdeteksi
- Preprocessing gambar
- OCR untuk membaca teks plat

---

## Tahap 4 — Integrasi Sistem
- Menggabungkan deteksi plat dan OCR
- Menampilkan hasil OCR

---

## Tahap 5 — Pembuatan Interface
- Membuat aplikasi Streamlit
- Fitur upload gambar
- Menampilkan hasil deteksi dan OCR

---

## Tahap 6 — Testing dan Dokumentasi
- Testing menggunakan beberapa gambar
- Dokumentasi hasil project
- Finalisasi GitHub repository

---

# 9. Rencana Struktur Project

```text
alpr-ocr-project/
│
├── app/
│   └── app.py
│
├── docs/
│   ├── 01_project_plan.md
│   ├── 02_methodology.md
│   ├── 03_implementation.md
│   ├── 04_testing.md
│   └── assets/
│
├── images/
├── outputs/
├── models/
│   └── best.pt
│
├── detect.py
├── ocr.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 10. Output yang Diharapkan

Output yang diharapkan dari project ini:

- Sistem OCR deteksi nomor plat kendaraan
- Aplikasi berbasis Streamlit
- Dokumentasi project di GitHub
- Hasil testing sistem
- Screenshot hasil deteksi
- Portfolio project Computer Vision

---

# 11. Kesimpulan

Project ini dirancang sebagai implementasi sederhana Computer Vision menggunakan YOLOv8 dan EasyOCR untuk mendeteksi dan membaca nomor plat kendaraan secara otomatis.

Dengan ruang lingkup yang sederhana, project ini tetap dapat merepresentasikan implementasi AI secara nyata dan dapat menjadi portfolio yang relevan dalam bidang Artificial Intelligence dan Computer Vision.