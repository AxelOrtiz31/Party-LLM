#Importa las 03 librerias necesarias
import requests as rs
import json as js

from PIL import Image
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"/workspace/Party-LLM/aplicacion/sql.jpg"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)


#Codigo para que la IA responda
url = 'http://127.0.0.1:11434/api/generate'
myobj = {
  "model": "llama3",
  "prompt":"Can you make the script for SQL for this picture?",
  "text": [text],
  "stream": False
}

x = rs.post(url, json = myobj)
x = js.loads(x.text)

print(x['response'])


