# 08_Heuristicas.
# Define una función de "intuición" (estimación) para el GPS.

from typing import Dict

# Heurísticas: estimación de distancia al destino (Hospital)
# Entre menor sea el número, más cerca se considera.
heuristica: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 5,
    "Escuela": 4,
    "Parque": 2,
    "Mercado": 7,
    "Hospital": 0
}

def estimar_distancia(ciudad: str) -> int:
    """
    Devuelve el valor heurístico estimado al hospital.
    Si no existe el nodo, devuelve un número grande (infinito simbólico).
    """
    return heuristica.get(ciudad, 999)

def demo_heuristicas():
    print("== Estimaciones heurísticas del GPS Inteligente ==")
    for lugar, valor in heuristica.items():
        print(f"{lugar:10s} -> {valor}")

    print("\nEjemplo: el GPS 'cree' que el Parque está más cerca del Hospital que la Plaza.")
    print(f"h(Parque) = {estimar_distancia('Parque')}")
    print(f"h(Plaza)  = {estimar_distancia('Plaza')}")

if __name__ == "__main__":
    demo_heuristicas()
