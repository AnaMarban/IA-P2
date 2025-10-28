# Regla_de_Bayes.
# GPS Inteligente - Enfoque 6: Probabilidad
# Tema - Regla de Bayes

# Probabilidades conocidas
P_lluvia = 0.3
P_no_lluvia = 0.7
P_trafico_dado_lluvia = 0.8
P_trafico_dado_no_lluvia = 0.2

# Calcular la probabilidad total de tráfico
P_trafico = (P_trafico_dado_lluvia * P_lluvia) + (P_trafico_dado_no_lluvia * P_no_lluvia)

# Aplicar la Regla de Bayes:
# P(Lluvia | Tráfico) = [P(Tráfico | Lluvia) * P(Lluvia)] / P(Tráfico)
P_lluvia_dado_trafico = (P_trafico_dado_lluvia * P_lluvia) / P_trafico

# Complemento
P_no_lluvia_dado_trafico = 1 - P_lluvia_dado_trafico

print("== REGLA DE BAYES ==")
print(f"P(Lluvia) = {P_lluvia:.2f}")
print(f"P(Tráfico | Lluvia) = {P_trafico_dado_lluvia:.2f}")
print(f"P(Tráfico | No Lluvia) = {P_trafico_dado_no_lluvia:.2f}")
print(f"P(Lluvia | Tráfico) = {P_lluvia_dado_trafico:.2f}")
print(f"P(No Lluvia | Tráfico) = {P_no_lluvia_dado_trafico:.2f}")
print("\n El GPS razona al revés: ve el efecto (tráfico) y deduce la causa (lluvia).")
