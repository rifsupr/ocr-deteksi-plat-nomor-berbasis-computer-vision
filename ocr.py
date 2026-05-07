import cv2
import easyocr

# Inisialisasi OCR
reader = easyocr.Reader(['en'])

# Load gambar
image_path = 'images/plat_2.jpg'
image = cv2.imread(image_path)

# =========================
# PREPROCESSING
# =========================

# Convert ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize gambar
gray = cv2.resize(gray, None, fx=2, fy=2)

# Thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Simpan hasil preprocessing
cv2.imwrite('outputs/preprocessed.jpg', thresh)

# =========================
# OCR
# =========================

results = reader.readtext(thresh)

print("Hasil OCR:")
print("-" * 30)

for result in results:
    text = result[1]
    confidence = result[2]

    print(f"Teks       : {text}")
    print(f"Confidence : {confidence:.2f}")
    print("-" * 30)