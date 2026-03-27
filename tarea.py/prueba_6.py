# Ejercicio 6
# ------------------------------------------------------------
# Un cine cobra $4.500 la entrada normal y hace un 30% de
# descuento a estudiantes y un 50% a adultos mayores.
# El programa debe pedir cuántas entradas normales,
# cuántas de estudiante y cuántas de adulto mayor se vendieron.
# ¿Cuánto recaudó el cine en total?
 
# Tu código aquí:
Entradas_normales = int(input("Ingrese la cantidad de entradas normales vendidas: "))
Entradas_estudiantes = int(input("Ingrese la cantidad de entradas de estudiante vendidas: "))
Entradas_adultos_mayores = int(input("Ingrese la cantidad de entradas de adulto mayor vendidas: "))
Precio_normal = 4500
Descuento_estudiante = 0.3
Descuento_adulto_mayor = 0.5
Ingresos_normales = Entradas_normales * Precio_normal
Ingresos_estudiantes = Entradas_estudiantes * Precio_normal * (1 - Descuento_estudiante)
Ingresos_adultos_mayores = Entradas_adultos_mayores * Precio_normal * (1 - Descuento_adulto_mayor)
Total_recaudado = Ingresos_normales + Ingresos_estudiantes + Ingresos_adultos_mayores
print(f"El cine recaudó un total de: {Total_recaudado}")