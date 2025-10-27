# 03_DFS_explorador_profundo.
# Explora una ruta hasta el fondo antes de retroceder.

from typing import Dict, List, Optional

Grafo = Dict[str, List[str]]

def dfs_en_profundidad(grafo: Grafo, inicio: str, destino: str) -> Optional[List[str]]:
    """
    DFS iterativo con pila.
    Devuelve una ruta (no necesariamente la más corta) o None si no hay.
    """
    pila: List[List[str]] = [[inicio]]  # cada elemento es un camino parcial
    visitados = set()

    while pila:
        camino = pila.pop()          # saco el ÚLTIMO camino (LIFO)
        nodo = camino[-1]

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == destino:
            return camino

        # Empuja vecinos como nuevos caminos
        # (revertimos para que el orden de expansión sea controlable/legible)
        for vecino in reversed(grafo.get(nodo, [])):
            if vecino not in visitados:
                pila.append(camino + [vecino])

    return None

def demo_ciudad():
    ciudad: Grafo = {
        "Casa":    ["Av1", "Mercado"],
        "Av1":     ["Plaza", "Parque"],
        "Plaza":   ["Escuela"],
        "Parque":  ["Hospital"],
        "Mercado": [],
        "Escuela": [],
        "Hospital": []
    }

    origen, destino = "Casa", "Hospital"
    ruta = dfs_en_profundidad(ciudad, origen, destino)

    if ruta:
        print("Ruta encontrada por DFS (profundidad):")
        print("  " + " → ".join(ruta))
        print(f"Cruces recorridos: {len(ruta)-1}")
    else:
        print("No hay ruta disponible.")

if __name__ == "__main__":
    demo_ciudad()
