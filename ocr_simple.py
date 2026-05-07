import easyocr

# Inisialisasi OCR reader
reader = easyocr.Reader(['en'])

# Path gambar
image_path = 'images/plat_2.jpg'

# Jalankan OCR
results = reader.readtext(image_path)

# Tampilkan hasil
print("Hasil OCR:")

for result in results:
    text = result[1]
    confidence = result[2]

    print(f"Teks: {text}")
    print(f"Confidence: {confidence}")
    print("-" * 30)