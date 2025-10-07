#Desafios de nivel 1

# Desafio 1 numeros duplicados
def eliminar_duplicados(lista):
    """Elimina los elementos duplicados de una lista manteniendo el orden."""
    unicos = []
    for elemento in lista:
        if elemento not in unicos:
            unicos.append(elemento)
    return unicos

# Ejemplo de uso
numeros = [1, 2, 2, 3, 4, 4, 5, 1, 6]
resultado = eliminar_duplicados(numeros)

print("Lista original:", numeros)
print("Lista sin duplicados:", resultado)

# Desafio 2 verificar si una cadena o número es un palíndromo.

def es_palindromo(valor):
    """Verifica si una cadena o número es palíndromo."""
    # Convertimos a cadena para manejar números y texto igual
    texto = str(valor)
    # Comparamos el texto con su versión invertida
    return texto == texto[::-1]


# Ejemplos de uso
print(es_palindromo("ana"))       # True
print(es_palindromo("reconocer")) # True
print(es_palindromo("python"))    # False
print(es_palindromo(12321))       # True
print(es_palindromo(12345))       # False

# Desafio valor maximo y minimo sin funciones integradas
def encontrar_max_min(lista):
    """Encuentra el valor máximo y mínimo de una lista sin usar max() o min()."""
    # Verificar que la lista no esté vacía
    if not lista:
        return None, None

    maximo = lista[0]
    minimo = lista[0]

    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento

    return maximo, minimo


# Ejemplo de uso
numeros = [5, 3, 8, 1, 9, -2, 7]

maximo, minimo = encontrar_max_min(numeros)

print("Lista:", numeros)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)

# Desafio tama;o de una cadena sin funcion integrada
def longitud_cadena(cadena):
    """Devuelve la longitud de una cadena sin usar len()."""
    contador = 0
    for _ in cadena:
        contador += 1
    return contador


# Ejemplo de uso
texto = "Hola mundo"
longitud = longitud_cadena(texto)

print(f"La cadena '{texto}' tiene {longitud} caracteres.")
