# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:28:05 2023

@author: b12s304e26
"""

"""
En uno de sus catálogos de primavera, L. L. Bean anunciaba calzado en 29 de las 192 páginas
de su catálogo. Supongamos que tomamos al azar 20 páginas. Nos interesa el número de
páginas que anuncian calzado. Cada página puede ser elegida más de una vez.
a. Defina la variable aleatoria X en palabras.
b. Enumere los valores que puede tomar X.
c. Cuáles son los parámetros de la distribución.
d. ¿Cuántas páginas espera que anuncien calzado? (Rta: 3.02)
e. ¿Es probable que las veinte anuncien calzado en ellas? ¿Por qué sí o por qué no? (Rta: No)
f. ¿Cuál es la probabilidad de que menos de diez anuncien calzado en ellas? (Rta: 0.9997)
"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""a. Defina la variable aleatoria X en palabras."""
# Y: Numero de paginas que anucian calzado

"""b. Enumere los valores que puede tomar X."""
y = list(range(1,21))

"""c. Cuáles son los parámetros de la distribución."""
p = 29/192
Y = stats.geom(p)

"""d. ¿Cuántas páginas espera que anuncien calzado? """
media = Y.mean()
print(f"Media = E(X) = {media:.4}")

"""e. ¿Es probable que las veinte anuncien calzado en ellas? ¿Por qué sí o por qué no? """
pmf_y = Y.pmf(y)
print(f"P(X = 20) = {pmf_y[19]:.4}")

""". ¿Cuál es la probabilidad de que menos de diez anuncien calzado en ellas?"""

p_sum_9 = sum(pmf_y[:10]) 
print(f"P(X < 10) = {p_sum_9:.4}")
