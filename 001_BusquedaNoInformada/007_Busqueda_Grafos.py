# 07_Busqueda_En_Grafos.
# Clase unificadora que permite elegir algoritmo según el tipo de problema.

from typing import Dict, List, Tuple, Optional
from collections import deque  # cola para BFS
import heapq  # cola de prioridad para UCS

# Tipo para grafo ponderado: cada arista es (vecino, costo)
Grafo = Dict[str, List[Tuple[str, int]]]


class BusquedaGrafos:
    """Clase que agrupa varios algoritmos de búsqueda sobre un grafo.

    Métodos incluidos:
    - bfs: búsqueda por anchura que devuelve una ruta con menos aristas.
    - ucs: búsqueda de costo uniforme que devuelve la ruta de menor costo.
    - dfs: búsqueda por profundidad (no garantiza ruta más corta).
    """

    def __init__(self, grafo: Grafo):
        # Guardamos el grafo proporcionado
        self.grafo = grafo

    # BFS (Breadth-First Search)
    def bfs(self, inicio: str, destino: str) -> Optional[List[str]]:
        # Cola de caminos, empezando por el nodo inicio
        cola = deque([[inicio]])
        # Conjunto de visitados para evitar ciclos
        visitados = {inicio}

        while cola:
            camino = cola.popleft()  # sacamos el camino más antiguo (FIFO)
            nodo = camino[-1]        # nodo actual es el último del camino

            # Si llegamos al destino, devolvemos el camino completo
            if nodo == destino:
                return camino

            # Expansión: añadimos vecinos no visitados como nuevos caminos
            for vecino, _ in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(camino + [vecino])

        # Si no encontramos el destino, devolvemos None
        return None

    # UCS (Uniform Cost Search)
    def ucs(self, inicio: str, destino: str) -> Optional[Tuple[List[str], int]]:
        # Cola de prioridad con tuplas (costo_acumulado, camino)
        cola = [(0, [inicio])]
        visitados = set()

        while cola:
            costo, camino = heapq.heappop(cola)  # extrae el camino con menor costo acumulado
            nodo = camino[-1]

            # Si ya procesamos este nodo, lo ignoramos
            if nodo in visitados:
                continue
            visitados.add(nodo)

            # Si es el destino, devolvemos camino y costo total
            if nodo == destino:
                return camino, costo

            # Expandimos vecinos y empujamos nuevos caminos con su costo
            for vecino, peso in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    heapq.heappush(cola, (costo + peso, camino + [vecino]))

        return None

    # DFS simple (iterativa con pila)
    def dfs(self, inicio: str, destino: str) -> Optional[List[str]]:
        pila = [[inicio]]
        visitados = set()

        while pila:
            camino = pila.pop()  # sacamos el último camino (LIFO)
            nodo = camino[-1]

            # Si ya visitamos el nodo, lo saltamos
            if nodo in visitados:
                continue
            visitados.add(nodo)

            # Si es el destino, devolvemos el camino
            if nodo == destino:
                return camino

            # Añadimos vecinos en orden inverso para controlar la expansión
            for vecino, _ in reversed(self.grafo.get(nodo, [])):
                if vecino not in visitados:
                    pila.append(camino + [vecino])

        return None


def demo_grafo_general():
    # Grafo de ejemplo con pesos (por ejemplo, tiempo o distancia)
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
    # Ejecutamos y mostramos los resultados de BFS, UCS y DFS
    print("BFS:", " → ".join(buscador.bfs(origen, destino)))
    ruta, costo = buscador.ucs(origen, destino)
    print(f"UCS: {' → '.join(ruta)} (costo total {costo})")
    print("DFS:", " → ".join(buscador.dfs(origen, destino)))


if __name__ == "__main__":
    demo_grafo_general()
