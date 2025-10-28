# 11_Ascension_Colinas.
# El GPS sube "colinas" eligiendo siempre el vecino con mejor heurística.

from typing import Dict, List, Optional  # tipos para anotaciones
import random  # import opcional (no se usa en esta versión simple)


# Grafo simple: cada nodo lista sus vecinos (no ponderado)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Plaza", "Casa"],
    "Mercado": ["Plaza"],
    "Plaza": ["Parque"],
    "Parque": ["Hospital"],
    "Hospital": []
}


# Heurística: estimación de la distancia restante al Hospital (valores menores = mejor)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Mercado": 7,
    "Plaza": 5,
    "Parque": 2,
    "Hospital": 0
}


def hill_climbing(grafo: Dict[str, List[str]], inicio: str, destino: str) -> List[str]:
    """
    Búsqueda por Ascensión de Colinas (Hill Climbing).

    - Estrategia: desde el nodo actual, elegir siempre el vecino con menor valor
      heurístico (es decir, el que "parece" más cercano al objetivo).
    - Si ningún vecino mejora la heurística, el algoritmo se detiene: hemos
      alcanzado un máximo local (no necesariamente el objetivo).
    - devuelve el camino seguido por el GPS hasta que se detiene.
    """

    # Nodo donde estamos y camino recorrido
    actual = inicio
    camino = [actual]

    print(f"Iniciando en: {actual} (h={h[actual]})")

    while True:
        vecinos = grafo.get(actual, [])  # vecinos del nodo actual
        if not vecinos:
            # No hay vecinos: no podemos avanzar
            print("No hay más caminos.")
            break

        # Seleccionamos el vecino con la menor heurística (mejor según la 'intuición')
        mejor_vecino = min(vecinos, key=lambda n: h[n])

        # Si el mejor vecino mejora la heurística, avanzamos hacia él
        if h[mejor_vecino] < h[actual]:
            actual = mejor_vecino
            camino.append(actual)
            print(f"→ Avanzando a {actual} (h={h[actual]})")
        else:
            # Ningún vecino mejora: estamos en un máximo local y paramos
            print(f"Sin mejora desde {actual}. GPS detenido en un máximo local.")
            break

        # Si alcanzamos el destino, terminamos con éxito
        if actual == destino:
            print("¡Destino alcanzado!")
            break

    return camino


def demo_colinas():
    origen, destino = "Casa", "Hospital"
    camino = hill_climbing(grafo, origen, destino)

    print("\nRuta seguida por el GPS:")
    print("  " + " → ".join(camino))
    # Mostramos la heurística del nodo final (puede no ser 0 si quedó en máximo local)
    print(f"Heurística final: {h[camino[-1]]}")


if __name__ == "__main__":
    demo_colinas()
