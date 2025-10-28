# 01_BFS_menos_cruces.
# Encuentra la ruta con MENOS CRUCES (no en metros).

from collections import deque   # deque: cola eficiente para BFS
from typing import Dict, List, Optional  # tipos para anotaciones

Grafo = Dict[str, List[str]]  # tipo: un grafo es un diccionario nodo -> lista de vecinos


def bfs_menos_cruces(grafo: Grafo, inicio: str, destino: str) -> Optional[List[str]]:
    """
    BFS clásico en grafo NO ponderado.
    Devuelve la ruta con MENOS aristas (menos cruces/semáforos).
    """
    # Si inicio y destino son el mismo nodo, la ruta es sólo ese nodo
    if inicio == destino:
        return [inicio]

    # Conjunto de nodos ya visitados para evitar ciclos
    visitados = set([inicio])

    # Cola de caminos; cada elemento es una lista que representa el camino desde inicio
    cola = deque([[inicio]])           # cada elemento es un camino parcial

    # Mientras haya caminos pendientes por explorar
    while cola:
        camino = cola.popleft()        # sacamos el camino más antiguo (FIFO)
        nodo = camino[-1]              # último nodo del camino actual

        # Iteramos sobre los vecinos del nodo actual
        for vecino in grafo.get(nodo, []):
            # Si ya visitamos el vecino, lo saltamos
            if vecino in visitados:
                continue

            # Marcamos el vecino como visitado
            visitados.add(vecino)

            # Construimos un nuevo camino que añade al vecino
            nuevo = camino + [vecino]

            # Si el vecino es el destino, devolvemos el camino completo
            if vecino == destino:
                return nuevo

            # Si no es el destino, añadimos el nuevo camino a la cola para seguir explorando
            cola.append(nuevo)

    # Si agotamos la cola y no encontramos el destino, no hay ruta
    return None


def demo_ciudad():
    # Mapa de ciudad (no ponderado: cada calle "cuesta" 1 cruce)
    ciudad: Grafo = {
        "Casa":     ["Av1", "Parque"],
        "Av1":      ["Casa", "Plaza", "Parque"],
        "Plaza":    ["Av1", "Escuela", "Mercado"],
        "Parque":   ["Casa", "Av1", "Hospital"],
        "Mercado":  ["Plaza", "Hospital"],
        "Escuela":  ["Plaza"],
        "Hospital": ["Parque", "Mercado"],
    }

    # Definimos origen y destino para la demostración
    origen, destino = "Casa", "Hospital"

    # Ejecutamos la búsqueda BFS para obtener la ruta con menos cruces
    ruta = bfs_menos_cruces(ciudad, origen, destino)

    # Si hay ruta, la imprimimos y mostramos el número de cruces (aristas)
    if ruta:
        print("Ruta con MENOS cruces:")
        print("  " + " → ".join(ruta))  # mostramos la secuencia de nodos
        print(f"Cruces totales: {len(ruta)-1}")  # cruces = aristas = longitud-1
    else:
        # Si no se encontró ninguna ruta, avisamos
        print("No hay ruta encontrada.")


if __name__ == "__main__":
    demo_ciudad()
