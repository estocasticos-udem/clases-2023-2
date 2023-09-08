import random

# Forma 1
print("Forma 1 - Usando indices")
poblacion = 2*['B'] + 3*['R']
print("Poblacion inicial:", poblacion)
num_experimentos = 6
muestras = random.sample(poblacion, k = num_experimentos)
print("Bolas elegidas: ", muestras, sep="")


