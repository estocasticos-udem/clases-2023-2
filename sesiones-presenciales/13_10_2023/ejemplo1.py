# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:51:12 2023

@author: b12s304e26
"""

"""
Se supone que el Sky Train llega cada ocho minutos desde la terminal hasta el centro de
alquiler de automóviles y el estacionamiento de larga duración. Se sabe que los tiempos de
espera del tren siguen una distribución uniforme.
a. ¿Cuál es el tiempo promedio de espera (en minutos)? (Rta: 4)
b. Halle el percentil 30 de los tiempos de espera (en minutos).
c. ¿Cuál es la probabilidad de esperar más de siete minutos dado que una persona ha
   esperado más de cuatro minutos? (Rta: 0.25)
"""

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
X ~ U(a,b)

X: Tiempo en minutos que demora el Sky Train desde la terminal a los destinos

Parametros:
a = 0
b = 8
"""


"""
X ~ U(a = 0,b = 8)
"""
a = 0
b = 8 
X = stats.uniform(loc=a, scale=b)

# a. ¿Cuál es el tiempo promedio de espera (en minutos)?
media = X.mean()
print(f"Tiempo promedio: {media:.2f}")

# b....

# c.  ¿Cuál es la probabilidad de esperar más de siete minutos dado que una persona ha
#     esperado más de cuatro minutos? 
#
#
# P(X > 7|X > 4)

P_A = 1 - X.cdf(x = 7)
P_B = 1 - X.cdf(x = 4)
P_AB = P_A
P_A_dado_B = P_AB/P_B
print(f"P(X > 7|X > 4) = {P_A_dado_B:.2f}")

# Graficas
fig, (ax1, ax2) = plt.subplots(1, 2)
x = np.arange(0,10,0.1)
pdf_x = X.pdf(x)
cdf_x = X.cdf(x)

# Grafica del a PDF
ax1.plot(x, pdf_x)
ax1.set_title('PDF de X')
ax1.xlabel('x')
ax2.plot(x, cdf_x)
ax2.xlabel('x')





