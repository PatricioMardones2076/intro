#Realizar un programa que solicite ingresar 3 valores enteros y luego muestrelos siempre negativos.
val1 = int(input("Ingresar primer valor: "))
val2 = int(input("Ingresar segundo valor: "))
val3 = int(input("Ingresar tercer valor: "))    
if val1 > 0:
    print("El primer valor ahora es:", -val1)
if val2 > 0:
    print("El segundo valor ahora es:", -val2)
if val3 > 0:
    print("El tercer valor ahora es:", -val3)

#Desarrolle un programa que permita ingresar un numero, si es negativo, debemos enviar un mensaje al usuario "Numero invalido, reingrese" y debe volver a ingresar otro numero, si es positivo, se debe mostrar el mensaje "Numero correcto " y termina el programa.
num = int(input("Ingrese un numero: "))
if num < 0:
    print("Numero invalido, reingrese")
    num = int(input("Ingrese un numero: "))
if num > 0:
    print("Numero correcto")

#Desarrolle un programa que permita ingresar la estatura y peso, si aldividir el peso por la estatura al cuadrado el valor es menor a 25 desplegaremos por pantalla "Peso normal", si el valor es mayor a 25 desplegaremos por pantalla "Peso normal" y si el valor sobrepasa los 25 mostraremos "Sobrepeso".
estatura = float(input("Ingrese la estatura en metros: "))
peso = float(input("Ingrese el peso en kilogramos: "))

imc = peso / (estatura * estatura)

if imc < 25:
    print("Peso normal")

if imc > 25:
    print("Sobrepeso")


