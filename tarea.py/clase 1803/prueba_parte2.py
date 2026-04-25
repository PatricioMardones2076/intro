#Desarrolle un programa que solicite hasta donde desea la serie el usuario.
#El número que ingrese el usuario debe ser mayor a 5.

#Ejemplo.
#Hasta donde desea la serie: 10
#1+2-3+4-5+6-7+8-9+10=7
numero = int(input("Hasta donde debe ser la serie: "))
while numero <= 5:
    print("El número debe ser mayor a 5. Intente nuevamente, por favor.")
    numero = int(input("Hasta donde debe ser la serie: "))
resultado = 0
i = 1
while i <= numero:
    if i % 2 == 0:
        resultado = resultado + i
    else:
        resultado = resultado - i
    i = i + 1
print("El resultado de la serie es:", resultado)
