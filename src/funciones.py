# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    resultado = []
    for elemento in lista:
        resultado.append(func(elemento))
    return resultado
    pass


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    def funcion_compuesta(x):
        return f(g(x))
    return funcion_compuesta
    pass


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}

    def cacheado (*args):
        if args in cache:
            return cache[args]
        
        resultado  = func(*args)
        cache[args] = resultado

        return resultado
    return cacheado
    pass


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
    NO uses functools.reduce
    """
    contador = inicial
    for valor in lista:
        contador = func(contador,valor)
    return contador
    pass
