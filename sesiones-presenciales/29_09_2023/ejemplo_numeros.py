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
Y ~ U(k,l)

Y: Numero entre 10 y 30 

y = {10,12,...,30}

Y ~ U(k = 0,l = 1)
"""


k = 10
l = 30

Y = stats.randint(low = k, high = l + 1) # Y ~ U(k = 10,l = 30)

# 
y = list(range(0,41))
y_pmf = Y.pmf(y)


# Grafica de la PMF
fig, axs = plt.subplots(2)
fig.suptitle('PMF y CDF')
# Grafica PFM
axs[0].plot(y, y_pmf, 'bs', ms=10)
axs[0].vlines(y, 0, y_pmf, colors='b', lw = 5, alpha=0.5)
axs[0].set_ylabel("$P(Y = y)$")
# Grafica CDF
#axs[1].plot(x, x_cdf, 'rs', ms=10)
#axs[1].vlines(x, 0, x_cdf, colors='r', lw = 5, alpha=0.5)
#axs[1].set_ylabel("$P(X <= x)$")
#axs[1].set_xlabel("$x$: Numero de mensajes enviados o recibidos en una hora")
