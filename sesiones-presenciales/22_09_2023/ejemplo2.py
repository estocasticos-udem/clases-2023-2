# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:43:26 2023

@author: b12s304e26
"""

"""
Una bolsa contiene fichas de letras. Cuarenta y cuatro de las fichas son 
vocales y 56 son consonantes. Se eligen siete fichas al azar. Quiere 
saber la probabilidad de que cuatro de las siete fichas sean vocales. 
¿Cuál es el grupo de interés, el tamaño del grupo de interés y el tamaño 
de la muestra?
 
"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
Definición de la VA hipergeometrica: F ~ H(r,b,n)

F: Numero de vocales elegidas para el grupo de 7 fichas

# Parametros
r = 56   # n (primer grupo - exitos)
b = 44
n = 7    # N (muestra)
         # M = r + b (Total)
"""

# Notacion clase

# Python
n = 56     # r 
N = 7      # n   
M = 100    # b  -> M = r + b 


F = stats.hypergeom(N = 7, n = 56, M = 100) # Variable aleatoria hipergeometrica
pmf_4 = F.pmf(4)
print(f"P(F = 4) = {pmf_4}")