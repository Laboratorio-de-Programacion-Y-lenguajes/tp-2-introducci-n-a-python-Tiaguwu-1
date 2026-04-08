# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================
# Completá cada función siguiendo las instrucciones.
# NO modifiques los nombres de las funciones ni sus parámetros.
# ============================================================


def crear_saludo(nombre: str) -> str:
    return f"Hola, {nombre}!"
    pass


def suma_enteros(a: int, b: int) -> int:
    return a + b
    pass


def es_mayor_de_edad(edad: int) -> bool:
    return edad >=18
    pass


def tipo_de_dato(valor) -> str:
    match (valor):
        case bool():
            return "bool"
        case int():
            return "int"
        case str():
            return "str"
        case float():
            return "float"
    pass


def convertir_a_float(valor: str) -> float:
    return float(valor)
    pass
