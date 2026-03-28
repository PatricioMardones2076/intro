# Para bajar 1 kg. de peso tenemos que trotar 30 minutos y realizar 100 abdominales, realice un sistema donde se ingrese la cantidad de peso que se desea bajar y el sistema le entregue cuantos minutos debe trotar y la cantidad de abdominales que debe ejecutar.
# Tu código aquí:

#Definir variables
peso_a_bajar = 0.0
peso_a_bajar = float(input("Ingrese la cantidad de peso que desea bajar en kg: "))

#Entrada
minutos_a_trotar = peso_a_bajar * 30
abdominales_a_ejecutar = peso_a_bajar * 100

#Salida
print(f"Para bajar {peso_a_bajar} kg. debe trotar {minutos_a_trotar} minutos y realizar {abdominales_a_ejecutar} abdominales.") 