import requests as rs

url = 'http://127.0.0.1:11434/api/generate'
myobj = {
  "model": "tinyllama",
  "prompt":"How are you?",
  "stream": False
}

x = rs.post(url, json = myobj)

print(x.text)