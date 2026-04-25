#Desarrolle un programa que permita ingresar 10 numeros  y al finalizar, despligue cual es el mayor de ellos.
i = 1
resultado = int(input("Ingrese un número: "))
while i <= 9:
    numero = int(input("Ingrese un número: "))
    if numero > resultado:
        resultado = numero
    i = i + 1
print("El mayor de los números ingresados es:", resultado)
