# 13_Temple_Simulado.
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


# Heurística (distancia estimada al Hospital; menor = mejor)
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
    Temple simulado (Simulated Annealing) aplicado a navegación.

    - Empieza con alta 'temperatura' que permite aceptar movimientos peores
      (exploración), y la temperatura va bajando (explotación).
    - A cada paso se toma un vecino aleatorio y se decide si se acepta
      según la diferencia heurística y la temperatura.
    - Parámetros:
      * temperatura_inicial: controla la probabilidad inicial de aceptar peores.
      * factor_enfriamiento: multiplicador para reducir la temperatura.
      * iteraciones_por_nivel: cuántos intentos se hacen antes de enfriar.
    """

    # Estado inicial
    actual = inicio
    mejor = inicio
    mejor_h = h[actual]
    temperatura = temperatura_inicial
    camino = [actual]

    print(f"Iniciando en: {actual} (h={mejor_h})\n")

    # Mientras la temperatura sea lo suficientemente alta, seguimos explorando
    while temperatura > 0.5:
        for _ in range(iteraciones_por_nivel):
            vecinos = grafo.get(actual, [])
            if not vecinos:
                # No hay vecinos desde aquí
                break

            # Elegimos un vecino al azar para probar
            vecino = random.choice(vecinos)
            # Delta: cuánto empeora (o mejora) la heurística
            delta = h[vecino] - h[actual]

            # Si mejora (delta < 0) lo aceptamos. Si empeora, lo aceptamos con
            # probabilidad e^{-delta / T} (más probable a temperaturas altas).
            if delta < 0 or random.random() < math.exp(-delta / temperatura):
                actual = vecino
                camino.append(actual)

                # Si encontramos una heurística mejor, la guardamos
                if h[actual] < mejor_h:
                    mejor = actual
                    mejor_h = h[actual]

                print(f"Temperatura={temperatura:.2f} | Avanzando a {actual} (h={h[actual]})")

            # Si alcanzamos el destino, devolvemos el camino y la mejor heurística
            if actual == destino:
                print("\n¡Destino alcanzado!\n")
                return camino, mejor_h

        # Enfriamos: reducimos la temperatura antes de la siguiente ronda
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
