from PIL import Image
import pytesseract
from googletrans import Translator
from translate import Translator
import os
import glob

# Sets up the googletranslator api
translator = Translator(to_lang="eng")

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Edit this path to tesseract.exe on your system. On windows its by default in the following:
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

# Path to the images folder. Edit this to yours.
os.chdir("C:\\Users\\Niranjana\\Desktop\\Brain Uninstalled")

# Goes thru every image:
for images in glob.glob("*.png"):
    # Opens image
    im = Image.open(images)

    # Gets the image and translates it to Czech. You can specify own lang if you want.
    text = pytesseract.image_to_string(im, lang = 'tam')
    text_translated = translator.translate(text)

    # Finally, print the translated image's text and print it.
    print(text_translated)
    print("\n")
