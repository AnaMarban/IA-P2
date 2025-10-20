# 13_Temple_Simulado.py
# GPS Inteligente - Módulo 13: Búsqueda de Temple Simulado (Simulated Annealing)
# El GPS "se enfría" poco a poco: al principio explora, luego se estabiliza.

import math
import random
from typing import Dict, List

# Grafo urbano (vecinos)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Casa", "Plaza"],
    "Plaza": ["Av1", "Parque", "Mercado"],
    "Parque": ["Plaza", "Hospital"],
    "Mercado": ["Casa", "Plaza"],
    "Hospital": ["Parque"]
}

# Heurística (distancia estimada al Hospital)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 4,
    "Parque": 2,
    "Mercado": 5,
    "Hospital": 0
}

def simulated_annealing(
    grafo: Dict[str, List[str]],
    inicio: str,
    destino: str,
    temperatura_inicial: float = 10.0,
    factor_enfriamiento: float = 0.9,
    iteraciones_por_nivel: int = 3
):
    """
    Temple simulado: explora caminos aceptando a veces peores soluciones
    según la temperatura.
    """
    actual = inicio
    mejor = inicio
    mejor_h = h[actual]
    temperatura = temperatura_inicial
    camino = [actual]

    print(f"Iniciando en: {actual} (h={mejor_h})\n")

    while temperatura > 0.5:
        for _ in range(iteraciones_por_nivel):
            vecinos = grafo.get(actual, [])
            if not vecinos:
                break

            vecino = random.choice(vecinos)
            delta = h[vecino] - h[actual]

            # Si mejora, lo tomamos; si no, a veces también
            if delta < 0 or random.random() < math.exp(-delta / temperatura):
                actual = vecino
                camino.append(actual)
                if h[actual] < mejor_h:
                    mejor = actual
                    mejor_h = h[actual]
                print(f"Temperatura={temperatura:.2f} | Avanzando a {actual} (h={h[actual]})")

            if actual == destino:
                print("\n¡Destino alcanzado!\n")
                return camino, mejor_h

        # Bajamos la temperatura
        temperatura *= factor_enfriamiento

    print("\nTemperatura muy baja, el GPS se estabiliza.")
    return camino, mejor_h


def demo_temple():
    origen, destino = "Casa", "Hospital"
    camino, heur_final = simulated_annealing(grafo, origen, destino)
    print("Ruta seguida por el GPS:")
    print("  " + " → ".join(camino))
    print(f"Heurística final: {heur_final}")

if __name__ == "__main__":
    demo_temple()
