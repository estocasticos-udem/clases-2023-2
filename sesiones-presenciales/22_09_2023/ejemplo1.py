# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:43:26 2023

@author: b12s304e26
"""

"""
Un plato de caramelos contiene 100 gominolas y 80 chicles. Se eligen 50 caramelos al azar. ¿Cuál es la probabilidad 
de que 35 de los 50 sean chicles? 
"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
Definición de la VA hipergeometrica: X ~ H(r,b,n)

X: Numero de chicles en la muestra de 50 dulces

# Parametros
r = 80   # n (primer grupo - exitos)
b = 100
n = 50   # N (muestra)
         # M = r + b (Total)
"""

# Notacion clase

# Python
n = 80     # r = 80
N = 50     # n = 50  
M = 180    # b = 80 -> M = r + b = 80 + 100


X = stats.hypergeom(N = 50, n = 80, M = 180) # Variable aleatoria hipergeometrica
pmf_35 = X.pmf(35)
print(f"P(x = 35) = {pmf_35}")