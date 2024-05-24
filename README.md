# Party-LLM
Aprendizaje acerca de las LLM - IA Generativas

## Link del shell de Linux:

--- curl -fsSL https://ollama.com/install.sh | sh #'''

## Link para activar el servidor ollama:
'''Activar el servidor: 
ollama serve'''

## Link para usar tinyllama:

´´´ollama run tinyllama´´´


### Modo CHAT
Para usar el modo chat basta con colocar el comando anteriormente mencionado. Para detenerlo control C y control D.


### Modo Generativo

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"How are you?",
  "stream": false
}'