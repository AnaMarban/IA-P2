# 10_Busqueda_Astar_AOstar.py
# GPS Inteligente - Módulo 10: Búsquedas A* y AO*
# A* combina costo real (g) + heurística (h).
# AO* es una versión avanzada para decisiones en grafos AND/OR.

import heapq
from typing import Dict, List, Tuple, Optional

# Mapa urbano con costos (g)
grafo: Dict[str, List[Tuple[str, int]]] = {
    "Casa":     [("Av1", 4), ("Parque", 3)],
    "Av1":      [("Casa", 4), ("Plaza", 2), ("Parque", 5)],
    "Plaza":    [("Av1", 2), ("Escuela", 6)],
    "Parque":   [("Casa", 3), ("Av1", 5), ("Hospital", 2)],
    "Escuela":  [("Plaza", 6)],
    "Hospital": [("Parque", 2)]
}

# Heurística (h)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 5,
    "Escuela": 4,
    "Parque": 2,
    "Hospital": 0
}

def a_estrella(
    grafo: Dict[str, List[Tuple[str, int]]],
    inicio: str,
    destino: str
) -> Optional[Tuple[List[str], int]]:
    """
    Búsqueda A*: f(n) = g(n) + h(n)
    g = costo acumulado, h = estimación al destino.
    """
    cola = [(h[inicio], 0, [inicio])]  # (f = g + h, g, camino)
    visitados = {}

    while cola:
        f, g, camino = heapq.heappop(cola)
        nodo = camino[-1]

        # Si ya visitamos con menor costo, saltamos
        if nodo in visitados and g >= visitados[nodo]:
            continue
        visitados[nodo] = g

        if nodo == destino:
            return camino, g

        for vecino, costo in grafo.get(nodo, []):
            g_nuevo = g + costo
            f_nuevo = g_nuevo + h[vecino]
            heapq.heappush(cola, (f_nuevo, g_nuevo, camino + [vecino]))

    return None


def demo_Astar():
    origen, destino = "Casa", "Hospital"
    resultado = a_estrella(grafo, origen, destino)

    print("== Búsqueda A* (A Estrella) ==")
    if resultado:
        ruta, costo = resultado
        print("Ruta óptima encontrada:")
        print("  " + " → ".join(ruta))
        print(f"Costo total: {costo}")
    else:
        print("No hay ruta al destino.")


# ======================================================
#  AO* (AND-OR Graph Search) – versión conceptual
# ======================================================

"""
AO* se usa cuando hay decisiones condicionales o tareas paralelas.
Por ejemplo:
- Para llegar al Hospital, puedes ir por Parque (OR)
  o primero pasar por Av1 **y** luego Plaza (AND).

En este caso, AO* elige el mejor conjunto de caminos combinando costos y heurísticas.
"""

def explicar_AOstar():
    print("\n== AO* (AND-OR Search) ==")
    print("Este método se usa en problemas con decisiones combinadas:")
    print("  Ejemplo:")
    print("  • Ir al Hospital por Parque (opción 1)")
    print("  • Ir por Av1 → Plaza → Hospital (opción 2)")
    print("  Si la opción 2 implica pasos que dependen unos de otros (AND),")
    print("  AO* calcula la combinación óptima de ambos caminos.")
    print("\nA* busca un solo camino; AO* puede combinar subrutas con condiciones.")


if __name__ == "__main__":
    demo_Astar()
    explicar_AOstar()
