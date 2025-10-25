# 01_BFS_menos_cruces.py
# GPS Inteligente - Módulo 1: Búsqueda en Anchura (BFS)
# Encuentra la ruta con MENOS CRUCES (no en metros).

from collections import deque
from typing import Dict, List, Optional

Grafo = Dict[str, List[str]]

def bfs_menos_cruces(grafo: Grafo, inicio: str, destino: str) -> Optional[List[str]]:
    """
    BFS clásico en grafo NO ponderado.
    Devuelve la ruta con MENOS aristas (menos cruces/semáforos).
    """
    if inicio == destino:
        return [inicio]

    visitados = set([inicio])
    cola = deque([[inicio]])           # cada elemento es un camino parcial
    while cola:
        camino = cola.popleft()
        nodo = camino[-1]
        for vecino in grafo.get(nodo, []):
            if vecino in visitados:
                continue
            visitados.add(vecino)
            nuevo = camino + [vecino]
            if vecino == destino:
                return nuevo
            cola.append(nuevo)
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

    origen, destino = "Casa", "Hospital"
    ruta = bfs_menos_cruces(ciudad, origen, destino)

    if ruta:
        print("Ruta con MENOS cruces:")
        print("  " + " → ".join(ruta))
        print(f"Cruces totales: {len(ruta)-1}")
    else:
        print("No hay ruta encontrada.")

if __name__ == "__main__":
    demo_ciudad()
