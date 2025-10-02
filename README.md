# Juego del Ahorcado en Python

Este proyecto implementa el **juego del ahorcado** en Python.  
El programa selecciona una palabra al azar de una lista y el jugador debe adivinarla letra por letra antes de quedarse sin vidas.  

---

## Tecnologías utilizadas

- **Python 3**  
- Librería estándar de Python (`random`) para seleccionar palabras al azar  
- Entrada y salida por consola (función `input` y `print`)  

---

## Estructura del proyecto

```
PROYECTO-AHORCADO
│
├── ahorcado.py         # Código principal del juego
└── README.md           # Este archivo de documentación
```

---

## Instalación

1. Asegúrate de tener instalado **Python 3.x**.  
   Puedes descargarlo desde:  
   https://www.python.org/downloads/

2. Descarga el archivo `ahorcado.py` en tu computadora.  

3. Abre una terminal en la carpeta donde se encuentra el archivo.  

---

## Ejecución

En la terminal, escribe el siguiente comando:

```
python ahorcado.py
```

(o en algunos entornos también funciona con `py ahorcado.py`).

---

## Funcionamiento del juego

1. El programa elige al azar una palabra de una lista predefinida.  
2. Se muestra al jugador una serie de guiones que representan cada letra de la palabra.  
3. El jugador ingresa letras una por una:  
   - Si la letra está en la palabra, se reemplaza en los guiones.  
   - Si la letra no está en la palabra, se descuenta una vida y se agrega a la lista de letras incorrectas.  
4. El jugador empieza con **5 vidas**.  
   - Si se queda sin vidas → pierde el juego y se muestra la palabra correcta.  
   - Si adivina todas las letras → gana el juego.  

---

## Ejemplo de ejecución

```
['-', '-', '-', '-', '-']
Ingrese la letra de la palabra: a
['-', 'a', '-', '-', '-']
Ingrese la letra de la palabra: z
La letra no se encuentra dentro de la palabra, te quedan 4 vidas
['-', 'a', '-', '-', '-']
```

---

## Mejoras posibles

- Añadir un dibujo visual del ahorcado paso a paso.  
- Ampliar la lista de palabras o cargar palabras desde un archivo externo.  
- Manejar mayúsculas y minúsculas automáticamente.  
- Agregar la opción de jugar múltiples rondas.  

---

## Autor
Oscar Briones 