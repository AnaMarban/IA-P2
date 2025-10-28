# Independencia_Condicional.
# GPS Inteligente - Enfoque 6: Probabilidad
# Tema - Independencia Condicional

# Probabilidades simples
P_clima = {"Soleado": 0.6, "Lluvioso": 0.4}

# Probabilidad de tráfico según clima
P_trafico_dado_clima = {"Soleado": 0.3, "Lluvioso": 0.8}

# Probabilidad de accidente según clima (no depende del tráfico)
P_accidente_dado_clima = {"Soleado": 0.1, "Lluvioso": 0.4}

# Calcular P(accidente y tráfico) dado el clima
for clima in P_clima:
    P_trafico = P_trafico_dado_clima[clima]
    P_accidente = P_accidente_dado_clima[clima]
    conjunto = P_trafico * P_accidente  # como son independientes dado el clima
    print(f"{clima}: P(Tráfico y Accidente | {clima}) = {conjunto:.2f}")

print("\n➡️ Dado que ya conocemos el clima, los eventos 'Tráfico' y 'Accidente' son independientes.")
