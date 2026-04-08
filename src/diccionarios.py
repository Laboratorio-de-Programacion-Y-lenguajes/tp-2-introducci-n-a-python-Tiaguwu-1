# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    Ejemplo: contar_palabras("hola mundo hola") -> {"hola": 2, "mundo": 1}
    Las palabras deben ser comparadas en minúsculas.
    """
    lista = {}
    for palabra in texto.split():
        palabra = palabra.lower()
        if palabra in lista:
            lista[palabra] += 1
        else:
            lista[palabra] = 1
    return lista
    pass


def invertir_diccionario(d: dict) -> dict:
    """
    Retorna un nuevo diccionario con claves y valores intercambiados.
    Ejemplo: invertir_diccionario({"a": 1}) -> {1: "a"}
    """
    invertido = {}
    for clave, valor in d.items():
        invertido [valor] = clave
    return invertido
    pass


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios. Si hay claves repetidas, prevalece d2.
    """
    union = d1.copy()
    union.update(d2)
    return union
    pass


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un nuevo diccionario con solo los pares
    cuyo valor sea >= minimo.
    """
    pares = {}
    for clave, valor in d.items():
        if valor >= minimo:
            pares[clave] = valor
    return pares
    pass
