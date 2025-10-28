# 08_Heuristicas.
# Define una función de "intuición" (estimación) usada por algoritmos informados (p. ej. A*).

from typing import Dict  # tipo para el diccionario de heurísticas

# Heurísticas: estimación (número) de la distancia al destino (aquí: 'Hospital').
# Valores más pequeños significan "más cerca" según la heurística.
heuristica: Dict[str, int] = {
    "Casa": 8,      # el GPS estima que Casa está relativamente lejos
    "Av1": 6,
    "Plaza": 5,
    "Escuela": 4,
    "Parque": 2,    # Parque está estimado como bastante cerca del Hospital
    "Mercado": 7,
    "Hospital": 0   # destino: distancia heurística 0
}


def estimar_distancia(ciudad: str) -> int:
    """
    Devuelve el valor heurístico estimado desde 'ciudad' hasta el Hospital.

    - Si el nodo aparece en el diccionario 'heuristica', devolvemos ese valor.
    - Si no está presente, devolvemos 999 como "infinito simbólico" para indicar
      que la estimación es desconocida y muy grande.
    """
    return heuristica.get(ciudad, 999)


def demo_heuristicas():
    """Pequeña demo que imprime las heurísticas y ejemplos de uso."""
    print("== Estimaciones heurísticas del GPS Inteligente ==")

    # Mostramos cada lugar y su valor heurístico
    for lugar, valor in heuristica.items():
        print(f"{lugar:10s} -> {valor}")

    # Ejemplo explicativo: comparar estimaciones entre dos nodos
    print("\nEjemplo: el GPS 'cree' que el Parque está más cerca del Hospital que la Plaza.")
    print(f"h(Parque) = {estimar_distancia('Parque')}")
    print(f"h(Plaza)  = {estimar_distancia('Plaza')}")


if __name__ == "__main__":
    demo_heuristicas()
