# Ejercicio 1
# ------------------------------------------------------------
# María trabaja en una tienda y vende 3 productos distintos.
# El programa debe pedir el nombre y precio de cada producto,
# y la cantidad que se vendió de cada uno.
# ¿Cuánto es el total recaudado por la tienda ese día?
 
# Tu código aquí:
Producto_1 = input("Inserte nombre del producto 1: ")
Valor_producto_1 = float(input("Inserte valor del producto 1: "))
Cantidad_de_producto_1_vendido = int(input("Inserte cantidad vendida del producto 1: "))
Total_producto_1 = Cantidad_de_producto_1_vendido * Valor_producto_1

Producto_2 = input("Inserte nombre del producto 2: ")
Valor_producto_2 = float(input("Inserte valor del producto 2: "))
Cantidad_de_producto_2_vendido = int(input("Inserte cantidad vendida del producto 2: "))
Total_producto_2 = Cantidad_de_producto_2_vendido * Valor_producto_2

Producto_3 = input("Inserte nombre del producto 3: ")
Valor_producto_3 = float(input("Inserte valor del producto 3: "))
Cantidad_de_producto_3_vendido = int(input("Inserte cantidad vendida del producto 3: "))
Total_producto_3 = Cantidad_de_producto_3_vendido * Valor_producto_3

#Salida
Total_recaudado = Total_producto_1 + Total_producto_2 + Total_producto_3
print(f"Total recaudado: {Total_recaudado}")