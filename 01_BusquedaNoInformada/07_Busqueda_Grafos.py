# 07_Busqueda_En_Grafos.py
# GPS Inteligente - Módulo 7: Búsqueda en Grafos (general)
# Clase unificadora que permite elegir algoritmo según el tipo de problema.

from typing import Dict, List, Tuple, Optional
from collections import deque
import heapq

Grafo = Dict[str, List[Tuple[str, int]]]

class BusquedaGrafos:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    # BFS
    def bfs(self, inicio: str, destino: str) -> Optional[List[str]]:
        cola = deque([[inicio]])
        visitados = {inicio}
        while cola:
            camino = cola.popleft()
            nodo = camino[-1]
            if nodo == destino:
                return camino
            for vecino, _ in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(camino + [vecino])
        return None

    # UCS
    def ucs(self, inicio: str, destino: str) -> Optional[Tuple[List[str], int]]:
        cola = [(0, [inicio])]
        visitados = set()
        while cola:
            costo, camino = heapq.heappop(cola)
            nodo = camino[-1]
            if nodo in visitados:
                continue
            visitados.add(nodo)
            if nodo == destino:
                return camino, costo
            for vecino, peso in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    heapq.heappush(cola, (costo + peso, camino + [vecino]))
        return None

    # DFS simple
    def dfs(self, inicio: str, destino: str) -> Optional[List[str]]:
        pila = [[inicio]]
        visitados = set()
        while pila:
            camino = pila.pop()
            nodo = camino[-1]
            if nodo in visitados:
                continue
            visitados.add(nodo)
            if nodo == destino:
                return camino
            for vecino, _ in reversed(self.grafo.get(nodo, [])):
                if vecino not in visitados:
                    pila.append(camino + [vecino])
        return None


def demo_grafo_general():
    ciudad: Grafo = {
        "Casa":     [("Av1", 4), ("Parque", 3)],
        "Av1":      [("Casa", 4), ("Plaza", 2), ("Parque", 5)],
        "Plaza":    [("Av1", 2), ("Escuela", 6), ("Mercado", 4)],
        "Parque":   [("Casa", 3), ("Av1", 5), ("Hospital", 2), ("Mercado", 8)],
        "Mercado":  [("Plaza", 4), ("Parque", 8), ("Hospital", 3)],
        "Escuela":  [("Plaza", 6)],
        "Hospital": [("Parque", 2), ("Mercado", 3)]
    }

    buscador = BusquedaGrafos(ciudad)
    origen, destino = "Casa", "Hospital"

    print("== Búsqueda General en Grafos ==")
    print("BFS:", " → ".join(buscador.bfs(origen, destino)))
    ruta, costo = buscador.ucs(origen, destino)
    print(f"UCS: {' → '.join(ruta)} (costo total {costo})")
    print("DFS:", " → ".join(buscador.dfs(origen, destino)))

if __name__ == "__main__":
    demo_grafo_general()
