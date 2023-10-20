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

plt.close('all') # Se cierran todas las figuras para empezar

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

# b. Halle el percentil 30 de los tiempos de espera (en minutos).

P_k = 0.3
k = 0.3*b
print(f"El valor del percentil 30 es: k = {k:.2f}")

x = np.arange(-3,10,0.1)
pdf_x = X.pdf(x)
cdf_x = X.cdf(x)

# Graficando esto tenemos
fig, (ax) = plt.subplots()
ax.plot(x, pdf_x)
ax.set_ylabel('$f(x)$')
ax.vlines(x = k, ymin = 0,ymax = max(pdf_x), color = 'b', linestyles='--')
ax.fill_between(x, pdf_x,0, where=(x>=0) & (x<=k), color='blue', alpha=.1)
ax.set_xlabel('$x$: Tiempo de llegada del Sky Train (min)')


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
fig, (ax1, ax2) = plt.subplots(2,1)



# Grafica del a PDF
ax1.plot(x, pdf_x)
ax1.set_ylabel('$f(x)$')
ax2.plot(x, cdf_x)
ax2.set_ylabel('$F(x)$')
ax2.set_xlabel('$x$: Tiempo de llegada del Sky Train (min)')





