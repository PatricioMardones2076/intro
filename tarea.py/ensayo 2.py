# Ejercicio 2
# ------------------------------------------------------------
# Un taxista cobra $500 por kilómetro recorrido más una tarifa
# base fija de $1.500 al subir al auto.
# El programa debe pedir el nombre del pasajero y los
# kilómetros recorridos.
# ¿Cuánto debe pagar el pasajero en total?
# Muestra el resultado con f-string.
 
# Tu código aquí:
Nombre_pasajero = input("Inserte nombre del pasajero: ")
Kilometros_recorridos = float(input("Inserte kilómetros recorridos: "))
Valor_por_kilometro = 500
Tarifa_base = 1500

#Salida
Total_a_pagar = (Valor_por_kilometro * Kilometros_recorridos) + Tarifa_base
print(f"El pasajero {Nombre_pasajero} debe pagar un total de: {Total_a_pagar}")