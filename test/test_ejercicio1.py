import pytest

from src.ejercicio1 import facturar_compras

compras = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

informaciónEsperada = facturar_compras(compras)

def test_generar_informacion_compras():

    # Verifica que cada línea obtenida de la función facturar_compras() está presente en el resultado actual
    for lineaEsperada in informaciónEsperada.split('\n'):
        assert lineaEsperada in facturar_compras(compras)
