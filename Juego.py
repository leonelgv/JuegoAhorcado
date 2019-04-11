from random import *

# Declarar palabras para jugar
palabrasJuego = ["p,e,r,r,o", "a,r,b,o,l", "b,a,l,o,n", "t,r,i,a,n,g,u,l,o", "c,a,s,a", "e,d,i,f,i,c,i,o"]

# Define el número de palabras para jugar
elemento = randrange(len(palabrasJuego)-1)

# Divide una palabra, al azar, en letras
palabra = palabrasJuego[5].split(",")

# Definir numero de pistas
pistas = 0
print ("numero de letras de la palabra: ", len(palabra))
if (len(palabra) > 1 and (len(palabra) <= 5)):
    pistas = 1
if (len(palabra) > 5 and (len(palabra) <= 10)):
    pistas = 2
if (len(palabra) > 10 and (len(palabra) <= 15)):
    pistas = 3
if (len(palabra) > 15):
    pistas = 4

print ("numero de pistas: ", pistas)
elementoPalabra = randrange(len(palabra)-1)
try:
    print (palabra[elementoPalabra])
except IndexError:
    print ("No existe el índice")