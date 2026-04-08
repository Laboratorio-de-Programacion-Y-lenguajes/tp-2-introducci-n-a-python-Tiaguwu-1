# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    lista = []
    for i in range (1, n+1):
        lista.append(i)
    return lista
    pass


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    multiplos = []
    for i in range (1, 11):
        multiplos.append(i * n)
    return multiplos
    pass


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    resultado = 0
    while n > 0:
        resultado += n % 10
        n //= 10
    return resultado
    pass


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
    pass


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    a = 0
    b = 1
    lista = []
    for _ in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista
    pass
