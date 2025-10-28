# Red_Bayesiana.
# GPS Inteligente - Enfoque 7: Razonamiento Probabilístico
# Tema - Red Bayesiana

# Representación simple de una Red Bayesiana
# Ejemplo: Lluvia → Tráfico ← Accidente

# Probabilidades base (a priori)
P_lluvia = 0.3
P_accidente = 0.1

# Probabilidades condicionales de tráfico
P_trafico = {
    (True, True): 0.95,   # Si llueve y hay accidente
    (True, False): 0.80,  # Si llueve y no hay accidente
    (False, True): 0.70,  # Si no llueve y hay accidente
    (False, False): 0.10  # Si no llueve ni hay accidente
}

# Enumerar todos los casos posibles para calcular P(Trafico)
P_trafico_total = 0
casos = [(True, True), (True, False), (False, True), (False, False)]

for lluvia, accidente in casos:
    p_caso = (
        (P_lluvia if lluvia else 1 - P_lluvia)
        * (P_accidente if accidente else 1 - P_accidente)
        * P_trafico[(lluvia, accidente)]
    )
    P_trafico_total += p_caso

print("== RED BAYESIANA ==")
print("Nodos: Lluvia, Accidente, Tráfico")
print(f"P(Tráfico) = {P_trafico_total:.2f}")
print("\n➡️ El GPS combina causas (lluvia y accidentes) para inferir probabilidades del tráfico.")
