print("\n===== EJERCICIO 1: Factorial recursivo =====\n")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Ingrese un número para calcular los factoriales desde 1 hasta ese número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")


print("\n===== EJERCICIO 2: Serie de Fibonacci =====\n")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese hasta qué posición mostrar la serie de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(num + 1):
    print(fibonacci(i), end=" ")

print()  # salto de línea


print("\n===== EJERCICIO 3: Potencia recursiva =====\n")

def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)

base = int(input("Base: "))
exp = int(input("Exponente: "))
print(f"{base}^{exp} =", potencia(base, exp))


print("\n===== EJERCICIO 4: Decimal a Binario =====\n")

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(num)

print("Binario:", binario if binario != "" else "0")


print("\n===== EJERCICIO 5: Palíndromo recursivo =====\n")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra para verificar si es palíndromo: ")
print("¿Es palíndromo?:", es_palindromo(texto))


print("\n===== EJERCICIO 6: Suma de dígitos =====\n")

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(num))


print("\n===== EJERCICIO 7: Contar bloques en pirámide =====\n")

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Ingrese bloques del nivel más bajo: "))
print("Bloques totales necesarios:", contar_bloques(niveles))


print("\n===== EJERCICIO 8: Contar dígito dentro de un número =====\n")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("Número: "))
d = int(input("Dígito a buscar (0-9): "))
print("Cantidad de apariciones:", contar_digito(num, d))