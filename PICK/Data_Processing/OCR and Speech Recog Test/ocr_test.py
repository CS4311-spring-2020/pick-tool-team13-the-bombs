try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# Simple image to string
print(pytesseract.image_to_string(Image.open('PICK\\Data_Processing\\OCR Test\\typed_test.png')))