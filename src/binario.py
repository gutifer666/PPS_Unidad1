"""
binario.py
Programa que pide al usuario que introduzca un número binario e imprime por pantalla el número en formato decimal
Ultima Modificación. 29/11/2025
Autor. Francisco Javier Gutiérrez Pérez
Dependencias: Ninguna
"""

def esBinario(strbinario):
    """
    Verifica si una cadena representa un número binario válido.
    Parámetros: strbinario (str): Cadena que contiene el número binario.
    Retorna: bool: True si la cadena es un número binario válido, False en caso contrario.
    """

    # La función all() devuelve True si todos los elementos de una secuencia son verdaderos
    return all(char in "01" for char in strbinario)

def ejecutarApp():
    binario = input("Introduce un número binario: ")

    if not esBinario(binario):
        print("La cadena introducida no es un número binario válido")
        return

    # Convierte el número binario a decimal utilizando la función int() con base 2
    decimal = int(binario, 2)

    print(f"El número binario {binario} en decimal es {decimal}")

# Para que los tests puedan lanzarse sin ejecutar el programa
if __name__ == "__main__":
    ejecutarApp()