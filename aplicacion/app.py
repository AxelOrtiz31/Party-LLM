import requests as rs
import json as js

url = 'http://127.0.0.1:11434/api/generate'
myobj = {
  "model": "llama3",
  "prompt":"¿Puedes dar un ejemplo de una pregunta en Past Continuous?",
  "stream": False
}

x = rs.post(url, json = myobj)
x = js.loads(x.text)

print(x['response'])








print("\n"*10)
print(f"¡Hola \n Mundo!")

from math import sqrt as sq

resultado = sq(25)
print(resultado)

print(f'{resultado} es la raiz cuadrada de 25')
