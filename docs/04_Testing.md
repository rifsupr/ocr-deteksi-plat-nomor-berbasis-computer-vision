# Testing and Evaluation
# Implementasi OCR untuk Deteksi Nomor Plat Kendaraan Berbasis Computer Vision Menggunakan YOLOv8 dan EasyOCR

---

# 1. Pengujian Sistem

Pengujian dilakukan untuk mengetahui kemampuan sistem dalam:
- Mendeteksi area plat nomor kendaraan,
- Membaca teks plat menggunakan OCR,
- dan menampilkan hasil deteksi secara otomatis.

Testing dilakukan menggunakan beberapa gambar kendaraan dengan kondisi yang berbeda.

---

# 2. Skenario Pengujian

Berikut beberapa skenario pengujian yang dilakukan:

| No | Skenario | Tujuan |
|---|---|---|
| 1 | Gambar normal | Menguji OCR pada kondisi ideal |
| 2 | Gambar blur | Menguji ketahanan OCR |
| 3 | Pencahayaan rendah | Menguji kemampuan deteksi |
| 4 | Sudut plat miring | Menguji akurasi deteksi |
| 5 | Jarak kendaraan jauh | Menguji pembacaan OCR |

---

# 3. Hasil Pengujian

## Pengujian 1 - Gambar Normal

### Input
Gambar kendaraan dengan pencahayaan baik dan plat terlihat jelas.

### Hasil
- Plat berhasil terdeteksi
- OCR berhasil membaca teks dengan baik

### Output OCR

```text
B 1234 XYZ
```

### Kesimpulan
Sistem bekerja dengan baik pada kondisi gambar normal.

---

# 4. Pengujian 2 - Gambar Blur

### Input
Gambar kendaraan dengan kondisi sedikit blur.

### Hasil
- Plat masih dapat terdeteksi
- OCR mengalami beberapa kesalahan karakter

### Contoh Hasil OCR

```text
B 123A XYZ
```

### Kesimpulan
Kualitas gambar mempengaruhi hasil OCR.

---

# 5. Pengujian 3 — Pencahayaan Rendah

### Input
Gambar kendaraan dengan pencahayaan minim.

### Hasil
- Deteksi plat masih berjalan
- OCR kurang optimal

### Kesimpulan
Pencahayaan rendah mempengaruhi akurasi OCR.

---

# 6. Pengujian 4 — Sudut Plat Miring

### Input
Gambar kendaraan dengan posisi plat miring.

### Hasil
- Sistem masih mampu mendeteksi plat
- OCR kadang mengalami kesalahan pembacaan

### Kesimpulan
Sudut pengambilan gambar mempengaruhi hasil OCR.

---

# 7. Pengujian 5 — Kendaraan Jarak Jauh

### Input
Gambar kendaraan dengan ukuran plat kecil.

### Hasil
- Deteksi plat lebih sulit dilakukan
- OCR kurang akurat

### Kesimpulan
Ukuran plat pada gambar mempengaruhi performa sistem.

---

# 8. Analisis Hasil Pengujian

Berdasarkan hasil testing, sistem memiliki performa yang cukup baik pada kondisi gambar normal.

Beberapa faktor yang mempengaruhi hasil OCR:
- Kualitas gambar,
- Pencahayaan,
- Ukuran plat,
- Blur,
- dan sudut pengambilan gambar.

Preprocessing menggunakan OpenCV membantu meningkatkan kualitas OCR terutama pada gambar dengan kontras rendah.

---

# 9. Kelebihan Sistem

Kelebihan project:
- implementasi sederhana dan ringan,
- mampu mendeteksi plat kendaraan,
- OCR berjalan otomatis,
- mudah digunakan,
- dan cocok sebagai pembelajaran Computer Vision.

---

# 10. Kekurangan Sistem

Kekurangan sistem:
- OCR belum selalu akurat,
- Sensitif terhadap blur,
- Sensitif terhadap pencahayaan rendah,
- dan belum mendukung realtime CCTV.

---

# 11. Evaluasi Sistem

Secara umum sistem berhasil:
- Mendeteksi area plat kendaraan,
- Membaca teks plat,
- dan menampilkan hasil OCR dengan baik.

Kombinasi YOLOv8 dan EasyOCR cukup efektif untuk implementasi sederhana Automatic License Plate Recognition (ALPR).

---

# 12. Dokumentasi Hasil

Berikut dokumentasi hasil testing sistem:

## Hasil Deteksi Plat
Tambahkan screenshot hasil deteksi di sini.

---

## Hasil OCR
Tambahkan screenshot hasil OCR di sini.

---

## Hasil Preprocessing
Tambahkan screenshot preprocessing di sini.

---

# 13. Kesimpulan Pengujian

Berdasarkan hasil pengujian, sistem OCR deteksi nomor plat kendaraan berhasil diimplementasikan menggunakan YOLOv8 dan EasyOCR.

Sistem mampu melakukan:
- Deteksi plat kendaraan,
- OCR nomor plat,
- dan menampilkan hasil OCR secara otomatis.

Walaupun masih memiliki keterbatasan pada kondisi tertentu, project ini sudah mampu merepresentasikan implementasi dasar Computer Vision dan OCR dengan baik.