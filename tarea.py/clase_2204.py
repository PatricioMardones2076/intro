#Desarrolle un programa que permita ingresar 10 numeros positivos , si el usuario ingresa un numero negativo mostramos el error al ingreso "ERROR", al finalizar debemos entregar la suma de todos los numeros ingresados.
i = 1
resultado = 0
while i <= 10:
    numero = int(input("Ingrese un número positivo: "))
    if numero < 0:
        print("ERROR: El número ingresado es negativo.")
    else:
        resultado = resultado + numero
        i = i + 1
print("La suma de los números ingresados es:", resultado)