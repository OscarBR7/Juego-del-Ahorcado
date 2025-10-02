#Elegir palabra al azar
#Mostrar por guiones la cantidad de letras de nuestra palabra
#Pedir letra al usuario
#No es valida, volver a pedirle al usuario que ingrese una letra
#No se encuentra dentro de la palabra, agregar a una lista de letras incorrectas,
#descuenta una vida, muestra el número de vidas
#Se terminaron las vidas, fin del juego
#No se han terminado, siguiente letra
#La letra es correcta, reemplazar el guión por la letra
#Se ha completado la letra
#no, pedir una letra más
# si, fin del juego

from random import * 
def elegir_palabra ():
  lista_de_palabras = [
    'hola',
    'puerco',
    'manzana',
    'perro',
    'naranja',
    'azul',
    'mar',
    'lechuga',
    'tomate',
    'sopa',
    'crema',
    'pollo'
  ]
  palabra_elegida = choice(lista_de_palabras)
  return palabra_elegida

def mostrar_palara (palabra):
  guiones= len(palabra)
  caracter = '-'
  palabra_mostrada = [guiones*caracter]
  print(palabra_mostrada)

def pedir_letra_usuario ():
  alfabeto = [
    'a','b','c','d','e','f','g','h',
    'i','j','k','l','m','n','ñ','o',
    'p','q','r','s','t','u','v','w',
    'x','y','z'
  ]
  letra = input("Ingrese la letra de la palabra: ")
  while letra not in alfabeto:
    letra = input("Ingrese una letra valida: ")
  else: 
    return letra

def buscar_letra_en_palabra (palabra):
  vidas = 5
  letra_auxiliar = ''
  lista_palabras = ['-']*len(palabra)
  lista_letras_incorrectas = []
  while vidas > 0 :
    print(lista_palabras)
    letra_recibida = pedir_letra_usuario()
    letra_auxiliar = letra_recibida
    if(letra_auxiliar in palabra):
      for indice,letra in enumerate(palabra):
        if(letra_auxiliar == letra):
          lista_palabras[indice] = letra
        if("".join(lista_palabras) == palabra):
          return("Felicidades has adivinado!!"+palabra)
    else:
      lista_letras_incorrectas.append(letra_auxiliar)
      vidas-=1
      print(f"La letra no se encuentra dentro de la palara, te quedan {vidas} vidas")
  return (f"Lo siento has, perdido todas tus vidas, la palabra era {palabra}", lista_letras_incorrectas)


palabra = elegir_palabra()
print(buscar_letra_en_palabra(palabra))
