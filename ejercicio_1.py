
"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""
#Matias Tapia

#input para consultar cantidad vendida
Barras_vendidas = float(input("Barras vendidas de pan no del dia: "))

#inicializacion de precio de pan fresco
precio_normal = 3.49
Precio_barras = Barras_vendidas * (precio_normal * 0.6)
Precio_barras_normal = Barras_vendidas * precio_normal
Precio_barras = round(Precio_barras,2)
descuento = Precio_barras_normal - Precio_barras
descuento = round(descuento, 2)

print("precio habitual de una barra de pan es: " + str(precio_normal) + "€")
print("el descuento aplicado es de: " + str(descuento) + "€")
print("el coste total del pan no del dia: " + str(Precio_barras) + "€")
