# 05_Profundidad_Iterativa.py
# GPS Inteligente - Módulo 5: Búsqueda en Profundidad Iterativa (IDDFS)
# Combina DLS con límites crecientes: 1, 2, 3, ... hasta encontrar destino.

from typing import Dict, List, Optional, Tuple, Literal

Grafo = Dict[str, List[str]]
Status = Literal["success", "cutoff", "failure"]

def dls(grafo: Grafo, actual: str, destino: str, limite: int, visitados: Optional[set] = None) -> Tuple[Status, Optional[List[str]]]:
    """Búsqueda en profundidad con límite (DLS) — versión recursiva."""
    if visitados is None:
        visitados = set()
    if actual == destino:
        return "success", [actual]
    if limite == 0:
        return "cutoff", None

    visitados.add(actual)
    hubo_cutoff = False
    for vecino in grafo.get(actual, []):
        if vecino in visitados:
            continue
        status, subcamino = dls(grafo, vecino, destino, limite - 1, visitados)
        if status == "success":
            return "success", [actual] + subcamino
        if status == "cutoff":
            hubo_cutoff = True
    visitados.remove(actual)
    return ("cutoff", None) if hubo_cutoff else ("failure", None)

def iddfs(grafo: Grafo, inicio: str, destino: str, limite_max: int) -> Optional[List[str]]:
    """
    Profundidad Iterativa: prueba límites 0..limite_max.
    Devuelve el primer camino encontrado (mínimo en número de pasos) o None.
    """
    for limite in range(limite_max + 1):
        status, camino = dls(grafo, inicio, destino, limite, set())
        # Puedes imprimir el estado de cada iteración si quieres ver el “crecimiento”
        # print(f"[Iteración límite={limite}] -> {status}")
        if status == "success":
            return camino
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
