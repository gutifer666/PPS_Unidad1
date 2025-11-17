# ------------------------------ 
# Script: binario.py 
# Descripción: De Binario a Decimal
# Autor: Francisco Javier Gutiérrez Pérez
# Fecha: 17/11/2025
# ------------------------------ 

binario = input("Introduce un número binario: ")

def esBinario(strbinario):
    
    es_zero_o_uno = True

    for i in range(len(strbinario)):
        if strbinario[i] != "0" and strbinario[i] != "1":
            es_zero_o_uno = False
    
    return es_zero_o_uno

print(esBinario(binario))
