print("1) Imprimir Hola Mundo!")
print("Hola Mundo!")

print("2) Pedir nombre y saludar")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

print("3) Pedir nombre, apellido, edad y lugar de residencia")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("4) Área y perímetro de un círculo")
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

print("5) Convertir segundos a horas")
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

print("6) Tabla de multiplicar")
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print("7) Operaciones con dos números") 
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

print("8) Índice de masa corporal")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.2f}")

print("9) Conversión Celsius a Fahrenheit")
celsius = float(input("Ingrese la temperatura en °C: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

print("10) Promedio de 3 números")
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio de los 3 números es: {promedio:.2f}")
