# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:24:25 2023

@author: b12s304e26
"""

"""
VA unidorme dados
"""


import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
X ~ U(k,l)

X: Numero de caras que aparecen en un lanzamiento de una moneda

x = {0,1}

X ~ U(k = 0,l = 1)
"""


l = 1
k = 0
X = stats.randint(low = k, high = l + 1) # X ~ U(k = 0,l = 1)

# 
x = list(range(-10,11))
x_pmf = X.pmf(x)


# Grafica de la PMF
fig, axs = plt.subplots(2)
fig.suptitle('PMF y CDF')
# Grafica PFM
axs[0].plot(x, x_pmf, 'bs', ms=10)
axs[0].vlines(x, 0, x_pmf, colors='b', lw = 5, alpha=0.5)
axs[0].set_ylabel("$P(X = x)$")
# Grafica CDF
#axs[1].plot(x, x_cdf, 'rs', ms=10)
#axs[1].vlines(x, 0, x_cdf, colors='r', lw = 5, alpha=0.5)
#axs[1].set_ylabel("$P(X <= x)$")
#axs[1].set_xlabel("$x$: Numero de mensajes enviados o recibidos en una hora")
