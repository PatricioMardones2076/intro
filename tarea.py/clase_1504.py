#Ciclos

#while (prueba) existe en todos los lenguajes

#1.- Inicializacion
#2.- While (mientras) condicion
    #mientras se cumpla la condicion
#3.- Incremento o decremento

#Ejemplo:
x = 0
#mientras se cumpla la condicion
#while x <= 10:
#    print(x)
#    x = x + 1

# El usuario debe ingresar hasta donde desea la serie, desplegar de 2 en 2
#num = int(input("Ingrese hasta donde desea la serie: "))
#x = 0
#while x <= num:
#    print(x)
#    x = x + 2

#print("Fin del programa")

# El usuario debe ingresar hasta desde donde desea la serie, desplegar de 2 en 2, donde ejemplo usuario: 5/4/3/2/1/0 fin del programa
#num = int(input("Ingrese desde donde desea la serie: "))
#x = num
#while x >= 0:
#    print(x)
#    x = x - 2
#print("Fin del programa")

# Desarrolle un programa que permita ingresar 1000 numeros al usuario, al terminar despliegue la suma de ellos.
suma = 0
contador = 1
while contador <= 1000:
    num = int(input("Ingrese un numero: "))
    suma = suma + num
    contador = contador + 1
print("La suma de los numeros ingresados es:", suma)

#Deben pedir al usuario hasta donde la serie / ej: si dice hasta el 10
serie_final= int(input("Ingrese hasta donde quiere que sea la serie: "))
#Debes pedir al usuario un numero, luego debes mostrar la serie de numeros pares desde el 0 hasta el numero ingresado por el usuario. Ej: si el usuario ingresa 10, se deben mostrar si los numeros ingresados son par o impar.
i = 1
numero_serie_final = int(input("Ingrese un numero: "))

while i <= numero_serie_final:
    if i % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")
    i = i + 1

print("Fin del programa")



