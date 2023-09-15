# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:10:04 2023

@author: b12s304e26
"""

# Archivo en proceso

"""
Cada hijo de un par particular de padres tiene una probabilidad de 0.25 
de tener el tipo de sangre O. Supongamos que los padres tienen 5 hijos
"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# X: Numero de hijos con sangre tipo O

n = 5
p = 0.25
# X ~ B (n = 5, p = 0.25)
X = stats.binom(n, p)

# P(X = 3)
p_3 = X.pmf(3)
print(f"P(X = 3) = {p_3:.6}")

# P(X > 3)
p_4 = X.pmf(4)
p_5 = X.pmf(5)
p_mas3 = p_4 + p_5
print(f"P(X > 3) = {p_mas3:.6}")

x = list(range(6)) # x = [0,1,2,3,4,5]
pmf_x =  X.pmf(x)

modelo = pd.DataFrame({"x": x,"p": pmf_x})
print(modelo)

# Grafica
plt.plot(x, pmf_x, 'gs', ms=10)
plt.vlines(x, 0, pmf_x, colors='g', lw = 5, alpha=0.5)
plt.xlabel("$X$: Numero de niños con sangre tipo O")
plt.ylabel("$P(X = x)$")
plt.title("Niños con sangre tipo O")
plt.show()

# Medidas
media = X.mean()
var = X.var()
std = X.std()
print()
print("Estadisticos")
print(f"Media: E(X) = {media:.3}")
print(f"Varianza: VAR(X) = {var:.4}")
print(f"Desviacion estandar: STD(X) = {std:.4}")




