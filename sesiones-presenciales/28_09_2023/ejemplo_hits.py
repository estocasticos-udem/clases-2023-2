# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:55:55 2023

@author: b12s304e26
"""

"""
El número de hits en un sitio Web en cualquier intervalo de tiempo es una VA de Poisson. Un sitio particular tiene un promedio de 𝜆=2 hits por segundo:
a. ¿Cuál es la probabilidad que no hayan hits en un intervalo de 0.25 segundos? Rta: 0.607
b. ¿cuál es la probabilidad de que no hayan más de dos hits es un intervalo de un segundo? Rta: 0.667
c. Grafica de la pdf
"""


import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
Definición de la VA Poisson: X ~ P(alpha)



# Parametros
- l = 2
- T = 1

"""

l = 2 # lamda


"""
a. alpha = ?, T = 0.25 -> 

   X ~ P(alpha)
   X: Numero de hits en 0.25s
   
   P(X=0) = ?
"""

T = 0.25
alpha_1 = l*T
X = stats.poisson(mu = alpha_1)  
p_0 = X.pmf(0)
print(f"P(X = 0) = {p_0:.3}")


"""
b. alpha = ?, T = 1 -> 

   Y ~ P(alpha)
   Y: Numero de hits en 1s
   
   P(X <= 2) = ?
"""
T = 1
alpha_2 = l*T
Y = stats.poisson(mu = alpha_2)
p_leq_2 = Y.cdf(2)
print(f"P(Y <= 2) = {p_leq_2:.3}")

"""
c. Grafica de la pdf
"""
x = range(11)
y = range(11) 
x_pmf = X.pmf(x)
y_pmf = Y.pmf(y)

# Grafica de la PMF
fig, axs = plt.subplots(2)
fig.suptitle('PMFs')
# Grafica PFM de x
axs[0].plot(x, x_pmf, 'bs', ms=10)
axs[0].vlines(x, 0, x_pmf, colors='b', lw = 5, alpha=0.5)
axs[0].set_ylabel("$P(X = x)$")
axs[0].set_xlabel("$x$: Numero de hits en 0.25 seg")
# Grafica PFM de y
axs[1].plot(y, y_pmf, 'rs', ms=10)
axs[1].vlines(y, 0, y_pmf, colors='r', lw = 5, alpha=0.5)
axs[1].set_ylabel("$P(Y = y)$")
axs[1].set_xlabel("$y$: Numero de hits en 1 seg")


