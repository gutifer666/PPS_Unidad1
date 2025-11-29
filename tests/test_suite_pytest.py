"""
Ejercicio 5: Suite de tests con el módulo pytest.

Este archivo contiene los tests unitarios para las funciones
de los ejercicios 2 y 3.
"""
import pytest
from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista

# --- Tests para esBinario() ---
@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("101010", True),
        ("0000", True),
        ("1111", True),
        ("10201", False),
        ("abcde", False),
        ("2", False),
        ("01a01", False),
        ("", True),          # Cadena vacía, se considera válida
        (" ", False),        # Espacio en blanco se considera inválido
        ("01" * 1_000_000, True),
        ("\n1010", False),
        ("101ó0", False),
        ("💡", False),
    ],
)
def test_esBinario_parametrizado(entrada, esperado):
    assert esBinario(entrada) == esperado


def test_esBinario_lanza_TypeError_si_argumento_no_es_str():
    strbinario = 1010
    with pytest.raises(TypeError):
        esBinario(strbinario)


# --- Tests para estaEnRango(valor, minimo, maximo) ---
@pytest.mark.parametrize(
    "valor, minimo, maximo, esperado",
    [
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
    ],
)
def test_estaEnRango_parametrizado(valor, minimo, maximo, esperado):
    assert estaEnRango(valor, minimo, maximo) == esperado


@pytest.mark.parametrize(
    "valor, minimo, maximo",
    [
        (None, 1, 10),   # None no es comparable con int
        ("5", 1, 10),   # string e int
        (5, "1", 10),   # minimo string
        (5, 1, "10"),   # maximo string
    ],
)
def test_estaEnRango_tipos_invalidos_lanzan_TypeError(valor, minimo, maximo):
    with pytest.raises(TypeError):
        estaEnRango(valor, minimo, maximo)


# --- Tests para estaEnLista(valor, lista) ---
@pytest.mark.parametrize(
    "valor, lista, esperado",
    [
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
    ],
)
def test_estaEnLista_parametrizado(valor, lista, esperado):
    assert estaEnLista(valor, lista) == esperado

"""
Para lanzar los tests ejecutar:
pytest -p
pytest -vv
(Desde la carpeta raíz del proyecto)
"""