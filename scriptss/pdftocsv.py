import os
from PIL import Image
from pytesseract import pytesseract
import easyocr

    #"./instance/uploads/"+os.listdir("instance/uploads")[0]
def convert():
    path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    image_path = "./instance/uploads/"+os.listdir("instance/uploads")[0]
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img)

    os.remove("./instance/uploads/"+os.listdir("instance/uploads")[0])
    return(text[:-1])

        
