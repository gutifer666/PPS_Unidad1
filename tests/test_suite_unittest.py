"""
Ejercicio 4: Suite de tests con el módulo unittest.

Este archivo contiene los tests unitarios para las funciones 
de los ejercicios 2 y 3.
"""
import unittest
from src.binario import esBinario

class TestSuitUnitTest(unittest.TestCase):

    # Pruebas para esBinario() parametrizado
    def test_esBinario(self):
        casos_de_prueba = {
            "101010": True,
            "0000": True,
            "1111": True,
            "10201": False,
            "abcde": False,
            "2": False,
            "01a01": False,
            "": True,  # Cadena vacía, se considera válida
            " ": False, # Espacio en blanco se considera inválido
            "01" * 1000000: True,
            "\n1010": False,
            "101ó0": False,
            "💡": False,
        }

        for entrada, esperado in casos_de_prueba.items():
            with self.subTest(entrada=entrada):
                self.assertEqual(esBinario(entrada), esperado)

    def test_si_pasamos_un_entero_como_argumento_se_lanza_una_excepcion(self):
        strbinario = 1010
        with self.assertRaises(TypeError):
            esBinario(strbinario)

"""
Para lanzar los tests ejecutar:
python -m unittest discover tests -v
(Desde la carpeta raíz del proyecto)
"""
