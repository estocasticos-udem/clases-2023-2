# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:55:55 2023

@author: b12s304e26
"""

"""
Los usuarios de mensajes de texto reciben o envían un promedio de 41,5 mensajes de texto al día.
a. ¿Cuántos mensajes de texto recibe o envía un usuario por hora? Rta: 1.7292 
b. ¿Cuál es la probabilidad de que un usuario de mensajes de texto reciba o envíe dos mensajes por hora? Rta: 0.2653
c. ¿Cuál es la probabilidad de que un usuario de mensajes de texto reciba o envíe más de dos mensajes por hora? Rta: 0.2505
d. Dibuje la pmf hasta x = 10
"""


import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
Definición de la VA Poisson: X ~ P(alpha)

X: Numero de mensajes de texto enviados o recibidos en 1 hora

# Parametros
- N = 41.5
- delta = 24
- l = N/delta = 41.5/24
- T = 1


- alpha = l*T = 1.7292
X ~ P(alpha = 1.7292)
"""

N = 41.5
delta = 24
l = N/delta

"""
a. alpha = ?
"""

T = 1
alpha = l*T

X = stats.poisson(mu = alpha)  # X ~ P(alpha = 1.7292)

"""
b. P(X = 2) = ?
"""

p_2 = X.pmf(2)
print(f"P(X = 2) = {p_2:.4}")


""" 
c. P(X > 2) = 1 - P(X <= 2) ?
"""
# P(X <= 2)
# p_leq_2 = X.pmf(0) + X.pmf(1) + X.pmf(2)

p_leq_2 = X.cdf(2)
# P(X > 2) = 1 - P(X <= 2)
p_gt_2 = 1 - p_leq_2
print(f"P(X > 2) = {p_gt_2:.4}")

"""
Grafica
"""
x = list(range(0,11))
x_pmf = X.pmf(x)
x_cdf = X.cdf(x)


# Grafica de la PMF
fig, axs = plt.subplots(2)
fig.suptitle('PMF y CDF')
# Grafica PFM
axs[0].plot(x, x_pmf, 'bs', ms=10)
axs[0].vlines(x, 0, x_pmf, colors='b', lw = 5, alpha=0.5)
axs[0].set_ylabel("$P(X = x)$")
# Grafica CDF
axs[1].plot(x, x_cdf, 'rs', ms=10)
axs[1].vlines(x, 0, x_cdf, colors='r', lw = 5, alpha=0.5)
axs[1].set_ylabel("$P(X <= x)$")
axs[1].set_xlabel("$x$: Numero de mensajes enviados o recibidos en una hora")










