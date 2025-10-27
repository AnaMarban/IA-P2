# 12_Busqueda_Tabu.
# El GPS recuerda caminos malos para no repetirlos.

from typing import Dict, List, Tuple
import random

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

def busqueda_tabu(
    grafo: Dict[str, List[str]], 
    inicio: str, 
    destino: str, 
    max_iteraciones: int = 15, 
    tamano_tabu: int = 3
) -> Tuple[List[str], int]:
    """
    Implementación simple de Búsqueda Tabú.
    Busca mejorar la heurística paso a paso, evitando movimientos prohibidos.
    """
    actual = inicio
    mejor = inicio
    mejor_h = h[actual]
    lista_tabu = []
    camino = [actual]

    print(f"Iniciando en: {actual} (h={mejor_h})")

    for i in range(max_iteraciones):
        vecinos = grafo.get(actual, [])
        if not vecinos:
            print("Sin vecinos para continuar.")
            break

        # Evaluar vecinos (no tabú)
        vecinos_validos = [v for v in vecinos if v not in lista_tabu]
        if not vecinos_validos:
            print("Todos los vecinos son tabú, el GPS se detiene.")
            break

        # Escoger el mejor vecino (menor heurística)
        siguiente = min(vecinos_validos, key=lambda n: h[n])
        actual_h = h[siguiente]

        print(f"Iteración {i+1}: {actual} → {siguiente} (h={actual_h})")

        # Actualizar mejor ruta si mejora
        if actual_h < mejor_h:
            mejor = siguiente
            mejor_h = actual_h

        camino.append(siguiente)

        # Actualizar lista tabú (últimos movimientos)
        lista_tabu.append(actual)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)

        # Mover al siguiente
        actual = siguiente

        if actual == destino:
            print("¡Destino alcanzado!")
            break

    return camino, mejor_h

def demo_tabu():
    origen, destino = "Casa", "Hospital"
    camino, heur_final = busqueda_tabu(grafo, origen, destino)

    print("\nRuta seguida por el GPS:")
    print("  " + " → ".join(camino))
    print(f"Heurística final: {heur_final}")

if __name__ == "__main__":
    demo_tabu()
