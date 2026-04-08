# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    suma = 0
    for n in numeros:
        suma = suma + n
    return suma
    pass


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    pares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares
    pass


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    invertida = lista.copy()
    invertida.reverse()
    return invertida
    pass


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    duplicados = []
    for elemento in lista:
        if elemento not in duplicados:
            duplicados.append(elemento)
    return duplicados
    pass


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    listapar = []
    aplanada = []
    for par in lista:
        for n in par:
            aplanada.append(n)
    return aplanada
    pass
