primer_num = int(input("Ingrese el primer numero:"))
segundo_num = int(input("Ingrese el segundo numero:"))
tercer_num = int(input("Ingrese el tercer numero:"))
if primer_num < segundo_num:
 if primer_num < tercer_num:
    if segundo_num < tercer_num:
     print("Los numeros en orden ascendente son:", primer_num, segundo_num, tercer_num) 
if segundo_num < primer_num:
 if segundo_num < tercer_num:
    if primer_num < tercer_num:
      print("Los numeros en orden ascendente son:", segundo_num, primer_num, tercer_num)
if tercer_num < primer_num:
  if tercer_num < segundo_num:
    if primer_num < segundo_num:
     print("Los numeros en orden ascendente son:", tercer_num, segundo_num, primer_num)
