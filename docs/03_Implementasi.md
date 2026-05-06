# Implementation
# Implementasi OCR untuk Deteksi Nomor Plat Kendaraan Berbasis Computer Vision Menggunakan YOLOv8 dan EasyOCR

---

# 1. Persiapan Environment

Sebelum menjalankan project, beberapa library perlu diinstall terlebih dahulu.

Library yang digunakan:
- ultralytics
- easyocr
- opencv-python
- streamlit
- pillow
- numpy

Install dependency menggunakan perintah berikut:

```bash
pip install ultralytics
pip install easyocr
pip install opencv-python
pip install streamlit
pip install pillow
pip install numpy
```

Atau menggunakan:

```bash
pip install -r requirements.txt
```

---

# 2. Struktur Project

Berikut struktur folder project yang digunakan:

```text
alpr-ocr-project/
│
├── app/
│   └── app.py
│
├── docs/
│
├── images/
│
├── outputs/
│
├── models/
│   └── best.pt
│
├── detect.py
├── ocr.py
├── requirements.txt
├── README.md
└── .gitignore
```

Penjelasan:
- app.py digunakan untuk interface Streamlit
- detect.py digunakan untuk deteksi plat nomor
- ocr.py digunakan untuk proses OCR
- models/ digunakan untuk menyimpan model YOLOv8

---

# 3. Persiapan Model YOLOv8

Project menggunakan model pretrained YOLOv8 untuk mendeteksi plat nomor kendaraan.

Model disimpan pada folder:

```text
models/best.pt
```

Model ini digunakan untuk:
- mendeteksi area plat kendaraan,
- menghasilkan bounding box,
- dan memberikan koordinat area plat.

---

# 4. Implementasi Deteksi Plat

Deteksi plat dilakukan menggunakan YOLOv8.

Tahapan deteksi:
1. Membaca gambar input
2. Menjalankan model YOLOv8
3. Mengambil koordinat bounding box
4. Menampilkan hasil deteksi

Contoh alur deteksi:

```text
Input Image
      ↓
YOLOv8 Detection
      ↓
Bounding Box Plat
```

Output:
- Gambar hasil deteksi,
- Koordinat area plat.

---

# 5. Implementasi Crop Area Plat

Setelah plat berhasil dideteksi, sistem melakukan crop pada area plat menggunakan koordinat bounding box.

Tujuan crop:
- Mengambil area fokus plat,
- Mengurangi noise,
- dan mempermudah proses OCR.

Output dari proses ini berupa gambar plat kendaraan.

---

# 6. Implementasi Preprocessing

Sebelum OCR dilakukan, gambar plat diproses menggunakan OpenCV.

Tahapan preprocessing:
- Grayscale,
- Resize,
- Thresholding,
- Noise reduction.

Contoh alur preprocessing:

```text
Original Image
      ↓
Grayscale
      ↓
Threshold
      ↓
Resize
      ↓
OCR Ready Image
```

Tujuan preprocessing:
- Meningkatkan kualitas teks,
- Memperjelas karakter,
- dan membantu akurasi OCR.

---

# 7. Implementasi OCR Menggunakan EasyOCR

OCR dilakukan menggunakan EasyOCR.

Tahapan OCR:
1. Membaca gambar hasil preprocessing
2. Menjalankan EasyOCR
3. Mengambil hasil teks OCR
4. Menampilkan hasil nomor plat

Contoh hasil OCR:

```text
B 1234 XYZ
```

Output:
- teks nomor plat kendaraan.

---

# 8. Integrasi Sistem

Semua proses digabungkan menjadi satu pipeline sistem.

Pipeline implementasi:

```text
Input Gambar
      ↓
YOLOv8 Detection
      ↓
Crop Plat
      ↓
Preprocessing OpenCV
      ↓
EasyOCR
      ↓
Output OCR
```

Output akhir:
- hasil deteksi plat,
- hasil OCR,
- dan visualisasi sistem.

---

# 9. Implementasi Interface Streamlit

Project menggunakan Streamlit untuk membuat interface aplikasi sederhana.

Fitur interface:
- Upload gambar,
- Preview gambar,
- Hasil deteksi plat,
- Hasil OCR.

Perintah menjalankan aplikasi:

```bash
streamlit run app.py
```

---

# 10. Hasil Implementasi

Hasil implementasi sistem:
- Sistem mampu mendeteksi area plat nomor,
- Melakukan OCR pada plat,
- dan menampilkan hasil teks kendaraan.

Output yang dihasilkan:
- Gambar hasil deteksi,
- Area crop plat,
- Hasil OCR.

---

# 11. Kendala Implementasi

Beberapa kendala yang ditemukan:
- OCR kurang akurat pada gambar blur,
- Pencahayaan rendah mempengaruhi hasil OCR,
- Sudut plat tertentu sulit dideteksi.

Solusi yang dilakukan:
- Preprocessing gambar,
- Resize area plat,
- dan thresholding untuk meningkatkan kontras.

---

# 12. Kesimpulan Implementasi

Implementasi sistem berhasil dilakukan menggunakan kombinasi YOLOv8, OpenCV, dan EasyOCR.

Sistem mampu:
- Mendeteksi area plat kendaraan,
- Membaca teks plat,
- dan menampilkan hasil OCR dalam aplikasi sederhana berbasis Streamlit.

Project ini menjadi implementasi sederhana Computer Vision yang dapat digunakan sebagai media pembelajaran maupun portfolio project AI.