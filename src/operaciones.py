# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    texto_limpio = texto.lower().replace(" ","")
    invertido = texto_limpio[::-1]
    return invertido == texto_limpio
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    capitalizada = ""
    for palabra in texto.split():
        capitalizada += palabra.capitalize() + " "
    return capitalizada.strip()
    pass


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    contador = 0
    vocales = "aeiou"

    for caracter in texto.lower():
        if caracter in vocales:
            contador += 1
    return contador
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
def caesar_cipher(texto: str, desplazamiento: int) -> str:
    resultado = ""
    
    for caracter in texto:
        if 'A' <= caracter <= 'Z':
            nuevo_codigo = (ord(caracter) - ord('A') + desplazamiento) % 26
            resultado += chr(nuevo_codigo + ord('A'))
            
        elif 'a' <= caracter <= 'z':
            nuevo_codigo = (ord(caracter) - ord('a') + desplazamiento) % 26
            resultado += chr(nuevo_codigo + ord('a'))
            
        else:
            resultado += caracter
            
    return resultado
    pass
