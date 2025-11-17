# PPS_Unidad1

2. Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
introduzca un número binario e imprima por pantalla el número en formato decimal.
Para desarrollar el programa, es necesario que desarrolles una función con la
siguiente cabecera:
def esBinario(strbinario) 

## Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
como parámetro contiene una cadena binaria.

## Ejemplo de esBinario:
print(esBinario(“1001”))
True
print(esBinario(“Hola”))
False

3. Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
cabeceras:

def estaEnRango(valor, minimo, maximo)
## Devuelve True o False determinando que valor se encuentra entre el mínimo y el
máximo.

def estaEnLista(valor, lista)
## Devuelve True o False determinando si el valor está en la lista.

4. Crea una suite de tests mediante UnitTest que comprueben las 3 funciones que has
desarrollado en los ejercicios anteriores. Procura que los tests unitarios cubran lo
mejor posible la aparición de comportamientos no deseados.

5. Realiza el ejercicio 4 pero utilizando esta vez cualquier otro framework de terceros
como por ejemplo pytest.

## Estructura de archivos

PPS_Unidad1/
├── src/
│   ├── __init__.py
│   ├── binario.py          <-- Script del Ejercicio 2 
│   ├── lista.py            <-- Script del Ejercicio 3 
│   ├── funciones_check.py  <-- Las 3 funciones (para testearlas)
│
├── tests/
│   ├── __init__.py
│   ├── test_suite_unittest.py  <-- Ejercicio 4 
│   └── test_suite_pytest.py    <-- Ejercicio 5 
│
├── .venv/
├── .gitignore
├── requirements.txt
└── README.md