# 03_DFS_explorador_profundo.
# Explora una ruta hasta el fondo antes de retroceder.

from typing import Dict, List, Optional  # tipos para anotaciones

Grafo = Dict[str, List[str]]  # grafo: nodo -> lista de vecinos


def dfs_en_profundidad(grafo: Grafo, inicio: str, destino: str) -> Optional[List[str]]:
    """
    DFS iterativo usando una pila.
    Devuelve una ruta desde inicio hasta destino (puede no ser la más corta)
    o None si no existe ruta.
    """

    # Pila de caminos: cada elemento es una lista que representa un camino desde inicio
    pila: List[List[str]] = [[inicio]]  # cada elemento es un camino parcial

    # Conjunto de nodos ya visitados para evitar procesarlos varias veces
    visitados = set()

    # Mientras haya caminos por explorar en la pila
    while pila:
        # Sacamos el último camino añadido (LIFO -> profundidad)
        camino = pila.pop()          # saco el ÚLTIMO camino (LIFO)
        nodo = camino[-1]            # el nodo actual es el último del camino

        # Si ya visitamos este nodo, lo saltamos
        if nodo in visitados:
            continue
        # Marcamos el nodo como visitado
        visitados.add(nodo)

        # Si llegamos al destino, devolvemos el camino completo
        if nodo == destino:
            return camino

        # Empujamos los vecinos como nuevos caminos en la pila
        # Revertimos el orden para controlar el orden de expansión
        for vecino in reversed(grafo.get(nodo, [])):
            # Sólo añadimos vecinos no visitados
            if vecino not in visitados:
                pila.append(camino + [vecino])

    # Si agotamos la pila sin encontrar destino, no hay ruta
    return None


def demo_ciudad():
    # Definición simple del mapa de la ciudad (lista de vecinos por nodo)
    ciudad: Grafo = {
        "Casa":    ["Av1", "Mercado"],
        "Av1":     ["Plaza", "Parque"],
        "Plaza":   ["Escuela"],
        "Parque":  ["Hospital"],
        "Mercado": [],
        "Escuela": [],
        "Hospital": []
    }

    # Origen y destino de ejemplo
    origen, destino = "Casa", "Hospital"

    # Ejecutamos DFS en profundidad para encontrar una ruta
    ruta = dfs_en_profundidad(ciudad, origen, destino)

    # Imprimimos resultados si se encuentra una ruta
    if ruta:
        print("Ruta encontrada por DFS (profundidad):")
        print("  " + " → ".join(ruta))
        print(f"Cruces recorridos: {len(ruta)-1}")
    else:
        print("No hay ruta disponible.")


if __name__ == "__main__":
    demo_ciudad()
