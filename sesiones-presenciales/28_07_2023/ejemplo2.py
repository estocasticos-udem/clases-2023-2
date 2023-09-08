# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:24:11 2023

@author: b12s304e26
"""



"""
Enunciado
Un psicólogo infantil se interesa por el número de veces que el llanto de un recién nacido 
despierta a su madre después de la medianoche. Para una muestra aleatoria de 50 madres, 
se obtuvo la siguiente información. 
"""
import pandas as pd
import matplotlib.pyplot as plt
import math



"""
X: el número de veces por semana que el llanto de un recién nacido despierta a su madre 
   después de la medianoche
x: 0, 1, 2, 3, 4, 5
"""

print("Solucion ejemplo 2")


x = list(range(6))
p_x = [2/50, 11/50, 23/50, 9/50, 4/50, 1/50]

modelo2 = pd.DataFrame({"x": x, "P(x)":p_x})
modelo2 = modelo2.set_index("x")
print(modelo2) 

# Grafica
plt.plot(x, modelo2["P(x)"], 'rs', ms=10)
plt.vlines(x, 0, modelo2["P(x)"], colors='r', lw = 5, alpha=0.5)
plt.xlabel("$X$: Numero de veces que llora el niño")
plt.ylabel("$P(X = x)$")
plt.title("Encuesta de la llorada de los bebes")
plt.show()

# Valor esperado: Media
mu = sum((modelo2.index)*(modelo2["P(x)"]))
# Varianza
var = sum(((modelo2.index - mu)**2)*(modelo2["P(x)"]))
# Desviacion estandar
std = math.sqrt(var)
print()
print("Estadisticos")
print(f"Media: E(X) = {mu:.3}")
print(f"Varianza: VAR(X) = {var:.4}")
print(f"Desviacion estandar: STD(X) = {std:.4}")


