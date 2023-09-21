# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:28:05 2023

@author: b12s304e26
"""

"""
En una clase, su profesor planea darte 10 problemas como tarea. Sin embargo desea negociar la tarea para la cual propone 
a sus estudiantes jugar el juego del cumpleaños, el cual funciona así:
1. El profesor seleccionará un estudiante al azar de su clase y le pedirá a un estudiante elegido al azar, 
   que adivine el día de la semana (por ejemplo, jueves) en el que nació uno de los amigos del profesor. 
2. Si el estudiante adivina correctamente, entonces la clase tendrá un solo problema de tarea. 
3. Si el estudiante adivina el día de la semana equivocado, el profesor volverá a seleccionar al azar a otro estudiante 
   de la clase. El alumno elegido intentará adivinar el día de la semana en el que nació otro amigo del profesor. Si 
   este estudiante lo hace bien, la clase tendrá dos problemas de tarea. 
4. El juego continúa hasta que un alumno acierta correctamente el día en que nació uno de los (muchos) amigos del 
   profesor. 


Preguntas:
a. ¿Cuál es la probabilidad de que el primer estudiante adivine correctamente?
b. ¿Cuál es la probabilidad de que le pongan a la clase dos problemas de tarea?
c. ¿Cuál es la probabilidad de que el tercer estudiante sea el que adivine?
d. ¿Cuál es la probabilidad el éxito se obtenga en el k-esimo intento?
e. Encuentre la probabilidad de que la clase tenga que hacer como tarea 10 problemas.
f. Encuentre P(Y < 10) e interprete el valor en este contexto. 

"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""1. Defina la variable aleatoria X en palabras."""
# Y: Numero de intentos hasta que se adivina correctamente el dia del cumpleaños del amigo del profesor 
    
"""2. Enumere los valores que puede tomar X."""
y = list(range(1,11))

"""3. Cuáles son los parámetros de la distribución."""
p = 1/7
Y = stats.geom(p)
pmf_y = Y.pmf(y)
# a. P(Y = 1) = ?
P_y_1 = pmf_y[0]
print(f"P(Y = 1) = {P_y_1:.4}")
# b. P(Y = 2) = ?
P_y_2 = pmf_y[1]
print(f"P(Y = 2) = {P_y_2:.4}")
# c. P(Y = 3) = ?
P_y_3 = Y.pmf(3)
print(f"P(Y = 3) = {P_y_3:.4}")
# d. P(Y = k) = ?
# ----

# Grafica de la PFM (Probability Mass Function)
plt.plot(y, pmf_y, 'gs', ms=10)
plt.vlines(y, 0, pmf_y, colors='g', lw = 5, alpha=0.5)
plt.xlabel("$Y$: Numero de intentos hasta que se adivina correctamente")
plt.ylabel("$P(Y = y)$")
plt.title("Numero de intentos para la tarea")
plt.show()

# ----
# e. P(Y <10) = ?
print(f"P(Y = 10) = {pmf_y[9]:.4}")

# e. P(Y < 10) = ?
print(f"P(Y < 10) = {sum(pmf_y[:9]):.4}")
