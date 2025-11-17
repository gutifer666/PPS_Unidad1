"""
Ejercicio 4: Suite de tests con el módulo unittest.

Este archivo contiene los tests unitarios para las funciones 
de los ejercicios 2 y 3.
"""
import unittest
from src.binario import esBinario, deBinarioaDecimal

class TestSuitUnitTest(unittest.TestCase):

    # Pruebas para esBinario

    def test_esBinario_casos_validos(self):
        
        self.assertTrue(esBinario("1001")) # Ejemplo del enunciado
        self.assertTrue(esBinario("111111"))
        self.assertTrue(esBinario("000000"))
        self.assertTrue(esBinario("1"))
        self.assertTrue(esBinario("0"))
        self.assertTrue(esBinario("1010101010"))
    
    def test_esBinario_casos_invalidos(self):

        self.assertFalse(esBinario("Hola"))  # Ejemplo del enunciado
        self.assertFalse(esBinario("1021"))
        self.assertFalse(esBinario("10 10")) # Con un espacio
        self.assertFalse(esBinario("abc"))
        self.assertFalse(esBinario("1.0")) # Con un punto
        self.assertFalse(esBinario("101a"))

if __name__ == "__main__":
    """
    Ejecutar el archivo con: python -m unittest discover tests -v
    (Desde la carpeta raíz del proyecto)
    """
    unittest.main()