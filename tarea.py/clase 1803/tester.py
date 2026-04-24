#Desarrolle un programa que permita ingresar 10 numeros  y al finalizar, despligue cual es el mayor de ellos.
#i = 1
#resultado = int(input("Ingrese un número: "))
#while i <= 9:
#    numero = int(input("Ingrese un número: "))
#    if numero > resultado:
#        resultado = numero
#    i = i + 1
#print("El mayor de los números ingresados es:", resultado)


cont = 1
n = 0
suma = 0
while cont <= 10:
    n = int(input("Ingrese número ["+str(cont)+" de 10]: "))
    if cont == 1:
       if n > 0:
          suma = n
       else:
        print("ERROR: El número ingresado es invalido.")
        cont = cont - 1
    
    else:
        if n > 0:
            suma = suma + n
        else:
            print("ERROR: El número ingresado es invalido.")
            cont = cont - 1
    cont = cont + 1
print("La suma de los números ingresados es: ", suma)