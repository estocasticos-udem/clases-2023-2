"""
Suponga que se lanza varias veces un dado no cargado de seis lados  
con los números {1, 2, 3, 4, 5, 6} en sus lados. Obtener:
- El espacio muestral de S.
- La probabilidad de que se obtenga al menos 5 en el lanzamiento.

"""

# Espacio muestral del experimento
S = {1, 2, 3, 4, 5, 6}
N = len(S)

# Eventos
# E: Obtener al menos 5 en el lanzamiento: x >= 5

E = {5,6}
N_E = len(E)
P_E = N_E/N
print("--------------------------")
print(f"S = {S}")
print(f"E = {E}")
print(f"P(E) = {P_E}")

# A: Obtener un 2 o un 3 
A = set([2,3])
N_A = len(A)
P_A = N_A/N
print("--------------------------")
print(f"S = {S}")
print(f"E = {A}")
print(f"P(A) = {P_A}")

# B: La salida sea es par
B = {2,4,6}
N_B = len(B)
P_B = N_B/N
print("--------------------------")
print(f"S = {S}")
print(f"E = {B}")
print(f"P(B) = {P_B}")

# A and B: Que la salida sea: 2 o 3 "y" par (2, 4, 6)
A_and_B = A.intersection(B)
N_A_and_B = len(A_and_B)
P_A_and_B = N_A_and_B/N
print("--------------------------")
print(f"S = {S}")
print(f"A and B = {A_and_B}")
print(f"P(A and B) = {P_A_and_B}")

# A|B: 1. Que la salida sea: 2 o 3 dado que es par (2, 4, 6)
#      2. Que la salida sea: Dentro de los pares (2,4,6) este 2 o 3 
A_dado_B = {2}
# Forma 1
N_A_dado_B = len(A_dado_B)
P_A_dado_B_1 = N_A_dado_B/N_B
P_A_dado_B_2 = P_A_and_B/P_B
print(f"S = {S}")
print(f"A|B = {A_dado_B}")
print("--------------------------")
print(f"Forma 1: P(A|B) = {P_A_dado_B_1}")
print(f"Forma 2: P(A|B) = {P_A_dado_B_2}")