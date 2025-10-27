# 31_Red_Bayesiana_Dinamica.
# GPS Inteligente - Enfoque 4: Utilidad y Toma de Decisiones
# Tema 31 - Red Bayesiana Dinámica (DBN)

from typing import Dict

# Probabilidades iniciales (Paso 0)
P_clima = {"Soleado": 0.7, "Lluvioso": 0.3}
P_trafico_dado_clima = {
    "Soleado": {"Ligero": 0.7, "Medio": 0.2, "Pesado": 0.1},
    "Lluvioso": {"Ligero": 0.1, "Medio": 0.3, "Pesado": 0.6}
}

# Probabilidad de transición entre tiempos consecutivos
P_trafico_t1_dado_t0 = {
    "Ligero": {"Ligero": 0.6, "Medio": 0.3, "Pesado": 0.1},
    "Medio": {"Ligero": 0.2, "Medio": 0.5, "Pesado": 0.3},
    "Pesado": {"Ligero": 0.1, "Medio": 0.3, "Pesado": 0.6}
}

def predecir_trafico(inicial: Dict[str, float], pasos: int) -> Dict[str, float]:
    """Predice el estado del tráfico después de varios pasos."""
    actual = inicial.copy()
    for t in range(pasos):
        siguiente = {"Ligero": 0, "Medio": 0, "Pesado": 0}
        for estado0, prob0 in actual.items():
            for estado1, prob1 in P_trafico_t1_dado_t0[estado0].items():
                siguiente[estado1] += prob0 * prob1
        actual = siguiente
        print(f"⏱️ Paso {t+1}: {actual}")
    return actual

def demo_dbn():
    print("== Red Bayesiana Dinámica ==")
    print("Probabilidad inicial del tráfico (dado clima):")
    inicial = {
        estado: sum(P_clima[c] * P_trafico_dado_clima[c][estado] for c in P_clima)
        for estado in ["Ligero", "Medio", "Pesado"]
    }
    print(f"t=0: {inicial}\n")

    predecir_trafico(inicial, pasos=3)

if __name__ == "__main__":
    demo_dbn()
