#Entrada
nom = input ("Inserte nombre")
especie = input ("Inserte especie")
peso = input ("Inserte peso")
edad = input ("Inserte edad")
vacuna = input ("Ingrese si esta vacunado o no")

#Salida
print( "Usted posee un perro llamado", nom, "que es de la especie", especie, "el cual pesa", peso, "tiene una una edad de", edad, "ademas de que", vacuna)

#Entrada
nom = input ("Inserte nombre")
especie = input ("Inserte especie")
peso = input ("Inserte peso")
edad = input ("Inserte edad")
vacuna = input ("Ingrese si esta vacunado o no")

#Salida
print (f"Usted posee un perro llamado {nom} que es de la especie {especie} el cual pesa {peso}, tiene una una edad de {edad}, ademas de que {vacuna}")

#Ejericio 2
#Entrada
nom = input ("Inserte nombre")
edad = input ("Inserte edad")
nacimiento = input ("inserte fecha de nacimiento")

#Salida
print(f"Su nombre es {nom}" , f"tiene una edad de {edad}" , f"usted nacio el {nacimiento}")

#Entrada
nom = input ("Inserte nombre")
edad = input ("Inserte edad")
nacimiento = input ("inserte fecha de nacimiento")

#Salida
print(f"Su nombre es {nom}" , f"tiene una edad de {edad}" , f"usted nacio el {nacimiento}", sep = " | ", end = "✓")

#Entrada
nom = input ("Inserte nombre")
edad = input ("Inserte edad")
nacimiento = input ("inserte fecha de nacimiento")

#Salida
print(f"Su nombre es {nom}\n" , f"tiene una edad de {edad}\n" , f"usted nacio el {nacimiento}", end = "✓")

#Declaración de variables
buses = int(input("Ingrese el numero de buses: "))
passengers = int(input("Ingrese el numero de pasajeros: "))
price = int(input("Ingrese el precio: "))

recaudacion = price * passengers

print(f"La recaudacion de cada bus es de {recaudacion}")

total = recaudacion * 2

print(f"El dinero ganado por los 2 buses es de {total}")


