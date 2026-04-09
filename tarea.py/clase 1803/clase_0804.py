#Despliegue un sistema que permita ingresar 2 numeros si el primero es mayor que el segundo, despliegue la resta de ellos si no la multiplicacion

primer_num = int(input("Ingrese el primer numero:"))
segundo_num = int(input("Ingrese el segundo numero:"))

if primer_num > segundo_num:
    resta = primer_num - segundo_num
    print("La resta de los numeros es:", resta)

if primer_num == segundo_num:
        print("ERROR...Los numeros son iguales, por favor ingrese numeros de distinto valor cada uno")

if primer_num < segundo_num:
    multiplicacion = primer_num * segundo_num
    print("La multiplicacion de los numeros es:", multiplicacion)
