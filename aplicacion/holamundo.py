import requests as rs
import json as js

url = 'https://api.groq.com/openai/v1/chat/completions'
API_KEY = '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'
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}
myobj = {
         "messages": [
           {
             "role": "system",
             "content": "Eres una IA, responde como una inteligencia artificial."
           },
           {
             "role": "user",
             "content": "¿Cómo se usa el Past Continuous para describir una acción interrumpida?"
           },
         ],
         "model": "mixtral-8x7b-32768",
         "temperature": 1,
         "max_tokens": 1024,
         "top_p": 1,
         "stream": False,
         "stop": None
}

x = rs.post(url, json = myobj, headers=headers)
x = js.loads(x.text)

print(x['choices'][0]['message']['content'])








print("\n"*10)
print(f"¡Hola \n Mundo!")

from math import sqrt as sq

resultado = sq(25)
print(resultado)

print(f'{resultado} es la raiz cuadrada de 25')
