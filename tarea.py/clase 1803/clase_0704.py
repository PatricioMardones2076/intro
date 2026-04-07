#Desarrolle un programa que permita ingresar la edad del usuario y despliegue si es mayor o menor de edad (edad maxima 130)
edad = int (input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")

    if edad >= 130:
        print("Edad no valida, INGRESE SU EDAD REAL")

else: print("Usted es menor de edad")

#Leer cuento chino "Buena suerte Mala suerte"