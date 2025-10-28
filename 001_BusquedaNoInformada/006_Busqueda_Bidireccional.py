# 06_Busqueda_Bidireccional.
# Explora simultáneamente desde el origen y el destino para encontrar un punto de encuentro.

from collections import deque  # deque: cola eficiente para BFS
from typing import Dict, List, Optional, Set  # tipos usados en las anotaciones

# Tipo para representar el grafo: nodo -> lista de vecinos
Grafo = Dict[str, List[str]]


def bidirectional_bfs(grafo: Grafo, inicio: str, destino: str) -> Optional[List[str]]:
    """Búsqueda bidireccional usando BFS desde inicio y destino.

    Devuelve una lista de nodos representando el camino encontrado, o None si no hay ruta.
    """
    # Caso trivial: origen == destino
    if inicio == destino:
        return [inicio]

    # Colas de búsqueda (cada elemento es un camino parcial)
    cola_inicio = deque([[inicio]])
    cola_destino = deque([[destino]])

    # Conjuntos de nodos visitados desde cada lado
    visitados_inicio: Set[str] = {inicio}
    visitados_destino: Set[str] = {destino}

    # Mapas de padres para reconstruir el camino cuando se crucen las búsquedas
    padres_inicio = {inicio: None}
    padres_destino = {destino: None}

    # Mientras ambos frentes tengan nodos por explorar
    while cola_inicio and cola_destino:
        # --- Expandir desde el lado del inicio ---
        camino = cola_inicio.popleft()
        nodo = camino[-1]

        # Recorremos vecinos del nodo actual
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados_inicio:
                # Marcamos y guardamos el padre para reconstrucción
                visitados_inicio.add(vecino)
                padres_inicio[vecino] = nodo

                # Construimos y encolamos el nuevo camino parcial
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola_inicio.append(nuevo_camino)

                # Si el nodo aparece en el frente contrario, hemos encontrado intersección
                if vecino in visitados_destino:
                    return reconstruir_camino(padres_inicio, padres_destino, vecino)

        # --- Ahora expandimos desde el lado del destino ---
        camino = cola_destino.popleft()
        nodo = camino[-1]

        for vecino in grafo.get(nodo, []):
            if vecino not in visitados_destino:
                visitados_destino.add(vecino)
                padres_destino[vecino] = nodo
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola_destino.append(nuevo_camino)

                # Comprobamos intersección con el frente de inicio
                if vecino in visitados_inicio:
                    return reconstruir_camino(padres_inicio, padres_destino, vecino)

    # Si alguna cola se vacía sin intersección, no hay ruta
    return None


def reconstruir_camino(padres_inicio: Dict[str, Optional[str]], padres_destino: Dict[str, Optional[str]], nodo_encontrado: str) -> List[str]:
    """Reconstruye el camino completo a partir de los mapas de padres y el nodo de intersección.

    - Reconstruye la parte desde el inicio hasta 'nodo_encontrado' usando padres_inicio.
    - Reconstruye la parte desde el nodo_encontrado hasta el destino usando padres_destino.
    """
    # Parte 1: reconstruye desde inicio hasta el punto medio (incluye nodo_encontrado)
    camino_inicio = []
    n = nodo_encontrado
    while n is not None:
        camino_inicio.append(n)
        n = padres_inicio[n]
    camino_inicio.reverse()  # invertir para ir desde inicio -> punto medio

    # Parte 2: reconstruye desde el punto medio (excluyendo nodo_encontrado) hasta el destino
    camino_destino = []
    # Empezamos desde el padre del nodo_encontrado en el mapa destino (evita duplicar nodo_encontrado)
    n = padres_destino[nodo_encontrado]
    while n is not None:
        camino_destino.append(n)
        n = padres_destino[n]

    # Concatenamos la primera parte con la segunda para obtener el camino completo
    return camino_inicio + camino_destino


def demo_bidireccional():
    # Grafo de ejemplo (ciudad) con conexiones
    ciudad: Grafo = {
        "Casa":    ["Av1", "Mercado"],
        "Av1":     ["Casa", "Plaza", "Parque"],
        "Plaza":   ["Av1", "Escuela"],
        "Parque":  ["Av1", "Hospital"],
        "Mercado": ["Casa"],
        "Escuela": ["Plaza"],
        "Hospital": ["Parque"]
    }

    origen, destino = "Casa", "Hospital"
    ruta = bidirectional_bfs(ciudad, origen, destino)

    print("== Búsqueda Bidireccional ==")
    if ruta:
        print("Ruta encontrada:", " → ".join(ruta))
        print(f"Total de cruces: {len(ruta)-1}")
    else:
        print("No hay ruta disponible.")


if __name__ == "__main__":
    demo_bidireccional()
