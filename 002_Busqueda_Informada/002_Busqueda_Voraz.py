# 09_Voraz_PrimeroElMejor.
# El GPS elige siempre el camino que parece más cercano al destino según la heurística (Greedy Best-First).

from typing import Dict, List, Optional  # tipos para anotaciones
import heapq  # cola de prioridad para seleccionar el nodo con menor heurística


# Mapa de ciudad (grafo no ponderado: cada arista cuenta como 1 paso)
grafo: Dict[str, List[str]] = {
    "Casa":    ["Av1", "Mercado"],
    "Av1":     ["Casa", "Plaza", "Parque"],
    "Plaza":   ["Av1", "Escuela"],
    "Parque":  ["Av1", "Hospital"],
    "Mercado": ["Casa"],
    "Escuela": ["Plaza"],
    "Hospital": ["Parque"]
}


# Heurística: estimación (h) de la distancia restante al Hospital
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
    Implementa búsqueda Voraz (Greedy Best-First).

    Idea: siempre expandir el nodo cuya heurística h(n) es la menor
    (el que 'parece' más cercano al objetivo según la heurística).


    """

    # Cola de prioridad donde la prioridad es el valor heurístico del último nodo del camino
    cola = [(h[inicio], [inicio])]   # (heurística, camino)
    visitados = set()

    while cola:
        heur, camino = heapq.heappop(cola)  # extrae el camino con menor h
        nodo = camino[-1]

        # Si ya procesamos este nodo, lo ignoramos
        if nodo in visitados:
            continue
        visitados.add(nodo)

        # Si es el destino, devolvemos el camino construido
        if nodo == destino:
            return camino

        # Si no es destino, empujamos sus vecinos con prioridad según su heurística
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(cola, (h[vecino], camino + [vecino]))

    # Si agotamos la cola sin encontrar destino, no hay ruta
    return None


def demo_greedy():
    # Demo: origen y destino para la prueba
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
