# 10_Busqueda_Astar_AOstar.
# A* combina costo real (g) + heurística (h). AO* es una versión conceptual para grafos AND/OR.

import heapq  # cola de prioridad para A*
from typing import Dict, List, Tuple, Optional


# Mapa urbano con costos reales (g): cada tupla es (vecino, costo)
grafo: Dict[str, List[Tuple[str, int]]] = {
    "Casa":     [("Av1", 4), ("Parque", 3)],
    "Av1":      [("Casa", 4), ("Plaza", 2), ("Parque", 5)],
    "Plaza":    [("Av1", 2), ("Escuela", 6)],
    "Parque":   [("Casa", 3), ("Av1", 5), ("Hospital", 2)],
    "Escuela":  [("Plaza", 6)],
    "Hospital": [("Parque", 2)]
}


# Heurística (h): estimación restante al destino (Hospital)
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
    Búsqueda A* (A estrella).

    f(n) = g(n) + h(n)
    - g(n): costo acumulado desde el inicio hasta n.
    - h(n): estimación heurística desde n hasta el destino.

    La cola guarda tuplas (f, g, camino) y se extrae el menor f.
    """

    # Inicializamos la cola con f = h(inicio), g = 0 y el camino que contiene inicio
    cola = [(h[inicio], 0, [inicio])]  # (f = g + h, g, camino)

    # Diccionario para registrar el mejor g conocido por cada nodo (costo real mínimo visto)
    visitados = {}

    while cola:
        f, g, camino = heapq.heappop(cola)
        nodo = camino[-1]

        # Si ya visitamos este nodo con un g menor o igual, no vale la pena procesarlo
        if nodo in visitados and g >= visitados[nodo]:
            continue
        # Guardamos el mejor g encontrado para 'nodo'
        visitados[nodo] = g

        # Si llegamos al destino, devolvemos el camino y el costo real g
        if nodo == destino:
            return camino, g

        # Expandimos vecinos: calculamos sus g y f y los añadimos a la cola
        for vecino, costo in grafo.get(nodo, []):
            g_nuevo = g + costo
            f_nuevo = g_nuevo + h[vecino]
            heapq.heappush(cola, (f_nuevo, g_nuevo, camino + [vecino]))

    # Si agotamos la cola sin encontrar destino, no hay ruta
    return None


def demo_Astar():
    # Demo rápida de A* sobre el grafo definido arriba
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

AO* elige el mejor conjunto de caminos combinando costos y heurísticas
en problemas donde algunas acciones deben combinarse (AND) y otras son alternativas (OR).
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
