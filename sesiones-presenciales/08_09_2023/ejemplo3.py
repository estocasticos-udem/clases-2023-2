# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:24:11 2023

@author: b12s304e26
"""



"""
Un equipo de fútbol masculino juega al fútbol en cero, en uno o en dos días a la semana. La probabilidad de que 
jueguen cero días es de 0,2, la de que jueguen un día es de 0,5 y la de que jueguen dos días es de 0,3. Calcule el 
promedio a largo plazo o el valor esperado, 𝜇, del número de días por semana que el equipo de fútbol masculino 
juega al fútbol.

"""
import pandas as pd
import matplotlib.pyplot as plt
import math



"""
X: el número de días que el equipo de fútbol masculino juega al fútbol por semana
x: 0, 1, 2
"""

print("Solucion ejemplo 3")


x = list(range(3))
p_x = [0.2, 0.5, 0.3]

modelo3 = pd.DataFrame({"x": x, "P(x)":p_x})
print(modelo3) 
modelo3["x*P(x)"] = modelo3["x"]*modelo3["P(x)"]
print(modelo3) 

# Grafica
plt.plot(x, modelo3["P(x)"], 'gs', ms=10)
plt.vlines(x, 0, modelo3["P(x)"], colors='g', lw = 5, alpha=0.5)
plt.xlabel("$X$: Numero de veces que llora el niño")
plt.ylabel("$P(X = x)$")
plt.title("Encuesta de la llorada de los bebes")
plt.show()


# Valor esperado: Media
mu = modelo3["x*P(x)"].sum()
# Varianza
var = sum(((modelo3["x"] - mu)**2)*modelo3["P(x)"])
# Desviacion estandar
std = math.sqrt(var)
print()
print("Estadisticos")
print(f"Media: E(X) = {mu:.3}")
print(f"Varianza: VAR(X) = {var:.4}")
print(f"Desviacion estandar: STD(X) = {std:.4}")

