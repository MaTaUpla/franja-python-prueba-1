#Matias Tapia

""" Escribir un programa que le pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales.
"""
#se le indica al usuario ingrese los datos
capital_a_invertir = float(input("ingrese capital a invertir: "))
interes = float(input("ingrese porcentual anual: "))
número_años = float(input("ingrese número de años: "))

#calculo de formula, donde pow es para la potencia de numero de años
auxiliar_formula = ((interes / 100) + 1)
formula = capital_a_invertir * pow(auxiliar_formula, número_años)
formula = round(formula, 2)

#resultado del capital obtenido
print("El capital obtenido seria: " + str(formula))
