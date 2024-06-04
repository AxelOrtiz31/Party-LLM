#Importa las 03 librerias necesarias
import requests as rs
import json as js
import base64

#Codigo para transformar una imagen a base64
with open('piz.jpeg', 'rb') as f:
    convert = base64.b64encode(f.read())

img = convert.decode('utf-8')



#Codigo para que la IA responda
url = 'http://127.0.0.1:11434/api/generate'
myobj = {
  "model": "llava",
  "prompt":"What is in this picture?",
  "images": [img],
  "stream": False
}

x = rs.post(url, json = myobj)
x = js.loads(x.text)

print(x['response'])
