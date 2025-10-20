# 09_Voraz_PrimeroElMejor.py
# GPS Inteligente - Módulo 9: Búsqueda Voraz Primero el Mejor (Greedy Best-First Search)
# El GPS elige siempre el camino que parece más cercano al destino según la heurística.

from typing import Dict, List, Optional
import heapq

# Mapa de ciudad (sin pesos, cada calle = 1 cruce)
grafo: Dict[str, List[str]] = {
    "Casa":    ["Av1", "Mercado"],
    "Av1":     ["Casa", "Plaza", "Parque"],
    "Plaza":   ["Av1", "Escuela"],
    "Parque":  ["Av1", "Hospital"],
    "Mercado": ["Casa"],
    "Escuela": ["Plaza"],
    "Hospital": ["Parque"]
}

# Heurística: estimación de distancia al Hospital
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 5,
    "Escuela": 4,
    "Parque": 2,
    "Mercado": 7,
    "Hospital": 0
}

def greedy_best_first(grafo: Dict[str, List[str]], inicio: str, destino: str) -> Optional[List[str]]:
    """
    Implementa búsqueda Voraz Primero el Mejor (Greedy Best-First).
    Siempre expande el nodo con menor heurística (h).
    """
    cola = [(h[inicio], [inicio])]   # (heurística, camino)
    visitados = set()

    while cola:
        heur, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == destino:
            return camino

        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(cola, (h[vecino], camino + [vecino]))

    return None

def demo_greedy():
    origen, destino = "Casa", "Hospital"
    ruta = greedy_best_first(grafo, origen, destino)

    print("== Búsqueda Voraz Primero el Mejor ==")
    if ruta:
        print("Ruta elegida por el GPS (intuición):")
        print("  " + " → ".join(ruta))
        print(f"Pasos recorridos: {len(ruta)-1}")
    else:
        print("No hay ruta al destino.")

if __name__ == "__main__":
    demo_greedy()
