import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r""

def convert():
    img = Image.open('image,jpg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()