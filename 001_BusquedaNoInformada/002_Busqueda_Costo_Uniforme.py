# 02_UCS_menos_distancia.
# Encuentra la ruta con MENOR DISTANCIA (o tiempo).

import heapq
from typing import Dict, List, Tuple, Optional

# Cada conexión tiene un costo: ciudad[origen] = [(destino, costo), ...]
Grafo = Dict[str, List[Tuple[str, int]]]

def ucs_menos_distancia(grafo: Grafo, inicio: str, destino: str) -> Optional[Tuple[List[str], int]]:
    """
    Búsqueda de Costo Uniforme (Uniform Cost Search)
    Encuentra la ruta con menor costo total.
    """
    cola = [(0, [inicio])]  # (costo acumulado, camino)
    visitados = set()

    while cola:
        costo, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == destino:
            return camino, costo

        for vecino, peso in grafo.get(nodo, []):
            if vecino not in visitados:
                nuevo_costo = costo + peso
                heapq.heappush(cola, (nuevo_costo, camino + [vecino]))

    return None

def demo_ciudad():
    # Mapa de la ciudad con DISTANCIAS (en minutos)
    ciudad: Grafo = {
        "Casa":     [("Av1", 4), ("Parque", 3)],
        "Av1":      [("Casa", 4), ("Plaza", 2), ("Parque", 5)],
        "Plaza":    [("Av1", 2), ("Escuela", 6), ("Mercado", 4)],
        "Parque":   [("Casa", 3), ("Av1", 5), ("Hospital", 2), ("Mercado", 8)],
        "Mercado":  [("Plaza", 4), ("Parque", 8), ("Hospital", 3)],
        "Escuela":  [("Plaza", 6)],
        "Hospital": [("Parque", 2), ("Mercado", 3)],
    }

    origen, destino = "Casa", "Hospital"
    resultado = ucs_menos_distancia(ciudad, origen, destino)

    if resultado:
        ruta, costo_total = resultado
        print("Ruta con MENOR distancia:")
        print("  " + " → ".join(ruta))
        print(f"Distancia total: {costo_total} unidades")
    else:
        print("No hay ruta encontrada.")

if __name__ == "__main__":
    demo_ciudad()
