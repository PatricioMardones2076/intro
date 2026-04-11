#Desarrrolle un programa que permita ingresar 3 numeros y desplegarlos de forma descendente.
primer_num = int(input("Ingrese el primer numero:"))
segundo_num = int(input("Ingrese el segundo numero:"))
tercer_num = int(input("Ingrese el tercer numero:"))
if primer_num > segundo_num:
 if primer_num > tercer_num:
    if segundo_num > tercer_num:
     print("Los numeros en orden descendente son:", primer_num, segundo_num, tercer_num) 
if segundo_num > primer_num:
 if segundo_num > tercer_num:
    if primer_num > tercer_num:
      print("Los numeros en orden descendente son:", segundo_num, primer_num, tercer_num)
if tercer_num > primer_num:
  if tercer_num > segundo_num:
    if primer_num > segundo_num:
     print("Los numeros en orden descendente son:", tercer_num, segundo_num, primer_num)
if tercer_num > primer_num:
  if tercer_num > segundo_num:
    if segundo_num > primer_num:
     print("Los numeros en orden descendente son:", tercer_num, primer_num, segundo_num)
