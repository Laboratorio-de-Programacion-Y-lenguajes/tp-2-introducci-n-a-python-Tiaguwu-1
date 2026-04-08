# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: Gemini

**Prompt usado**:
> Estoy haciendo un trabajo de inytoduccion a python de laboratorio de programacion y lenguajes, mi funcion :         case bool():
            return "bool"
me tira error en el testeo donde el error es:
FAILED tests/test_variables.py::test_tipo_de_dato_bool - AssertionError: assert 'int' == 'bool', que es lo que esta mal?

**Resultado obtenido**:
> El error que estás experimentando es un "clásico" de Python debido a cómo está diseñado el lenguaje internamente. El problema no es necesariamente tu lógica, sino una herencia histórica de Python: la clase bool es una subclase de int.
```
def identificar_tipo(valor):
    match valor:
        # El booleano debe ir PRIMERO
        case bool():
            return "bool"
        case int():
            return "int"
        case str():
            return "str"
        # ... otros tipos
```
**¿Lo usaste tal cual o lo modificaste?**

Si, hice el cambio que fue poner el case del boolean primero porque sino tomaba el boolean como un entero.

---

### 2 - condicionales.py

**Herramienta**: Gemini

**Prompt usado**:
> def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota:
    - nota >= 9: "Sobresaliente"
    - nota >= 7: "Bueno"
    - nota >= 6: "Aprobado"
    - nota < 6:  "Desaprobado"
    """
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"
    pass
esta funcion podria hacerlo con un match?

**Resultado obtenido**:
```
def clasificar_nota(nota: float) -> str:
    match nota:
        case n if n >= 9:
            return "Sobresaliente"
        case n if n >= 7:
            return "Bueno"
        case n if n >= 6:
            return "Aprobado"
        case _:
            return "Desaprobado"
```
>¿Es mejor usar match en este caso?
    Siendo honestos y directos: para este problema en particular, el if-elif-else suele ser preferible. Aquí te explico por qué:
    **Legibilidad:** El match-case con "guards" (if n >= 9) es un poco más ruidoso visualmente que un if tradicional para rangos numéricos simples.
    **Propósito:** El match brilla cuando necesitas desestructurar objetos complejos (listas, diccionarios o clases) o cuando comparas valores exactos (como vimos con los tipos de datos en tu consulta anterior). Para una escala numérica simple, el if es el estándar de la industria.
    **Rendimiento:** En este nivel, la diferencia es imperceptible, pero el match tiene una pequeña sobrecarga extra por cómo evalúa los patrones.

**¿Lo usaste tal cual o lo modificaste?**

No, los deje con los elif nomas ya que no era necesario.

---

### 3 - listas.py

**Herramienta**: Gemini

**Prompt usado**:
> def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    invertida = lista
    invertida.sort(reverse= True)
    return invertida
    pass
    por que no la invierte? cual es el error?

**Resultado obtenido**:
> En tu lógica, cuando el bucle encuentra que n (de la lista original) es igual a palabra (de la copia), ejecutas remove. El problema es que la primera vez que se comparan, son el mismo elemento.
Si tienes [1, 2, 1], cuando el bucle llega al primer 1, ve que 1 == 1 y lo elimina.
¡Al final terminas borrando todo o dejando la lista vacía/incompleta porque estás eliminando la primera aparición en lugar de la segunda!
Además, nunca debes eliminar elementos de una lista mientras la recorres (aunque sea una copia), ya que los índices se desplazan y el bucle se "salta" elementos.

```def eliminar_duplicados(lista: list) -> list:
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado
```

**¿Lo usaste tal cual o lo modificaste?**

Lo modifique porque tenia un error.

---

**Prompt usado**:
> def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    listapar = []
    aplanada = []
    for par in lista:
        listapar.copy(par)
        for n in listapar:
            aplanada.append(n)
    return aplanada
    pass 
y aca

**Resultado obtenido**: 
>En este caso, el error es técnico: el método .copy() de las listas no recibe argumentos.
En Python, lista.copy() se usa sin nada entre paréntesis para devolver una copia de la lista que lo llama. No sirve para "copiar el contenido de X dentro de Y". Al intentar listapar.copy(par), Python lanzará un TypeError.
Además, la variable listapar es redundante. Puedes iterar directamente sobre los elementos internos.

```
def aplanar_lista(lista: list) -> list:
    aplanada = []
    for sublista in lista:
        for elemento in sublista:
            aplanada.append(elemento)
    return aplanada
```

**¿Lo usaste tal cual o lo modificaste?**

Si, me ayudo a entenderlo y modifique mi error.

---

### 4 - diccionarios.py

**Herramienta**: Gemini

**Prompt usado**:
> def invertir_diccionario(d: dict) -> dict:
    """
    Retorna un nuevo diccionario con claves y valores intercambiados.
    Ejemplo: invertir_diccionario({"a": 1}) -> {1: "a"}
    """
    invertido = {}
    for clave, valor in d.items():
        invertido [valor] = clave
    return invertido
    pass
en el momento que recorre el for, cuando saca la clave y el valor, en el lugar del valor guarda la clave pero cuando guaarda el valor

**Resultado obtenido**:
> Entiendo perfectamente tu duda: parece que la información "desaparece" o que no se está guardando el valor original. Lo que sucede es que en un diccionario, el concepto de "valor" y "clave" es relativo a la posición que ocupan.
En tu código, el antiguo valor se convierte en la nueva clave. No es que se pierda, es que cambia de rol.
¿Qué está pasando línea por línea?
Imagina que d = {"a": 1}.
for clave, valor in d.items():
Python extrae "a" y la guarda en la variable clave.
Python extrae 1 y lo guarda en la variable valor.
invertido[valor] = clave
Aquí le estás diciendo a Python: "En el nuevo diccionario, busca el asiento llamado 1 (que era el valor) y sienta allí a "a" (que era la clave)".
Al final, cuando haces return invertido, obtienes {1: "a"}. El "1" ahora es quien manda (la clave) y "a" es la información asociada (el valor).

**¿Lo usaste tal cual o lo modificaste?**

Lo use para entender bien el par guardado en los diccionarios.

---

### 5 - loops.py

**Herramienta**: Gemini

**Prompt usado**:
> fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    a = 0
    b = 1
    lista = []
    for _ in range(n):
        list.append(a)
        a, b = b, a + b
    return lista
que esta mal


**Resultado obtenido**:
El error: list vs lista
En tu código, creaste una variable llamada lista, pero dentro del bucle intentas usar list.append(a).
list (en minúsculas y sin la "a") es el nombre de la clase o el tipo de dato en Python. Al intentar hacer list.append, Python se confunde porque le estás pidiendo a la "fábrica de listas" que guarde un número, en lugar de pedírselo a tu lista específica.
lista (con "a") es el nombre de tu variable.

**¿Lo usaste tal cual o lo modificaste?**

Si, en vez de poner lista, puse list.

---

### 6 - funciones.py

**Herramienta**: Gemini

**Prompt usado**:
> def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}
    
    pass
no entiendo

**Resultado obtenido**:
Este es uno de los conceptos más potentes de Python. La memoización consiste en crear una "memoria" para una función, de modo que si le pides algo que ya calculó antes, no pierda tiempo repitiendo el trabajo, sino que te dé la respuesta guardada.

Para resolverlo, necesitas usar un concepto llamado "Clausura" (Closure): una función dentro de otra que "recuerda" el diccionario cache.
```
def memoizar(func):
    cache = {}

    def envoltura(*args):
        # Si los argumentos ya están en el diccionario, retornamos el valor
        if args in cache:
            return cache[args]
        
        # Si no están, llamamos a la función original y guardamos el resultado
        resultado = func(*args)
        cache[args] = resultado
        return resultado

    return envoltura
```

**¿Lo usaste tal cual o lo modificaste?**

Si, lo use tal cual, ya que yo no entendia como hacerlo, me dio una explicacion bastante completa y como era.

---

### 7 - operaciones.py

**Herramienta**: Gemini

**Prompt usado**: 
> como dar vuelta un string

**Resultado obtenido**:
> El método del "Slicing" (La más rápida)
Esta es la forma estándar en Python. Utiliza la notación de corchetes [inicio:fin:paso]. Al poner -1 en el paso, le dices a Python que recorra el string hacia atrás.
```
texto = "Python"
invertido = texto[::-1]
print(invertido)  # Resultado: "nohtyP"
```

**¿Lo usaste tal cual o lo modificaste?**

Si, lo use tal cual, explicar la funcion basica para dar vuelta un String.

---

**Prompt usado**: 
> def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    
    pass

entiendo lo del desplazamiento en donde seguramente hay que usar codigo ascii para hacer el pasaje pero no se como hacaerlo

**Resultado obtenido**: Gemini ha dicho
El Cifrado César es un reto clásico de lógica porque requiere que el alfabeto sea "circular": si estás en la 'z' y te desplazas 1, debes volver a la 'a'.

Para resolverlo en Python sin complicarte con listas de letras, lo mejor es usar los códigos ASCII de los caracteres. Cada letra tiene un número asignado (por ejemplo, 'A' es 65).

La lógica del "Círculo"
La fórmula mágica para que el alfabeto dé la vuelta es el operador módulo (%).

ord(caracter): Convierte la letra en su número ASCII.

Restar la base: Si es mayúscula, restamos 65 (valor de 'A') para que 'A' sea 0, 'B' sea 1, etc.

Sumar el desplazamiento: Aplicamos el movimiento.

% 26: Esto asegura que si el resultado es 26, vuelva a 0 (vuelva a la 'A').

chr(...): Convierte el número de nuevo a letra.

```
def caesar_cipher(texto: str, desplazamiento: int) -> str:
    resultado = ""
    
    for caracter in texto:
        # 1. Si es mayúscula
        if 'A' <= caracter <= 'Z':
            # (Posicion 0-25 + desplazamiento) % 26 + base ASCII
            nuevo_codigo = (ord(caracter) - ord('A') + desplazamiento) % 26
            resultado += chr(nuevo_codigo + ord('A'))
            
        # 2. Si es minúscula
        elif 'a' <= caracter <= 'z':
            nuevo_codigo = (ord(caracter) - ord('a') + desplazamiento) % 26
            resultado += chr(nuevo_codigo + ord('a'))
            
        # 3. Si no es letra (espacios, números, puntos), se queda igual
        else:
            resultado += caracter
            
    return resultado
```

**¿Lo usaste tal cual o lo modificaste?**

Use el codigo tal cual, ya que no sabia como implementar el pasaje de las letras al codigo ascii y  viceverse para hacer el desplazamiento.

---


## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?

Aprendi bastante de la sintaxis de python, y el como razonar sus funciones o llamadas a variables, me dio un poco de complejidad al ser diferente a java pero con la IA y la pagina w3schools pude entender bastantes cosas.