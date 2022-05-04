# -*- coding: utf-8 -*-
"""
Escribir un programa que haga transformaciones de pesos a dólares. 
Debe preguntarle al usuario si desea transformar de pesos mexicanos a dólares, de pesos chilenos a dólares, o desde pesos argentinos a dólares. 
Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares.
"""

#Matias Tapia

#inicializacion de valores de divisas
dolar_chileno = 855
dolar_mexicano = 20
dolar_argentino = 115

#indicacion a usuario de que divisa desea
print("transformacion de divisas")
print("coloque 1 para pesos chilenos a dolar")
print("coloque 2 para pesos mexicanos a dolar")
print("coloque 3 para pesos argentinos a dolar")
opcion = int(input("indique opcion a transformar: "))


#comprobar cual opcion eligio
if(opcion == 1):
  pesos = input("cantidad de pesos chilenos a transformar: ")
  if(int(pesos) > 0):
    transformacion =  int(pesos) / dolar_chileno
    transformacion = round(transformacion, 2)
    print("la cantidad de pesos chilenos ingresados fue: " + pesos + " ,al hacer el cambio queda con un total de " + str(transformacion) + " dolar(es)")
  else:
    print("ingrese una cantidad valida")
elif(opcion == 2):
  pesos = input("cantidad de pesos mexicanos a transformar: ")
  if(int(pesos) > 0):
    transformacion = int(pesos) / dolar_mexicano
    transformacion = round(transformacion, 2)
    print("la cantidad de pesos mexicanos ingresados fue: " + pesos + " ,al hacer el cambio queda con un total de " + str(transformacion) + " dolar(es)")
  else:
    print("ingrese una cantidad valida")
elif(opcion == 3):
  pesos = input("cantidad de pesos argentinos a transformar: ")
  if(int(pesos) > 0):
    transformacion = int(pesos) / dolar_argentino
    transformacion = round(transformacion, 2)
    print("la cantidad de pesos argentinos ingresados fue: " + pesos + " ,al hacer el cambio queda con un total de " + str(transformacion) + " dolar(es)")
  else:
    print("ingrese una cantidad valida")
else:
  print("ingrese una opcion correcta")
