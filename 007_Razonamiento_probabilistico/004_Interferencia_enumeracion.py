# Inferencia_por_Enumeracion.py
# GPS Inteligente - Enfoque 7: Razonamiento Probabilístico
# Tema - Inferencia por Enumeración

import itertools

# Variables: Lluvia, Tráfico, Accidente
# Probabilidades base
P_lluvia = {True: 0.3, False: 0.7}
P_trafico_dado_lluvia = {True: 0.8, False: 0.2}
P_accidente_dado_trafico = {True: 0.6, False: 0.1}

# Calcular P(T, A, L) recorriendo todos los mundos posibles
def P_conjunta(L, T, A):
    pL = P_lluvia[L]
    pT = P_trafico_dado_lluvia[L] if T else 1 - P_trafico_dado_lluvia[L]
    pA = P_accidente_dado_trafico[T] if A else 1 - P_accidente_dado_trafico[T]
    return pL * pT * pA

# Inferencia por enumeración: P(T | L=True)
def inferencia_enumeracion():
    mundos = list(itertools.product([True, False], repeat=3))  # L, T, A
    numerador = 0
    denominador = 0

    for L, T, A in mundos:
        p = P_conjunta(L, T, A)
        if L:  # Lluvia = True
            denominador += p
            if T:  # Tráfico = True
                numerador += p

    P_T_dado_L = numerador / denominador
    return P_T_dado_L

resultado = inferencia_enumeracion()

print("== INFERENCIA POR ENUMERACIÓN ==")
print(f"P(Tráfico | Lluvia) = {resultado:.2f}")
print("\n El GPS recorre todas las combinaciones posibles y calcula la probabilidad exacta.")
