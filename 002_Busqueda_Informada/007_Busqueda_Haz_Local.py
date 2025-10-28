# 14_Busqueda_HazLocal.
# Varios GPS cooperan, compartiendo los mejores caminos (Local Beam Search).

from typing import Dict, List, Tuple
import heapq  # usamos heap para seleccionar las mejores rutas según la heurística


# Grafo urbano (lista de vecinos por nodo)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Casa", "Plaza"],
    "Plaza": ["Av1", "Parque", "Mercado"],
    "Parque": ["Plaza", "Hospital"],
    "Mercado": ["Casa", "Plaza"],
    "Hospital": ["Parque"]
}


# Heurística: estimación de distancia restante al Hospital (menor = mejor)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 4,
    "Parque": 2,
    "Mercado": 5,
    "Hospital": 0
}


def local_beam_search(
    grafo: Dict[str, List[str]],
    inicios: List[str],
    destino: str,
    k: int = 2,
    max_iter: int = 10
) -> Tuple[List[str], int]:
    """
    Local Beam Search:
    - Mantiene k mejores rutas activas (haz local de tamaño k).
    - En cada iteración, expande todas las rutas activas y
      conserva sólo las k mejores según la heurística.

    Parámetros:
    - inicios: lista de nodos iniciales (varios GPS parten desde distintos puntos).
    - destino: nodo objetivo.
    - k: cuántas rutas mantener activas cada paso.
    - max_iter: máximo de iteraciones.

    Retorna: (mejor_camino_encontrado, heurística_del_nodo_final)
    """

    # Inicializamos las rutas activas con cada inicio: tuple (heurística, camino)
    rutas: List[Tuple[int, List[str]]] = [(h[i], [i]) for i in inicios]
    heapq.heapify(rutas)

    mejor_camino = None
    mejor_h = float("inf")

    print(f"Inicios: {', '.join(inicios)}\n")

    # Iteramos hasta max_iter veces o hasta que no haya más rutas
    for paso in range(max_iter):
        nuevas_rutas: List[Tuple[int, List[str]]] = []
        print(f"--- Iteración {paso+1} ---")

        # Expandir cada camino activo
        for _, camino in rutas:
            nodo_actual = camino[-1]

            # Si una ruta ya llegó al destino, la devolvemos inmediatamente
            if nodo_actual == destino:
                return camino, h[nodo_actual]

            # Expandimos hacia los vecinos no visitados del camino actual
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in camino:
                    nueva_ruta = camino + [vecino]
                    # Guardamos la ruta con su heurística (se usa h del último nodo)
                    heapq.heappush(nuevas_rutas, (h[vecino], nueva_ruta))
                    print(f"  Expandiendo {camino[-1]} → {vecino} (h={h[vecino]})")

        # Conservamos sólo las k rutas con menor heurística total entre las nuevas
        rutas = heapq.nsmallest(k, nuevas_rutas)

        # Mostrar las rutas que quedaron activas tras la poda
        print("  Mejores rutas ahora:")
        for heur, camino in rutas:
            print(f"   - {' → '.join(camino)} (h={heur})")

        # Actualizamos el mejor global si encontramos una ruta con heurística menor
        if rutas and rutas[0][0] < mejor_h:
            mejor_camino = rutas[0][1]
            mejor_h = rutas[0][0]

        # Si no quedan rutas por expandir, terminamos
        if not rutas:
            print("No hay más rutas para expandir.")
            break

    # Devolvemos la mejor ruta encontrada (o lista vacía) y su heurística
    return mejor_camino or [], mejor_h


def demo_haz_local():
    # Dos GPS parten desde distintos puntos: 'Casa' y 'Mercado'
    inicios = ["Casa", "Mercado"]
    destino = "Hospital"
    ruta, heur_final = local_beam_search(grafo, inicios, destino, k=2)

    print("\nRuta encontrada por el equipo de GPS:")
    if ruta:
        print("  " + " → ".join(ruta))
        print(f"Heurística final: {heur_final}")
    else:
        print("No se encontró ruta.")


if __name__ == "__main__":
    demo_haz_local()
