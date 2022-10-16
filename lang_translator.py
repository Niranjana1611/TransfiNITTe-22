# adds image processing capabilities
from PIL import Image
from langdetect import detect


# will convert the image to text string
from pytesseract import pytesseract

### translates into preferred language
from googletrans import Translator
from google_trans_new import google_translator 

# assigning an image from the source path
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open('ac214128.pdf-page002-img000.png')

pytesseract.tesseract_cmd = path_to_tesseract
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

p = Translator()

result_lang = detect(result)

print(result_lang)

# translates the text into french language
#k = p.translate(result,lang_tgt='en') 
#converts the result into string format


translator = google_translator(url_suffix="hk",timeout=5,proxies={'http':'118.185.38.153'})
k = translator.translate(result,lang_src=result_lang,lang_tgt='en')

translated = str(k.text)

with open('test.txt', mode ='w') as file:
  file.write(result)
  file.write("\n")
  file.write(translated)
  print("ready!")
