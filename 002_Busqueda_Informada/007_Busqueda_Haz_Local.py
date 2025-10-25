# 14_Busqueda_HazLocal.py
# GPS Inteligente - Módulo 14: Búsqueda de Haz Local (Local Beam Search)
# Varios GPS cooperan, compartiendo los mejores caminos.

from typing import Dict, List, Tuple
import heapq

# Grafo urbano (conexiones)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Casa", "Plaza"],
    "Plaza": ["Av1", "Parque", "Mercado"],
    "Parque": ["Plaza", "Hospital"],
    "Mercado": ["Casa", "Plaza"],
    "Hospital": ["Parque"]
}

# Heurística (distancia estimada al Hospital)
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
    - Mantiene k mejores rutas activas.
    - En cada paso, expande todas y conserva las mejores k.
    """
    # Rutas activas: (heurística total, [camino])
    rutas = [(h[i], [i]) for i in inicios]
    heapq.heapify(rutas)
    mejor_camino = None
    mejor_h = float("inf")

    print(f"Inicios: {', '.join(inicios)}\n")

    for paso in range(max_iter):
        nuevas_rutas = []
        print(f"--- Iteración {paso+1} ---")

        # Expandir cada camino actual
        for _, camino in rutas:
            nodo_actual = camino[-1]
            if nodo_actual == destino:
                return camino, h[nodo_actual]
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in camino:
                    nueva_ruta = camino + [vecino]
                    heapq.heappush(nuevas_rutas, (h[vecino], nueva_ruta))
                    print(f"  Expandiendo {camino[-1]} → {vecino} (h={h[vecino]})")

        # Mantener solo los mejores k caminos
        rutas = heapq.nsmallest(k, nuevas_rutas)

        # Mostrar los mejores caminos actuales
        print("  Mejores rutas ahora:")
        for heur, camino in rutas:
            print(f"   - {' → '.join(camino)} (h={heur})")

        # Actualizar mejor general
        if rutas and rutas[0][0] < mejor_h:
            mejor_camino = rutas[0][1]
            mejor_h = rutas[0][0]

        if not rutas:
            print("No hay más rutas para expandir.")
            break

    return mejor_camino or [], mejor_h


def demo_haz_local():
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
