# Probabilidad_Condicionada_Normalizacion.
# GPS Inteligente - Enfoque 6: Probabilidad
# Tema - Probabilidad Condicionada y Normalización

# Datos iniciales
P_trafico = 0.7
P_no_trafico = 0.3
P_lluvia_dado_trafico = 0.6
P_lluvia_dado_no_trafico = 0.2

# Calcular P(lluvia)
P_lluvia = (P_lluvia_dado_trafico * P_trafico) + (P_lluvia_dado_no_trafico * P_no_trafico)

# Ahora queremos: P(trafico | lluvia)
P_trafico_dado_lluvia = (P_lluvia_dado_trafico * P_trafico) / P_lluvia

# Y también: P(no_trafico | lluvia)
P_no_trafico_dado_lluvia = (P_lluvia_dado_no_trafico * P_no_trafico) / P_lluvia

# Normalización (solo para mostrar cómo los valores suman 1)
total = P_trafico_dado_lluvia + P_no_trafico_dado_lluvia
P_trafico_dado_lluvia /= total
P_no_trafico_dado_lluvia /= total

print("== PROBABILIDAD CONDICIONADA Y NORMALIZACIÓN ==")
print(f"P(Lluvia) = {P_lluvia:.2f}")
print(f"P(Tráfico | Lluvia) = {P_trafico_dado_lluvia:.2f}")
print(f"P(No Tráfico | Lluvia) = {P_no_trafico_dado_lluvia:.2f}")
print("\n➡️ El GPS ajusta sus creencias con base en nueva evidencia (lluvia detectada).")
