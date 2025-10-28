# 05_Profundidad_Iterativa.
# Combina DLS con límites crecientes: 1, 2, 3, ... hasta encontrar destino.

from typing import Dict, List, Optional, Tuple, Literal  # anotaciones de tipos

# Grafo simple: nodo -> lista de vecinos
Grafo = Dict[str, List[str]]

# Estados que devuelve la DLS: success (encontró), cutoff (límite alcanzado), failure (sin camino)
Status = Literal["success", "cutoff", "failure"]


def dls(grafo: Grafo, actual: str, destino: str, limite: int, visitados: Optional[set] = None) -> Tuple[Status, Optional[List[str]]]:
    """Búsqueda en profundidad con límite (DLS) — versión recursiva.

    Devuelve una tupla (status, camino) donde 'status' indica si se encontró el destino,
    si se alcanzó el límite ('cutoff') o si la ruta fracasó ('failure').
    """

    # Inicializa el conjunto de visitados la primera vez
    if visitados is None:
        visitados = set()

    # Si ya estamos en el destino, devolvemos éxito con el camino que contiene sólo 'actual'
    if actual == destino:
        return "success", [actual]

    # Si no queda profundidad para explorar, devolvemos 'cutoff' (podría continuarse aumentando el límite)
    if limite == 0:
        return "cutoff", None

    # Marcamos el nodo actual como visitado para evitar ciclos
    visitados.add(actual)
    hubo_cutoff = False  # indicador si alguna rama alcanzó el límite

    # Recorremos sus vecinos
    for vecino in grafo.get(actual, []):
        # Saltamos vecinos ya visitados
        if vecino in visitados:
            continue

        # Llamada recursiva reduciendo el límite en 1
        status, subcamino = dls(grafo, vecino, destino, limite - 1, visitados)

        # Si una rama tuvo éxito, construimos el camino completo y devolvemos
        if status == "success":
            return "success", [actual] + subcamino

        # Si alguna rama fue 'cutoff', lo anotamos para informar que faltó profundidad
        if status == "cutoff":
            hubo_cutoff = True

    # Al hacer backtrack, quitamos 'actual' de visitados para otras rutas alternativas
    visitados.remove(actual)

    # Si hubo al menos un 'cutoff', devolvemos 'cutoff', sino 'failure'
    return ("cutoff", None) if hubo_cutoff else ("failure", None)


def iddfs(grafo: Grafo, inicio: str, destino: str, limite_max: int) -> Optional[List[str]]:
    """
    Profundidad Iterativa (IDDFS): incrementa el límite desde 0 hasta 'limite_max'
    y ejecuta DLS en cada paso. Devuelve el primer camino encontrado o None.
    """

    # Probamos límites crecientes; el primer 'success' nos da un camino de longitud mínima
    for limite in range(limite_max + 1):
        status, camino = dls(grafo, inicio, destino, limite, set())
        # Puedes descomentar la siguiente línea para ver el estado de cada iteración
        # print(f"[Iteración límite={limite}] -> {status}")
        if status == "success":
            return camino
    # Si agotamos hasta limite_max sin éxito, devolvemos None
    return None


def demo_ciudad():
    # Grafo de ejemplo (ciudad) con vecinos para cada nodo
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

    # Caso 1: límite pequeño (no llega)
    camino = iddfs(ciudad, origen, destino, limite_max=2)
    print("== IDDFS con límite_max=2 ==")
    print("Ruta:", " → ".join(camino) if camino else "No encontrada")
    print()

    # Caso 2: límite suficiente (sí llega)
    camino = iddfs(ciudad, origen, destino, limite_max=3)
    print("== IDDFS con límite_max=3 ==")
    print("Ruta:", " → ".join(camino) if camino else "No encontrada")


if __name__ == "__main__":
    demo_ciudad()
