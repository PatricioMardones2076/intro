#Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero que el teatro deja de percibir por cada una de las categorías. Tomar en cuenta que los niños menores de 5 años no pueden entrar al teatro y que existe un precio único($ 10.000.-) en los asientos. 
#Los descuentos se hacen tomando en cuenta el siguiente cuadro: 
#Categorías Edad Descuento 
#Categoría 1 -> 5 - 14 -> 35 % 
#Categoría 2 -> 15 - 19 -> 25 % 
#Categoría 3 -> 20 – 60 -> 0 %
#Categoría 4 -> Mayor de 60 años -> 90% 

#Desarrolle un programa que permita ingresar la cantidad de personas que pueden entrar al teatro, luego por cada entrada calcular según edad del cliente.
#Al finalizar el último cliente entregar el siguiente detalle:
#a)	Total recaudado.
#b)	Cantidad de clientes ingresada ingresados en cada categoría.
#c)	Total de descuentos aplicados.
precio = 10000
total_recaudado = 0
total_descuentos = 0
categoria_1 = 0
categoria_2 = 0
categoria_3 = 0
categoria_4 = 0
cantidad_personas = int(input("Ingrese la cantidad de personas que pueden entrar al teatro: "))
i = 1
while i <= cantidad_personas:
    edad = int(input("Ingrese la edad del cliente: "))
    if edad < 5:
        print("Los niños menores de 5 años no pueden entrar al teatro.")
    if 5 <= edad <= 14:
        descuento = precio * 0.35
        total_descuentos = total_descuentos + descuento
        total_recaudado = total_recaudado + (precio - descuento)
        categoria_1 = categoria_1 + 1
    if 15 <= edad <= 19:
        descuento = precio * 0.25
        total_descuentos = total_descuentos + descuento
        total_recaudado = total_recaudado + (precio - descuento)
        categoria_2 = categoria_2 + 1
    if 20 <= edad <= 60:
        total_recaudado = total_recaudado + precio
        categoria_3 = categoria_3 + 1
    if edad > 60:
        descuento = precio * 0.90
        total_descuentos = total_descuentos + descuento
        total_recaudado = total_recaudado + (precio - descuento)
        categoria_4 = categoria_4 + 1
    i = i + 1
print("Total recaudado:", total_recaudado)
print("Cantidad de clientes ingresados en cada categoría:")
print("Categoría 1 (5-14 años):", categoria_1)
print("Categoría 2 (15-19 años):", categoria_2)
print("Categoría 3 (20-60 años):", categoria_3)
print("Categoría 4 (Mayor de 60 años):", categoria_4)
print("Total de descuentos aplicados:", total_descuentos)

