"""
Ejercicio 4: Suite de tests con el módulo unittest.

Este archivo contiene los tests unitarios para las funciones 
de los ejercicios 2 y 3.
"""
import unittest
from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista

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

    # Pruebas para estaEnRango(valor, minimo, maximo)
    def test_estaEnRango_parametrizado(self):
        casos = [
            # dentro del rango (inclusivo)
            (1, 1, 20, True),
            (20, 1, 20, True),
            (10, 1, 20, True),
            # fuera del rango
            (0, 1, 20, False),
            (21, 1, 20, False),
            # rangos negativos
            (-5, -10, -1, True),
            (0, -10, -1, False),
            # minimo > maximo
            (5, 10, 1, False),
            # comparar float con int
            (5.0, 1, 10, True),
        ]
        for valor, minimo, maximo, esperado in casos:
            with self.subTest(valor=valor, minimo=minimo, maximo=maximo):
                self.assertEqual(estaEnRango(valor, minimo, maximo), esperado)

    def test_estaEnRango_tipos_invalidos_lanzan_TypeError(self):
        casos_invalidos = [
            (None, 1, 10),     # None no es comparable con int
            ("5", 1, 10),     # string e int
            (5, "1", 10),     # minimo string
            (5, 1, "10"),     # maximo string
        ]
        for valor, minimo, maximo in casos_invalidos:
            with self.subTest(valor=valor, minimo=minimo, maximo=maximo):
                with self.assertRaises(TypeError):
                    estaEnRango(valor, minimo, maximo)

    # Pruebas para estaEnLista(valor, lista)
    def test_estaEnLista_parametrizado(self):
        casos = [
            # presentes / ausentes
            (3, [1, 2, 3], True),
            (4, [1, 2, 3], False),
            # strings
            ("a", ["a", "b"], True),
            ("a", ["A", "b"], False),
            # booleanos e igualdad con enteros
            (True, [True, False], True),
            (1, [True, False], True),   # True == 1 → True
            (0, [False], True),         # False == 0 → True
            # None y lista vacía
            (None, [None, 0], True),
            (5, [], False),
            # tipos distintos no son iguales
            ("5", [5], False),
            # duplicados
            (2, [1, 2, 2, 3], True),
        ]
        for valor, lista, esperado in casos:
            with self.subTest(valor=valor, lista=lista):
                self.assertEqual(estaEnLista(valor, lista), esperado)
"""
Para lanzar los tests ejecutar:
python -m unittest discover tests -v
(Desde la carpeta raíz del proyecto)
"""
