print("Ejercicio 1")
edad=int(input("Ingrese su edad: "))
if edad>=18:
    print("Es mayor de edad")
elif edad<18 and edad>0:
    print("Es menor de edad")
else:
    print("Edad invalida")
print("\nEjercicio 2")
nota=int(input("Ingrese la nota: "))
if nota>=6:
    print("Aprobado")
elif nota<6 and nota>=0:
    print("Desaprobado")
else:
    print("Nota invalida")
print("\nEjercicio 3")
numero=int(input("Ingrese un numero par: "))
if numero%2==0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")
print("\nEjercicio 4")
edad=int(input("Ingrese su edad: "))
if edad>=0 and edad<12:
    print("Es un niño/a")
elif edad>=12 and edad<18:
    print("Es adolescente")
elif edad>=18 and edad<30:
    print("Es adulto/a joven")
elif edad>=30:
    print("Es adulto")
else:
    print("Edad invalida")
print("\nEjercicio 5")
contrasenia=input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(contrasenia)>=8 and len(contrasenia)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("\nEjercicio 6")
import random
numeros_aleatorios=[random.randint(1,100) for i in range(50)]
from statistics import mode, median, mean
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
print("Lista de numeros: ", numeros_aleatorios)
print("Moda: ", moda)
print("Meidana: ", mediana)
print("Media: ", media)
if media>mediana and mediana>moda:
    print("Sesgo positivo")
elif media<mediana and mediana<moda:
    print("Sesgo negativo")
elif media==mediana==moda:
    print("Sin sesgo")
print("\nEjercicio 7")
texto=input("Ingrese una frase o palabra: ")
if texto.lower().endswith(("a", "e", "i", "o", "u")):
    print(texto+"!")
else:
    print(texto)
print("\nEjercicio 8")
nombre=input("Ingrese su nombre: ")
opcion=(input("Elija una opcion:\n1. Si quierre su nombre en mayusculas. Por ejemplo: PEDRO\n2. Si quiere su nombre en minusculas. Por ejemplo: pedro\n3. Si quiere su nombre con la primera letra mayuscula. Por ejemplo: Pedro\nIngrese 1, 2 o 3: "))
if opcion=="1":
    print("Su nombre es:",nombre.upper())
elif opcion=="2":
    print("Su nombre es:",nombre.lower())
elif opcion=="3":
    print("Su nombre es:",nombre.title())
else:
    print("La opcion que ingreso no es valida")
print("\nEjercicio 9")
magnitud=float(input("ingrese la magnitud del terremoto: "))
if magnitud<3 and magnitud>0:
    print("Muy leve (imperceptible)")
elif magnitud>=3 and magnitud<4:
    print("Leve (ligeramente perceptible)")
elif magnitud>=4 and magnitud<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud>=5 and magnitud<6:
    print("Fuerte (puede causar daño a estructuras débiles)")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud >=7 and magnitud<10:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("no es una entrada valida")
print("\nEjercicio 10")
ubi=input("En que hemisferio se encuentra (S/N): ")
mes=int(input("Ingrese el mes (1-12): "))
dia=int(input("Ingrese el dia del mes: "))
if ubi=="N":
    if (mes==3 and dia>=21) or (mes in [4,5]) or (mes==6 and dia <=20):
        print("Te encuentras en primavera")
    elif (mes==6 and dia>=21) or (mes in [7,8]) or (mes==9 and dia <=20):
        print("Te encuentras en verano")
    elif (mes==9 and dia>=21) or (mes in [10,11]) or (mes==12 and dia <=20):
        print("Te encuentras en otoño")
    else:
        print("Te encuentras en invierno")
elif ubi=="S":
    if (mes==3 and dia>=21) or (mes in [4,5]) or (mes==6 and dia <=20):
        print("Te encuentras en otoño")
    elif (mes==6 and dia>=21) or (mes in [7,8]) or (mes==9 and dia <=20):
        print("Te encuentras en invierno")
    elif (mes==9 and dia>=21) or (mes in [10,11]) or (mes==12 and dia <=20):
        print("Te encuentras en primavera")
    else:
        print("Te encuentras en verano")
else:
    print("Hemisferio invalido") 