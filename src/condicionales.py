# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"
    pass


def mayor_de_tres(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    pass


def clasificar_nota(nota: float) -> str:
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"
    pass


def es_bisiesto(anio: int) -> bool:
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False
    pass
