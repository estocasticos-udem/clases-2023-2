import pandas as pd


df = pd.DataFrame({'Alto': [18, 20 ,12], 
                   'Medio': [28, 51, 25],
                   'Bajo': [14,28,9]},
             index=['Obeso', 'Normal',"Bajo_peso"])

print(df) 



# a. Calcule el total de cada fila y columna

# Columnas
pesos = df.sum(axis = 1)
# Filas
alturas = df.sum()

# b. Calcule la probabilidad de que una persona elegida al azar 
# de este grupo sea alta.
N = df.sum().sum() 

N_alta = alturas[0]
# df.iloc[0,0]
 
P_alta = N_alta/N

print(f"P(alta)= {P_alta:.3f}")

# d. Calcule la probabilidad de que una persona elegida al azar de este 
# grupo sea obesa y alta.

N_obesa_alta = df.iloc[0,0]
P_obesa_alta = N_obesa_alta/N
print(f"P(obesa y alta)= {P_obesa_alta:.3f}")


# d. Calcule la probabilidad de que una persona elegida al azar de este grupo 
# sea alta dado que es obesa
N_obesa = pesos[0]
P_alta_dado_obesa = N_obesa_alta/N_obesa
print(f"P(alta|obesa)= {P_alta_dado_obesa:.3f}")

# e. Calcule la probabilidad de que una persona elegida al azar de este grupo sea obesa, 
# dado que es alta.
N_alta = alturas[0]
P_obesa_dado_alta = N_obesa_alta/N_alta
print(f"P(obesa|alta)= {P_obesa_dado_alta:.3f}")

# f. Calcule la probabilidad de que una persona elegida al azar de este grupo sea 
# alta y de bajo peso.

N_alta_bajo_peso = df.iloc[2,0]
P_alta_bajo_peso = N_alta_bajo_peso/N
print(f"P(alta y bajo peso)= {P_alta_bajo_peso:.3f}")

# g. ¿Los eventos obeso y alto son independientes?
if P_alta_dado_obesa == P_alta:
    print("Los events alto y obeso \"son independientes\"")
else:
    print("Los events alto y obeso \"NO son independientes\"")


