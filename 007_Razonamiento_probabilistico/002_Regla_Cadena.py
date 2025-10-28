# Regla_de_la_Cadena.
# GPS Inteligente - Enfoque 7: Razonamiento Probabilístico
# Tema - Regla de la Cadena

# Probabilidades base
P_lluvia = 0.3                # P(L)
P_trafico_dado_lluvia = 0.8   # P(T | L)
P_accidente_dado_TL = 0.6     # P(A | T, L)

# Aplicar la Regla de la Cadena:
# P(L, T, A) = P(A | T, L) * P(T | L) * P(L)
P_conjunta = P_accidente_dado_TL * P_trafico_dado_lluvia * P_lluvia

print("== REGLA DE LA CADENA ==")
print(f"P(Lluvia) = {P_lluvia}")
print(f"P(Tráfico | Lluvia) = {P_trafico_dado_lluvia}")
print(f"P(Accidente | Tráfico, Lluvia) = {P_accidente_dado_TL}")
print(f"\nP(Lluvia, Tráfico, Accidente) = {P_conjunta:.3f}")

print("\n La Regla de la Cadena permite calcular probabilidades conjuntas de manera paso a paso.")
