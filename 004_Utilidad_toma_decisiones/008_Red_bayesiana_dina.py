# 31_Red_Bayesiana_Dinamica.
# GPS Inteligente - Enfoque 4: Utilidad y Toma de Decisiones
# Tema 31 - Red Bayesiana Dinámica (DBN)

from typing import Dict

# Diccionario de probabilidades iniciales del clima
P_clima = {"Soleado": 0.7, "Lluvioso": 0.3}
# Diccionario de probabilidades del tráfico dado el clima
P_trafico_dado_clima = {
    "Soleado": {"Ligero": 0.7, "Medio": 0.2, "Pesado": 0.1},
    "Lluvioso": {"Ligero": 0.1, "Medio": 0.3, "Pesado": 0.6}
}

# Diccionario de probabilidades de transición del tráfico entre tiempos consecutivos
P_trafico_t1_dado_t0 = {
    "Ligero": {"Ligero": 0.6, "Medio": 0.3, "Pesado": 0.1},
    "Medio": {"Ligero": 0.2, "Medio": 0.5, "Pesado": 0.3},
    "Pesado": {"Ligero": 0.1, "Medio": 0.3, "Pesado": 0.6}
}

def predecir_trafico(inicial: Dict[str, float], pasos: int) -> Dict[str, float]:
    """
    Predice la distribución de probabilidad del tráfico después de varios pasos,
    usando la matriz de transición de la red bayesiana dinámica.
    """
    actual = inicial.copy()  # Estado inicial de las probabilidades
    for t in range(pasos):
        siguiente = {"Ligero": 0, "Medio": 0, "Pesado": 0}  # Inicializa el siguiente estado
        for estado0, prob0 in actual.items():
            for estado1, prob1 in P_trafico_t1_dado_t0[estado0].items():
                siguiente[estado1] += prob0 * prob1  # Actualiza la probabilidad para cada estado
        actual = siguiente  # Avanza al siguiente paso
        print(f" Paso {t+1}: {actual}")
    return actual

def demo_dbn():
    print("== Red Bayesiana Dinámica ==")
    print("Probabilidad inicial del tráfico (dado clima):")
    # Calcula la probabilidad inicial del tráfico combinando clima y tráfico dado clima
    inicial = {
        estado: sum(P_clima[c] * P_trafico_dado_clima[c][estado] for c in P_clima)
        for estado in ["Ligero", "Medio", "Pesado"]
    }
    print(f"t=0: {inicial}\n")

    predecir_trafico(inicial, pasos=3)  # Predice la evolución del tráfico en 3 pasos

if __name__ == "__main__":
    demo_dbn()
