# Party-LLM
Aprendizaje acerca de las LLM - IA Generativas.

Este repositorio hecho en la materia de Base de Datos para Aplicaciones tiene el proposito de
enseñarnos como usar IAs interactivas para responder a las preguntas que le hagamos.

## Acerca de Ollama:

Ollama es una pagina web que proveee a los usuarios los servicios de diversas inteligencias artifiales (LLM), esto a travez de un muy extenso catalogo de IAs. Cada una de ellas cuenta con sus respectivas instrucciones acerca de como usarlas y aplicarlas en nuestro trabajo.

También se incluyen los repositorios de Github entre muchas otras herramientas, documentación y guias que nos ayudaran en nuestro camino.

## Instalacion de Ollama por el shell de Linux:

Cabe recalcar que todo esto es posible gracias a Ollama, sin el no seriamos capaces de utilizar estas IAs de una manera tan sencilla como la presentan. Dentro de su pagina web hay una serie de pasos acerca de como usar Ollama en los distintos OS. 

En este caso usaremos el de Linux para asi usar a las IAs en la terminal o Bash, esto a traves de la siguiente linea de comando:

```
curl -fsSL https://ollama.com/install.sh | sh
```

## Servidor Ollama:
Comando para activar el servidor de Ollama: 
```
ollama serve
```

---
## Comandos para activar distintas IAs(LLM):

| IA | Comando |
| :-: | :-: |
|Comando para usar tinyllama: |```ollama run tinyllama```|
|Comando para usar llava: |```ollama run llava```|
|Comando para usar sqlcoder: |```ollama run sqlcoder```|


### Modo CHAT
Para usar el modo chat con cada una de las IAs basta con colocar alguno de los comandos anteriormente mencionados. 
>Para detenerlo control C u control D.


### Modo Generativo
Usar el modo generativo es otra manera de preguntarle a las IAs cosas, aunque es un poco mas complejo, puesto que comparandolo con el modo *CHAT* en el cual se prepara un entorno para poder hablar con la IA directamente _escribiendo en la bash como si hablaras con alguien en alguna red social_, el modo generativo es usado a traves de una serie de comandos que ya vienen descritos en la pagina de ***Ollama***.

Por ejemplo: 

```shell
curl http://127.0.0.1:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"How are you?",
  "stream": false
}'
```


### Guardar progreso en el Repositorio de Github

```shell
git add . (Revisa)
git commit -m "UPDATE README" (Etiqueta)
git push -u origin main (Actualiza)
```