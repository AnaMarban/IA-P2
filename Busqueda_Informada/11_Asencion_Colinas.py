# 11_Ascension_Colinas.py
# GPS Inteligente - Módulo 11: Búsqueda de Ascensión de Colinas (Hill Climbing)
# El GPS sube "colinas" eligiendo siempre el vecino con mejor heurística.

from typing import Dict, List, Optional
import random

# Grafo (con conexiones simples)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Plaza", "Casa"],
    "Mercado": ["Plaza"],
    "Plaza": ["Parque"],
    "Parque": ["Hospital"],
    "Hospital": []
}

# Heurística (distancia estimada al hospital, menor = mejor)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Mercado": 7,
    "Plaza": 5,
    "Parque": 2,
    "Hospital": 0
}

def hill_climbing(grafo: Dict[str, List[str]], inicio: str, destino: str) -> List[str]:
    """
    Búsqueda por Ascensión de Colinas.
    Siempre se mueve hacia el vecino con mejor heurística (menor h).
    Si ningún vecino mejora, se detiene (posible máximo local).
    """
    actual = inicio
    camino = [actual]

    print(f"Iniciando en: {actual} (h={h[actual]})")

    while True:
        vecinos = grafo.get(actual, [])
        if not vecinos:
            print("No hay más caminos.")
            break

        # Buscar vecino con menor heurística
        mejor_vecino = min(vecinos, key=lambda n: h[n])
        if h[mejor_vecino] < h[actual]:
            actual = mejor_vecino
            camino.append(actual)
            print(f"→ Avanzando a {actual} (h={h[actual]})")
        else:
            print(f"Sin mejora desde {actual}. GPS detenido en un máximo local.")
            break

        if actual == destino:
            print("¡Destino alcanzado!")
            break

    return camino

def demo_colinas():
    origen, destino = "Casa", "Hospital"
    camino = hill_climbing(grafo, origen, destino)
    print("\nRuta seguida por el GPS:")
    print("  " + " → ".join(camino))
    print(f"Heurística final: {h[camino[-1]]}")

if __name__ == "__main__":
    demo_colinas()
