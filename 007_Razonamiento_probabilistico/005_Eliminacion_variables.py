# Eliminacion_de_Variables.py
# GPS Inteligente - Enfoque 7: Razonamiento Probabilístico
# Tema - Eliminación de Variables

# Variables: Lluvia (L), Tráfico (T), Accidente (A)

# Probabilidades base
P_lluvia = {True: 0.3, False: 0.7}
P_trafico_dado_lluvia = {True: 0.8, False: 0.2}
P_accidente_dado_trafico = {True: 0.6, False: 0.1}

# Función para calcular la probabilidad conjunta P(T, A | L)
def P_TA_dado_L(T, L):
    # Eliminar variable A (sumando sobre sus valores True/False)
    P_total = 0
    for A in [True, False]:
        pA_dado_T = P_accidente_dado_trafico[T] if A else 1 - P_accidente_dado_trafico[T]
        P_total += pA_dado_T
    P_total *= P_trafico_dado_lluvia[L] if T else (1 - P_trafico_dado_lluvia[L])
    return P_total

# Normalizar P(T | L)
def P_T_dado_L(L):
    p_true = P_TA_dado_L(True, L)
    p_false = P_TA_dado_L(False, L)
    normal = p_true + p_false
    return {"True": p_true / normal, "False": p_false / normal}

resultado = P_T_dado_L(True)

print("== ELIMINACIÓN DE VARIABLES ==")
print(f"P(Tráfico | Lluvia=True) = {resultado['True']:.2f}")
print(f"P(No Tráfico | Lluvia=True) = {resultado['False']:.2f}")
print("\n El GPS ignora las variables innecesarias (como 'Accidente') y calcula eficientemente.")
