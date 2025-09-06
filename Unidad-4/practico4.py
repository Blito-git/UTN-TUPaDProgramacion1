print("Ejercicio 1")
for i in range(101):
    print(i)
print("\nEjercicio 2")
numero=input("Ingrese un numero entero: ")
print("El numero contiene", len(numero),"digitos")
print("\nEjercicio 3")
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
suma=0
for i in range(min(numero1,numero2)+1,max(numero1,numero2)):
    suma+=i
print("El resultado de la suma es:",suma)
print("\nEjercicio 4")
suma=0
numero=1
while numero != 0:
    numero=int(input("Ingrese un numero\n0 para terminar\n---> "))
    if numero != 0:
        suma+=numero
print("El resultado de la suma es:",suma)
print("\nEjercicio 5")
import random
secreto=random.randint(0,9)
intentos=0
adivinado=False
while not adivinado:
    numero=int(input("Adivina el numero (0-9): "))
    intentos+=1
    if numero==secreto:
        adivinado=True
print(f"Acertaste en {intentos} intentos")
print("\nEjercicio 6")
for i in range(100,-1,-2):
    print(i)
print("\nEjercicio 7")
numero=int(input("Ingrese un numero: "))
suma=0
for i in range(numero + 1):
    suma+=i
print("El resultado de la suma es:",suma)
print("\nEjercicio 8")
pares=0
impares=0
positivos=0
negativos=0
entrada=0
while entrada<5:
    numero=int(input("Ingrese un numero: "))
    entrada+=1
    if numero%2==0:
        pares+=1
    if numero%2!=0:
        impares+=1
    if numero>0:
        positivos+=1
    if numero<0:
        negativos+=1
print(f"La cantidad de numeros pares es:{pares}\nLa cantidad de numeros impares es:{impares}\nLa cantidad de numeros positivos es:{positivos}\nLa cantidad de numeros negativos es:{negativos}")
print("\nEjercicio 9")
total=0
cantidad=int(input("Ingrese la cantidad de numero que desea ingresar: "))
for i in range(cantidad):
    numero=int(input(f"Ingrese el {i+1}º numero: "))
    total+=numero
media=total/cantidad
print("La media es:",media)
print("\nEjercicio 10")
numero=input("Ingrese un numero: ")
invertido=numero[::-1]
print("Numero invertido:",invertido)