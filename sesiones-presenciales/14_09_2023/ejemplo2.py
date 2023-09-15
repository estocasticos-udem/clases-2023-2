# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:57:59 2023

@author: b12s304e26
"""

"""
Más del 96 % de los institutos universitarios y universidades más grandes (más de 15.000
inscritos en total) tienen alguna oferta en línea. Supongamos que se eligen al azar 13 de estas
instituciones. Nos interesa el número de los que ofrecen cursos a distancia.
a. Describa la variable aleatoria X con palabras.
b. Enumere los valores que puede tomar X.
c. Cuáles son los parámetros de la distribución.
d. En promedio, ¿cuántas escuelas espera que ofrezcan este tipo de cursos? (Rta: 12.48).
e. Calcule la probabilidad de que como máximo diez ofrezcan esos cursos. (Rta: 0.0135).
f. ¿Es más probable que 12 o 13 ofrezcan estos cursos? Utilice los números para justificar su
respuesta numéricamente y responda con una oración completa. (Rta: 𝑃(𝑥 = 12) =
0.3186, 𝑃(𝑥 = 13) = 0.5882).
"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" a. Describa la variable aleatoria X con palabras."""
# X: Numero de universidades en las que se ofrecen cursos a distancia

""" b. Describa la variable aleatoria X con palabras."""
x = list(range(14))

"""c. Cuáles son los parámetros de la distribución."""
n = 13
p = 0.96
# X ~ B (n = 14, p = 0.96)
X = stats.binom(n, p)

"""d. En promedio, ¿cuántas escuelas espera que ofrezcan este tipo de cursos?"""
media = X.mean()
print()
print("Estadisticos")
print(f"Se esperan que: E(X) = {media:.4} escuelas ofrezcan cursos a distanca")

"""e. Calcule la probabilidad de que como máximo diez ofrezcan esos cursos."""
pmf =  X.pmf(x)
modelo = pd.DataFrame({"x": x,"p": pmf})
print(modelo)

prob1 = sum(pmf[:11])
print(f"P(X <= 01) = {prob1:.3}")

"""f. ¿Es más probable que 12 o 13 ofrezcan estos cursos? Utilice los números para justificar su
respuesta numéricamente y responda con una oración completa."""

p_13 = X.pmf(13)
p_12 = X.pmf(12)
print(f"P(X = 13) = {p_13:.3}")
print(f"P(X = 12) = {p_12:.3}")
if p_13 > p_12:
    print("13 es mas probable")
else:
    print("12 es mas probable")

"""
# P(X = 3)
p_3 = X.pmf(3)
print(f"P(X = 3) = {p_3:.6}")

# P(X > 3)
p_4 = X.pmf(4)
p_5 = X.pmf(5)
p_mas3 = p_4 + p_5
print(f"P(X > 3) = {p_mas3:.6}")

x = list(range(6)) # x = [0,1,2,3,4,5]
pmf_x =  X.pmf(x)

modelo = pd.DataFrame({"x": x,"p": pmf_x})
print(modelo)

# Grafica
plt.plot(x, pmf_x, 'gs', ms=10)
plt.vlines(x, 0, pmf_x, colors='g', lw = 5, alpha=0.5)
plt.xlabel("$X$: Numero de niños con sangre tipo O")
plt.ylabel("$P(X = x)$")
plt.title("Niños con sangre tipo O")
plt.show()

# Medidas
media = X.mean()
var = X.var()
std = X.std()
print()
print("Estadisticos")
print(f"Media: E(X) = {media:.3}")
print(f"Varianza: VAR(X) = {var:.4}")
print(f"Desviacion estandar: STD(X) = {std:.4}")
"""



