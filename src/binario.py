# ------------------------------ 
# Script: binario.py 
# Descripción: De Binario a Decimal
# Autor: Francisco Javier Gutiérrez Pérez
# Fecha: 17/11/2025
# ------------------------------ 

binario = input("Introduce un número binario: ")

def esBinario(strbinario):
    """
    Verifica si una cadena representa un número binario válido.
    
    Parámetros:
        strbinario (str): Cadena que contiene el número binario.
    
    Retorna:
        bool: True si la cadena es un número binario válido, False en caso contrario.
    """
    es_zero_o_uno = True

    for i in range(len(strbinario)):
        if strbinario[i] != "0" and strbinario[i] != "1":
            es_zero_o_uno = False
    
    return es_zero_o_uno

def deBinarioaDecimal(strbinario):
    """
    Convierte una cadena que representa un número binario a decimal.

    Parámetros:
        strbinario (str): Cadena que contiene el número binario.

    Retorna:
        int: Valor decimal del número binario.
    """
    decimal = 0
    longitud = len(strbinario)

    for i in range(longitud):
        digito = int(strbinario[longitud - 1 - i])
        decimal += digito * (2 ** i)
    
    return decimal
