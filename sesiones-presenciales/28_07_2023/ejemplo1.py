# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:24:11 2023

@author: b12s304e26
"""

print("Fecha: 08/09/2023")

"""
Suponga un experimento que consiste en lanzar una moneda no cargada tres veces.

X: Numero de caras en los lanzamientos
"""

import pandas as pd
import matplotlib.pyplot as plt

x = [0,1,2,3]
p_x = [1/8, 3/8, 3/8, 1/8]

modelo = pd.DataFrame({"x": x, "P(x)":p_x})
modelo = modelo.set_index("x")
print(modelo) 

# Grafica
plt.plot(x, modelo["P(x)"], 'bs', ms=10)
plt.vlines(x, 0, modelo["P(x)"], colors='b', lw = 5, alpha=0.5)
plt.xlabel("$X$: Numero de caras")
plt.ylabel("$P(X = x)$")
plt.title("Lanzamiento de tres monedas")
plt.show()
