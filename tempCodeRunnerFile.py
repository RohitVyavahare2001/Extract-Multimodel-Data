import pytesseract
from PIL import Image

for page_num in range(len(doc)):
    pix = doc[page_num].get_pixmap()  # Render page as image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    text = pytesseract.image_to_string(img)  # Perform OCR

    print(f"--- OCR Extracted Text from Page {page_num + 1} ---\n{text}\n")
