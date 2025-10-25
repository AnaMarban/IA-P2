# 06_Busqueda_Bidireccional.py
# GPS Inteligente - Módulo 6: Búsqueda Bidireccional (BBFS)
# Explora simultáneamente desde el origen y el destino.

from collections import deque
from typing import Dict, List, Optional, Set

Grafo = Dict[str, List[str]]

def bidirectional_bfs(grafo: Grafo, inicio: str, destino: str) -> Optional[List[str]]:
    if inicio == destino:
        return [inicio]

    # Colas de búsqueda desde ambos lados
    cola_inicio = deque([[inicio]])
    cola_destino = deque([[destino]])

    # Visitados
    visitados_inicio: Set[str] = {inicio}
    visitados_destino: Set[str] = {destino}

    # Mapas de padres (para reconstruir camino)
    padres_inicio = {inicio: None}
    padres_destino = {destino: None}

    while cola_inicio and cola_destino:
        # Expandir desde el lado de inicio
        camino = cola_inicio.popleft()
        nodo = camino[-1]

        for vecino in grafo.get(nodo, []):
            if vecino not in visitados_inicio:
                visitados_inicio.add(vecino)
                padres_inicio[vecino] = nodo
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola_inicio.append(nuevo_camino)

                # ¿Se cruzaron?
                if vecino in visitados_destino:
                    return reconstruir_camino(padres_inicio, padres_destino, vecino)

        # Expandir desde el lado de destino
        camino = cola_destino.popleft()
        nodo = camino[-1]

        for vecino in grafo.get(nodo, []):
            if vecino not in visitados_destino:
                visitados_destino.add(vecino)
                padres_destino[vecino] = nodo
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola_destino.append(nuevo_camino)

                if vecino in visitados_inicio:
                    return reconstruir_camino(padres_inicio, padres_destino, vecino)

    return None


def reconstruir_camino(padres_inicio: Dict[str, Optional[str]], padres_destino: Dict[str, Optional[str]], nodo_encontrado: str) -> List[str]:
    # Parte 1: reconstruye desde inicio hasta el punto medio
    camino_inicio = []
    n = nodo_encontrado
    while n is not None:
        camino_inicio.append(n)
        n = padres_inicio[n]
    camino_inicio.reverse()

    # Parte 2: reconstruye desde el punto medio hasta el destino
    camino_destino = []
    n = padres_destino[nodo_encontrado]
    while n is not None:
        camino_destino.append(n)
        n = padres_destino[n]
    return camino_inicio + camino_destino


def demo_bidireccional():
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
