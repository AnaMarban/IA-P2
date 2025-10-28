# Ponderacion_de_Verosimilitud.py
# GPS Inteligente - Enfoque 7: Razonamiento Probabilístico
# Tema - Ponderación de Verosimilitud (Likelihood Weighting)

import random

# Probabilidades base
P_lluvia = 0.3
P_trafico_dado_lluvia = {True: 0.8, False: 0.2}
P_accidente_dado_trafico = {True: 0.6, False: 0.1}

# Evidencia: ocurrió un accidente
EVIDENCIA_ACCIDENTE = True

# Función de muestreo con ponderación
def ponderacion_verosimilitud(n_muestras=10000):
    pesos_trafico = {True: 0, False: 0}
    for _ in range(n_muestras):
        # Muestreo de variables no evidenciales
        lluvia = random.random() < P_lluvia
        trafico = random.random() < P_trafico_dado_lluvia[lluvia]

        # Asignar peso según la evidencia (P(A | T))
        peso = P_accidente_dado_trafico[trafico] if EVIDENCIA_ACCIDENTE else (1 - P_accidente_dado_trafico[trafico])
        
        # Acumular pesos
        pesos_trafico[trafico] += peso

    # Normalizar
    total = pesos_trafico[True] + pesos_trafico[False]
    P_T_dado_A = pesos_trafico[True] / total
    return P_T_dado_A

resultado = ponderacion_verosimilitud()

print("== PONDERACIÓN DE VEROSIMILITUD ==")
print(f"P(Tráfico | Accidente=True) ≈ {resultado:.2f}")
print("\n El GPS asigna más peso a los mundos donde la evidencia (accidente) tiene más sentido.")
