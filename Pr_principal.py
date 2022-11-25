import os
from os import system
import Adivina_un_numero

def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 + " Bienvenido a la presentación del TPI de laboratorio " + '*' * 5)
    print('*' * 50)
    print('\n')


    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print('''
        [1] - Adivina un número
        [2] - Juego del ahorcado
        [3] - Papel Tijera
        [4] - Salir del programa''')
        eleccion_menu = input()

    return int(eleccion_menu)


juego=inicio()
if juego == 1:
    Adivina_un_numero.adivinanro()
elif juego == 2:
    Adivina_un_numero.adivinanro()


while inicio()==1:
    if juego==1:
         Adivina_un_numero.adivinanro()
    elif  juego==2:
      Adivina_un_numero.adivinanro()


