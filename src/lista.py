"""
lista.py
Programa que reciba un número del 1 al 20 introducido por el usuario
y compruebe si está dentro de la siguiente lista: [6,14,11,3,2,1,15,19]
Ultima Modificación. 29/11/2025
Autor. Francisco Javier Gutiérrez Pérez
Dependencias: Ninguna
"""

def estaEnRango(valor, minimo, maximo):
    # Devuelve True si valor está entre minimo y maximo (ambos inclusive).
    return minimo <= valor <= maximo


def estaEnLista(valor, lista):
    # Devuelve True si valor está contenido en la lista.
    return valor in lista


def pedir_entero(mensaje):
    # Pide un entero por consola, repitiendo hasta que el usuario introduzca un número válido.
    while True:
        try:
            entrada = input(mensaje).strip()
            return int(entrada)
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")


def ejecutarApp():
    numeros = [6, 14, 11, 3, 2, 1, 15, 19]
    minimo = 1
    maximo = 20

    numero = pedir_entero(f"Introduce un número del {minimo} al {maximo}: ")

    if not estaEnRango(numero, minimo, maximo):
        print(f"El número {numero} NO está en el rango [{minimo}, {maximo}].")
        return

    if estaEnLista(numero, numeros):
        print(f"El número {numero} está dentro de la lista {numeros}.")
    else:
        print(f"El número {numero} NO está dentro de la lista {numeros}.")


if __name__ == "__main__":
    ejecutarApp()