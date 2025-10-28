# 49_Muestreo_Directo_y_Por_Rechazo.py
# GPS Inteligente - Enfoque 7: Razonamiento Probabilístico
# Tema 49 - Muestreo Directo y por Rechazo

import random

# Probabilidades base
P_lluvia = 0.3
P_trafico_dado_lluvia = {True: 0.8, False: 0.2}

# Función para muestreo directo
def muestreo_directo(n_muestras=10000):
    conteo_trafico = 0
    for _ in range(n_muestras):
        lluvia = random.random() < P_lluvia
        trafico = random.random() < P_trafico_dado_lluvia[lluvia]
        if trafico:
            conteo_trafico += 1
    return conteo_trafico / n_muestras

# Función para muestreo por rechazo con evidencia (Lluvia=True)
def muestreo_por_rechazo(n_muestras=10000):
    muestras_validas = 0
    conteo_trafico = 0
    for _ in range(n_muestras):
        lluvia = random.random() < P_lluvia
        trafico = random.random() < P_trafico_dado_lluvia[lluvia]
        # Aceptar solo los casos donde Lluvia=True
        if lluvia:
            muestras_validas += 1
            if trafico:
                conteo_trafico += 1
    return conteo_trafico / muestras_validas if muestras_validas > 0 else 0

directo = muestreo_directo()
rechazo = muestreo_por_rechazo()

print("== MUESTREO DIRECTO Y POR RECHAZO ==")
print(f"Estimación directa de P(Tráfico): {directo:.2f}")
print(f"Estimación por rechazo de P(Tráfico | Lluvia=True): {rechazo:.2f}")
print("\n➡️ El GPS usa simulaciones aleatorias para estimar probabilidades en lugar de cálculos exactos.")
