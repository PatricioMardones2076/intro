# Ejercicio 7
# ------------------------------------------------------------
# Una fábrica produce 3 tipos de cajas: pequeña, mediana y grande.
# Cada caja pequeña pesa 2.5 kg, la mediana 5.8 kg y la grande 12.3 kg.
# El programa debe pedir cuántas cajas de cada tipo se fabricaron hoy.
# ¿Cuánto es el peso total producido?
# Si un camión soporta 500 kg, ¿cuántos camiones completos se necesitan?
# (usa división entera para los camiones completos y % para el resto)
 
# Tu código aqui:
Cajas_pequenas = int(input("Ingrese la cantidad de cajas pequeñas fabricadas: "))
Cajas_medianas = int(input("Ingrese la cantidad de cajas medianas fabricadas: "))
Cajas_grandes = int(input("Ingrese la cantidad de cajas grandes fabricadas: "))
Peso_pequenas = Cajas_pequenas * 2.5
Peso_medianas = Cajas_medianas * 5.8
Peso_grandes = Cajas_grandes * 12.3
Peso_total = Peso_pequenas + Peso_medianas + Peso_grandes
Camiones_completos = Peso_total // 500
Peso_restante = Peso_total % 500
print(f"El peso total producido es: {Peso_total} kg")
print(f"Se necesitan {Camiones_completos} camiones completos y un camión con {Peso_restante} kg restante.")
