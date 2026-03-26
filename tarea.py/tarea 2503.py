#Don Juan Gonzalez compra 2 packs de cerveza (6 latas por pack), una marca Dorada y la otra Baltica, el total de su compra fue 4500 pesos y el pack de Baltica costo 2100 ¿Cuanto es el costo de cada cerveza dorada y Baltica?

cerveza_A = int(input("Inserte cantidad de latas: "))
cerveza_A_valor = int(input("Inserte valor del six pack: "))
precio_individual_A = cerveza_A_valor / cerveza_A

valor_total = int(input("Inserte precio total: "))
precio_six_pack_cerveza_B = valor_total - cerveza_A_valor
cerveza_B = int(input("Inserte cantidad de latas: "))
cerveza_B_valor = int(input("Inserte valor del six pack: "))
precio_individual_cerveza_B = cerveza_B_valor / cerveza_B

print(f"{precio_individual_A} = {cerveza_A_valor} / {cerveza_A}")
print(f"precio_individual_cerveza_B = {cerveza_B_valor} / {cerveza_B}")
