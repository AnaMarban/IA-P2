# 02_UCS_menos_distancia.
# Encuentra la ruta con MENOR DISTANCIA (o tiempo).

import heapq  # heapq proporciona una cola de prioridad (min-heap)
from typing import Dict, List, Tuple, Optional  # anotaciones de tipos

# Cada conexión tiene un costo: ciudad[origen] = [(destino, costo), ...]
Grafo = Dict[str, List[Tuple[str, int]]]


def ucs_menos_distancia(grafo: Grafo, inicio: str, destino: str) -> Optional[Tuple[List[str], int]]:
    """
    Búsqueda de Costo Uniforme (Uniform Cost Search)
    Encuentra la ruta con menor costo total.
    Devuelve una tupla (camino, costo_total) o None si no hay ruta.
    """

    # Cola de prioridad: tuplas (costo_acumulado, camino_completo)
    # Empezamos con costo 0 y camino que contiene sólo el nodo inicio
    cola = [(0, [inicio])]  # (costo acumulado, camino)

    # Conjunto de nodos ya procesados (cuando los sacamos de la cola por primera vez)
    visitados = set()

    # Mientras haya nodos por explorar en la cola
    while cola:
        # Sacamos el elemento con menor costo acumulado
        costo, camino = heapq.heappop(cola)

        # El nodo actual es el último del camino
        nodo = camino[-1]

        # Si ya procesamos este nodo, lo ignoramos (evita trabajo repetido)
        if nodo in visitados:
            continue

        # Marcamos el nodo como procesado
        visitados.add(nodo)

        # Si es el destino, hemos encontrado la ruta de menor costo
        if nodo == destino:
            return camino, costo

        # Si no es destino, expandimos sus vecinos
        for vecino, peso in grafo.get(nodo, []):
            # Sólo consideramos vecinos no procesados
            if vecino not in visitados:
                # Nuevo costo acumulado si vamos al vecino desde el camino actual
                nuevo_costo = costo + peso

                # Insertamos en la cola de prioridad el nuevo camino y su costo
                heapq.heappush(cola, (nuevo_costo, camino + [vecino]))

    # Si la cola se vacía y no encontramos destino, no hay ruta
    return None


def demo_ciudad():
    # Mapa de la ciudad con DISTANCIAS (por ejemplo, en minutos)
    ciudad: Grafo = {
        "Casa":     [("Av1", 4), ("Parque", 3)],
        "Av1":      [("Casa", 4), ("Plaza", 2), ("Parque", 5)],
        "Plaza":    [("Av1", 2), ("Escuela", 6), ("Mercado", 4)],
        "Parque":   [("Casa", 3), ("Av1", 5), ("Hospital", 2), ("Mercado", 8)],
        "Mercado":  [("Plaza", 4), ("Parque", 8), ("Hospital", 3)],
        "Escuela":  [("Plaza", 6)],
        "Hospital": [("Parque", 2), ("Mercado", 3)],
    }

    # Definimos origen y destino para la demostración
    origen, destino = "Casa", "Hospital"

    # Ejecutamos UCS para encontrar la ruta más barata (menos tiempo/distancia)
    resultado = ucs_menos_distancia(ciudad, origen, destino)

    # Si se encontró una ruta, imprimimos la secuencia y el costo total
    if resultado:
        ruta, costo_total = resultado
        print("Ruta con MENOR distancia:")
        print("  " + " → ".join(ruta))
        print(f"Distancia total: {costo_total} unidades")
    else:
        # Si no hay ruta, avisamos
        print("No hay ruta encontrada.")


if __name__ == "__main__":
    demo_ciudad()
