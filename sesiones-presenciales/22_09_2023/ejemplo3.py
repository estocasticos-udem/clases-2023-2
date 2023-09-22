# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:43:26 2023

@author: b12s304e26
"""

"""
Un producto industrial particular se envía en lotes de 20. Hacer pruebas 
para determinar si un artículo es defectuoso o costoso; por tanto, 
el fabricante muestrea la producción en lugar de usar un plan de 
inspección del 100%. Un plan de muestreo construido para reducir al 
mínimo el número de piezas defectuosas, enviadas a los clientes, exige 
muestrear cinco artículos de entre cada lote y rechazar el lote si se 
observa más de una pieza tipo de inecuación se traducen defectuosa. 
(Si el lote es rechazado, cada artículo del lote se prueba entonces.) 
Si un lote contiene cuatro defectuosos, ¿cuál es la probabilidad de 
que sea aceptado?

"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
Definición de la VA hipergeometrica: X ~ H(r,b,n)

X: Numero de elementos defectuosos dentro de la muestra de cinco elementos

# Parametros
r = 4   # n (primer grupo - exitos)
b = 16
n = 5   # N (muestra)
        # M = r + b (Total)
"""

# Notacion clase

# Python
r = 4     # r 
b = 16     # n   
n = 5     # b  -> M = r + b 


X = stats.hypergeom(r + b, r, n) # Variable aleatoria hipergeometrica
p_ok = X.pmf(0) + X.pmf(1)
print(f"P(aceptado) = {p_ok}")

