# Distribucion_Probabilidad.
# GPS Inteligente - Enfoque 6: Probabilidad
# Tema - Distribución de Probabilidad

# Definir una distribución de probabilidad sobre los estados del tráfico
P_trafico = {
    "Ligero": 0.5,
    "Medio": 0.3,
    "Pesado": 0.2
}

# Verificar que las probabilidades sumen 1
total = sum(P_trafico.values())

# Calcular el tiempo esperado (promedio ponderado)
# Ligero = 10 min, Medio = 20 min, Pesado = 40 min
tiempos = {"Ligero": 10, "Medio": 20, "Pesado": 40}
tiempo_esperado = sum(P_trafico[e] * tiempos[e] for e in P_trafico)

print("== DISTRIBUCIÓN DE PROBABILIDAD ==")
for estado, p in P_trafico.items():
    print(f"P({estado}) = {p:.2f}")

print(f"\nVerificación: Total = {total:.2f}")
print(f"Tiempo esperado de viaje = {tiempo_esperado:.1f} minutos")

print("\n El GPS considera todos los escenarios posibles y calcula un promedio inteligente.")
